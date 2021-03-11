import random
random.seed(42)


def predict(video1_generator, video2_generator, video3_generator, video4_generator, audio_generator):
    """
    Predicts the next speaker. Must be implemented by challenge participants.

    :param video1_generator: Generator for video frames showing subject 1
    :param video2_generator: Generator for video frames showing subject 2
    :param video3_generator: Generator for video frames showing subject 3
    :param video4_generator: Generator for video frames showing subject 4
    :param audio_generator: Generator for audio samples
    :return: List of predictions for each speaker (0 = not speaking, 1 = speaking)
    """
    prediction = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]

    # TODO: implement method
    # frame = next(video1_generator)
    # audio_value = next(audio_generator)

    # for frame in video1_generator:
    return prediction
