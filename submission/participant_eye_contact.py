import random
random.seed(42)


def predict(video1_generator, video2_generator, video3_generator, video4_generator, audio_generator, subject):
    """
    Predicts eye contact. Must be implemented by challenge participants.

    :param video1_generator: Generator for video frames showing subject 1
    :param video2_generator: Generator for video frames showing subject 2
    :param video3_generator: Generator for video frames showing subject 3
    :param video4_generator: Generator for video frames showing subject 4
    :param audio_generator: Generator for audio samples
    :param subject: Subject for which eye contact should be predicted
    :return: List with prediction (0 = no eye contact, 1 = eye contact with subject 1, 2 = eye contact with subject 2, etc.)
    """
    prediction = [random.randint(0, 4)]

    # TODO: implement method
    # frame = next(video1_generator)
    # audio_value = next(audio_generator)

    # for frame in video1_generator:
    return prediction
