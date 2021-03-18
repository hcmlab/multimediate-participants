import os

import cv2
import numpy as np
from pydub import AudioSegment

LAST_AUDIO_PATH = None
LAST_AUDIO_SEGMENT = None

LAST_VIDEO_PATH = [None for x in range(4)]
LAST_VIDEO_CAPTURE = [None for y in range(4)]


def get_audio_generator(recording_path, start_time, end_time):
    global LAST_AUDIO_PATH, LAST_AUDIO_SEGMENT

    audio_file = os.path.join(recording_path, "audio.wav")

    fps = 30
    sr = 44100
    additional_time = 1 / fps + 1 / sr

    # Convert seconds to milliseconds
    t1 = int(start_time * 1000)
    t2 = int((end_time + additional_time) * 1000)

    # Cache audio for other samples from same file
    if LAST_AUDIO_PATH == audio_file:
        new_audio = LAST_AUDIO_SEGMENT
    else:
        new_audio = AudioSegment.from_wav(audio_file)
        LAST_AUDIO_SEGMENT = new_audio
        LAST_AUDIO_PATH = audio_file

    new_audio = new_audio[t1:t2]

    snippet = np.array(new_audio.get_array_of_samples())

    for i in range(len(snippet)):
        yield snippet[i]

    # return np.array(new_audio.get_array_of_samples())


def get_video_generator(generator_id, recording_path, subject, start_time, end_time):
    global LAST_VIDEO_PATH, LAST_VIDEO_CAPTURE

    video_file = os.path.join(recording_path, "{}.video.avi".format(subject))

    # Cache video for other samples from same file
    if LAST_VIDEO_PATH[generator_id] == video_file:
        capture = LAST_VIDEO_CAPTURE[generator_id]
    else:
        capture = cv2.VideoCapture(video_file)
        LAST_VIDEO_PATH[generator_id] = video_file
        LAST_VIDEO_CAPTURE[generator_id] = capture

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
        ret, frame_bgr = capture.read()

        buf[fc] = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

        yield buf[fc]
        fc += 1

    # return buf


def get_data_generators(recording_path, start_time, end_time):
    video_generators = []
    audio_generator = get_audio_generator(recording_path, start_time, end_time)

    for i in range(4):
        video_generators.append(get_video_generator(i, recording_path, "subjectPos{}".format(i + 1), start_time, end_time))

    return video_generators, audio_generator
