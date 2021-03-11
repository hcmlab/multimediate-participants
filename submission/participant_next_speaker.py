import random
random.seed(42)


def predict(video_generators, audio_generators):
    """
    Predicts the next speaker. Must be implemented by challenge participants.

    :param video_generators: List of 4 generators for video frames from each camera
    :param audio_generators: List of 4 generators for audio samples from each microphone
    :return: List of predictions for each speaker (0 = not speaking, 1 = speaking)
    """
    prediction = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]

    # TODO: implement prediction method
    # video_frame = next(video_generators[0])
    # audio_value = next(audio_generators[0])

    return prediction
