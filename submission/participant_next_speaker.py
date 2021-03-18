import random
random.seed(42)


def predict(video_generators, audio_generator):
    """
    Predicts the next speaker. Must be implemented by challenge participants.

    :param video_generators: List of 4 generators for video frames from each camera
    :param audio_generator: Generator for audio samples from microphone
    :return: List of predictions for each speaker (0 = not speaking, 1 = speaking)
    """
    prediction = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]

    # TODO: implement prediction method
    # video_frame_cam1 = next(video_generators[0])
    # audio_value = next(audio_generator)

    return prediction
