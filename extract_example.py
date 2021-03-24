import os
from submission.utils import data_loader
import pandas as pd

# Set path to dataset
dataset_path = r'/path/to/dataset'

# Set path to sample list
sample_list_path = os.path.join(dataset_path, 'sample_lists', 'train_eye_contact.csv')

# Load sample list
df_samples = pd.read_csv(sample_list_path, index_col='index')

# Iterate over entries
for index, row in df_samples.iterrows():
    # Get path to recording
    recording_path = os.path.join(dataset_path, 'data', row['recording'])

    # Get sample data generators
    video_generators, audio_generator = data_loader.get_data_generators(recording_path, row['start_time'], row['end_time'])

    # Get label for eye contact task
    label = row['label']

    # Get label for next speaker task
    # label = [row['label_1'], row['label_2'], row['label_3'], row['label_4']]

    # TODO Use video_generators, audio_generator and label
    # for frame in video_generators[1]:
    #     pass