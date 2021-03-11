import os
from datetime import datetime

import cv2
import numpy as np
from pydub import AudioSegment


def parse_time(start, end):
    start_time = datetime.strptime(start, '%M:%S')
    end_time = datetime.strptime(end, '%M:%S')

    t1 = start_time.minute * 60 + start_time.second
    t2 = end_time.minute * 60 + end_time.second

    return t1, t2


def get_audio_generator(recording_path, start_time, end_time):
    audio_file = os.path.join(recording_path, "subjectPos.audio.wav")

    #t1, t2 = parse_time(start_time, end_time)
    fps = 30
    sr = 44100
    additional_time = 1 / fps + 1 / sr

    # Convert seconds to milliseconds
    t1 = int(start_time * 1000)
    t2 = int((end_time + additional_time) * 1000)

    new_audio = AudioSegment.from_wav(audio_file)
    new_audio = new_audio[t1:t2]

    snippet = np.array(new_audio.get_array_of_samples())

    for i in range(len(snippet)):
        yield snippet[i]

    # return np.array(new_audio.get_array_of_samples())


def get_video_generator(recording_path, subject, start_time, end_time):
    video_file = os.path.join(recording_path, "{}.video.avi".format(subject))

    #t1, t2 = parse_time(start_time, end_time)

    capture = cv2.VideoCapture(video_file)

    frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = capture.get(cv2.CAP_PROP_FPS)

    # Calculate frame numbers
    t1 = int(start_time * fps)
    t2 = int(end_time * fps)
    frame_count = t2 - t1 + 1

    buf = np.empty((frame_count, frame_height, frame_width, 3), np.dtype('uint8'))

    capture.set(cv2.CAP_PROP_POS_FRAMES, t1)

    fc = 0
    ret = True
    while fc < frame_count and ret:
        ret, buf[fc] = capture.read()
        yield buf[fc]
        fc += 1

    # return buf


def get_data_generators(recording_path, start_time, end_time):
    video1 = get_video_generator(recording_path, 1, start_time, end_time)
    video2 = get_video_generator(recording_path, 2, start_time, end_time)
    video3 = get_video_generator(recording_path, 3, start_time, end_time)
    video4 = get_video_generator(recording_path, 4, start_time, end_time)

    audio = get_audio_generator(recording_path, start_time, end_time)

    return video1, video2, video3, video4, audio
