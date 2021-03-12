# MultiMediate Challenge 2021

This repository contains the starter code for the challenge as well as participation instructions. For more information about the challenge,
visit [multimediate-challenge.org](https://multimediate-challenge.org).

### Procedure

In this challenge, participants will receive training and validation data that they can use to build solutions for each challenge sub-task (eye contact detection and
next speaker prediction). The evaluation of these approaches will then be performed remotely on our side with the test portion of the dataset. 
For that, participants will create and upload docker images with their solutions that are then evaluated on our systems.

### Repository Structure

The starter code repository is intended for Python-based approaches and consists of the following files and folders:

```
.
├── output                                     # Output folder for predictions
│   ├── example_prediction_eye_contact.csv     # Example prediction file for eye contact task
│   └── example_prediction_next_speaker.csv    # Example prediction file for next speaker task
├── submission                                 # All files in this folder will be contained in the docker images
│   ├── utils
|       └── data_loader.py                     # Contains helper functions to load sample video/audio data
│   ├── main_eye_contact.py                    # Main file executed in the docker image for the eye contact task
│   ├── main_next_speaker.py                   # Main file executed in the docker image for the next speaker task
│   ├── participant_eye_contact.py             # Add your prediction code for eye contact task here
│   └── participant_next_speaker.py            # Add your prediction code for next speaker task here
├── EyeContact.Dockerfile                      # Dockerfile definition for eye contact task
├── NextSpeaker.Dockerfile                     # Dockerfile definition for next speaker task 
├── requirements-eye-contact.txt               # Add required python packages for eye contact task here (used in docker image)
├── requirements-next-speaker.txt              # Add required python packages for next speaker task here (used in docker image)
├── run.py                                     # Helper script to run evaluation locally or in docker container
```

From these files the following are the most important ones:

`submission/participant_eye_contact.py` This file is intended for the eye contact prediction code of the participants.

`submission/participant_next_speaker.py` This file is intended for the next speaker prediction code of the participants.

`run.py` This file can be used to test the evaluation directly or in a docker container. 
It supports the following parameters:
* `-t <task>` Select which task should be used (`eye_contact` or `next_speaker`)
* `-p "<path/to/dataset location>"` Path to the dataset location
* `-i "<image name>"` Name of the docker image prefix (default: `multimediate`)
* `-d` If this flag is set, the script will create and run a docker image with the name `<image name>_<task>` (e.g., `multimediate_eye_contact`)

Example usages:
```bash
# Run evaluation of eye contact task directly
python run.py -t eye_contact -p "/path/to/challenge dataset"

# Run evaluation of next speaker task directly
python run.py -t next_speaker -p "/path/to/challenge dataset"

# Run evaluation of eye contact task in docker container
python run.py -t eye_contact -p "/path/to/challenge dataset" -d

# Run evaluation of next speaker task in docker container
python run.py -t next_speaker -p "/path/to/challenge dataset" -d
```

### Docker Information (optional)
The `run.py` script in this repository can be used to create appropriate docker images to participate in the challenge.
However, participants can also create their own docker images as long as they comply with the following evaluation conditions:

* The root directory of the dataset will be mapped to `/input/` in the docker image (i.e., the `data` folder will be available at `/input/data/`).
* The name of the sample list file will be stored in the environment variable `MULTIMEDIATE_SAMPLE_FILE` (e.g., `test_eye_contact.csv`). The file will have the same structure as the provided sample lists (see folder `sample_lists` in the dataset).
* Based on the sample list file and the provided dataset location, the docker image should produce prediction files with the same structure as the examples in the `output` folder and write them to the folder `/code/output/` within the docker image.

## Participation Guide

The following steps should be performed to participate in the challenge:

### Initial Setup

1. Clone the challenge repository:
   
   ```bash
   git clone https://github.com/hcmlab/multimediate-participants.git
   ```

1. Download dataset from [here](https://TODO).

1. Implement prediction code for the respective tasks in the following files:
   
   * Eye contact task: `submission/participant_eye_contact.py`
   
   * Next speaker task: `submission/participant_next_speaker.py`

1. _(Optional)_ Add required Python packages for the respective tasks to the following files:

   * Eye contact task: `requirements-eye-contact.txt`
   
   * Next speaker task: `requirements-next-speaker.txt`

1. _(Optional)_ Modify Dockerfile for respective tasks:

   * Eye contact task: `EyeContact.Dockerfile`
   
   * Next speaker task: `NextSpeaker.Dockerfile`

### Test Prediction Code
1. Run evaluation script on validation data:
   
   ```bash
   # Eye contact task
   python run.py -t eye_contact -p "/path/to/challenge dataset"
   
   # Next speaker task
   python run.py -t next_speaker -p "/path/to/challenge dataset"
   ```
   
   The result should be similar to the one below. _If no error occurs, go to the next step._

   ```
   Running code for task eye_contact directly
   Successfully calculated eye contact predictions.
   Eye contact accuracy: 0.17763157894736842
   ```

1. Add the `-d` flag to see if the code also works inside a docker image:

   ```bash
   # Eye contact task
   python run.py -t eye_contact -p "/path/to/challenge dataset" -d
   
   # Next speaker task
   python run.py -t next_speaker -p "/path/to/challenge dataset" -d
   ```
   
   The result should be similar to the one below. _If no error occurs, go to the next step._

   ```
   Running code for task eye_contact in docker container
   Building image: multimediate_eye_contact
   Building image completed. Running image:
   Successfully calculated eye contact predictions. 
   Eye contact accuracy: 0.17763157894736842
   ```
   
1. Check the docker image names by running the following command:

   ```bash
   docker images
   ```
   
   The result should be similar to the one below:
   
   ```bash
   REPOSITORY                     TAG         IMAGE ID          CREATED          SIZE
   multimediate_eye_contact       latest      5689a6cd5444      1 hours ago      833MB
   multimediate_next_speaker      latest      46677483e0f0      1 hours ago      833MB
   ```


### Online Submission

1. Join the challenge on [EvalAI](https://TODO) if you have not done this already:
    * Create an account and a participant team.
    * Go to the [EvalAI challenge page](https://TODO) and participate with your team.

1. Install EvalAI command line interface:

   ```bash
   pip install evalai
   ```

1. Set EvalAI account token (you can get it from [here](https://eval.ai/web/profile)):

   ```bash
   evalai set_token <your EvalAI participant token>
   ```

1. Push docker image to EvalAI docker registry:

   ```bash
   evalai push <docker image name>:<image tag> --phase <phase name>
   ```
   
   Examples:
   
   ```bash
   # Eye contact
   evalai push multimediate_eye_contact:latest --phase multimediate-eye-contact-501
   
   # Next speaker
   evalai push multimediate_next_speaker:latest --phase multimediate-next-speaker-501
   ```

1. Check the status of your submission on the [EvalAI challenge page](https://TODO).