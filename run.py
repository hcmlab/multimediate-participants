import argparse
import os
import sys

import docker
import pandas as pd
from sklearn.metrics import recall_score, accuracy_score

# Task names
NEXT_SPEAKER = 'next_speaker'
EYE_CONTACT = 'eye_contact'


def run_docker(task_name, image_name, data_path, sample_file):
    # Get absolute path
    data_path = os.path.abspath(data_path)

    # Get docker client
    client = docker.from_env()

    # Set Dockerfile
    docker_file = 'NextSpeaker.Dockerfile'
    if task_name == EYE_CONTACT:
        docker_file = 'EyeContact.Dockerfile'

    docker_image_name = '{}_{}'.format(image_name, task_name)
    print('Building image: {}'.format(docker_image_name))

    # Build docker image (sudo docker build -f NextSpeaker.Dockerfile -t multimediate-next-speaker .)
    client.images.build(path='.', dockerfile=docker_file, tag=docker_image_name)

    # Configure mounted container volumes
    output_dir = os.path.join(os.getcwd(), 'output')
    volumes = {data_path: {'bind': '/input', 'mode': 'ro'}, output_dir: {'bind': '/code/output', 'mode': 'rw'}}
    print('Building image completed. Running image:')

    env = ['MULTIMEDIATE_SAMPLE_FILE={}'.format(sample_file)]

    # Run docker container (sudo docker run -it --rm -e MULTIMEDIATE_SAMPLE_FILE=validation-next-speaker.csv -v $PWD/input:/input -v $PWD/output:/code/output multimediate-next-speaker)
    container_log = client.containers.run(docker_image_name, volumes=volumes, environment=env, remove=True, stdin_open=True, tty=True, network_disabled=True)

    # Print docker container output
    print(container_log.decode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--task', required=True, choices=[NEXT_SPEAKER, EYE_CONTACT], help='challenge task')
    parser.add_argument('-p', '--path', required=True, type=str, help='path to input data')
    parser.add_argument('-d', '--docker', action='store_true', help='run code in docker container')
    parser.add_argument('-i', '--image', type=str, default='multimediate', help='docker image name')
    parser.add_argument('-s', '--samples', type=str, default='val', help='')

    args = parser.parse_args()

    sample_file_name = '{}_{}.csv'.format(args.samples, args.task)

    if args.docker:
        print('Running code for task {} in docker container'.format(args.task))

        run_docker(args.task, args.image, args.path, sample_file_name)
    else:
        print('Running code for task {} directly'.format(args.task))

        # Fix module import
        sys.path.append('./submission')

        if args.task == NEXT_SPEAKER:
            from submission.main_next_speaker import predict
        else:
            from submission.main_eye_contact import predict

        predict(args.path, sample_file_name)

    # Get labels and predictions
    sample_file_abs = os.path.join(args.path, sample_file_name)
    prediction_file = os.path.join('output', 'prediction_{}.csv'.format(args.task))

    df_labels = pd.read_csv(sample_file_abs, index_col='index')
    df_predictions = pd.read_csv(prediction_file, index_col='index')

    df_combined = pd.concat([df_labels, df_predictions], axis=1)

    labels = []
    predictions = []

    # Iterate over all samples
    for index, row in df_combined.iterrows():
        if args.task == NEXT_SPEAKER:
            for i in range(1, 5):
                labels.append(row['label_{}'.format(i)])
                predictions.append(row['prediction_{}'.format(i)])
        else:
            labels.append(row['label'])
            predictions.append(row['prediction'])

    # Evaluate predictions
    if args.task == NEXT_SPEAKER:
        print('Next speaker unweighted average recall: {}'.format(recall_score(labels, predictions, average='macro')))
    else:
        print('Eye contact accuracy: {}'.format(accuracy_score(labels, predictions)))
