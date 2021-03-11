import os
import sys

import pandas as pd

import participant_next_speaker
from utils import data_loader


def predict(data_path, sample_file):
    try:
        # Get absolute sample file
        sample_file_abs = os.path.join(data_path, sample_file)

        # Load sample list
        df_samples = pd.read_csv(sample_file_abs, index_col='index')

        predictions = []

        # Iterate over samples
        for index, row in df_samples.iterrows():
            recording_path = os.path.join(data_path, row['recording'])

            video1, video2, video3, video4, audio = data_loader.get_data_generators(recording_path, row['start_time'], row['end_time'])

            predictions.append([index] + participant_next_speaker.predict(video1, video2, video3, video4, audio))

        # Write predictions
        df_out = pd.DataFrame(predictions, columns=['index', 'prediction_1', 'prediction_2', 'prediction_3', 'prediction_4'])
        df_out.to_csv('output/prediction_next_speaker.csv', index=False)

        print('Successfully calculated next speaker predictions.')
    except Exception as e:
        error_info = sys.exc_info()[-1]
        error_file = os.path.split(error_info.tb_frame.f_code.co_filename)[1]
        error_line = error_info.tb_lineno
        print('Failure! {}: {} in file {} line {}'.format(type(e).__name__, e, error_file, error_line))


if __name__ == '__main__':
    predict('/input', os.environ['MULTIMEDIATE_SAMPLE_FILE'])
