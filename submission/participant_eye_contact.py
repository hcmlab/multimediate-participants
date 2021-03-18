import random
random.seed(42)


def predict(video_generators, audio_generator, subject):
    """
    Predicts eye contact. Must be implemented by challenge participants.

    :param video_generators: List of 4 generators for video frames from each camera
    :param audio_generator: Generator for audio samples from microphone
    :param subject: Subject for which eye contact should be predicted (e.g., "subjectPos1")
    :return: List with prediction (0 = no eye contact, 1 = eye contact with subject 1, 2 = eye contact with subject 2, etc.)
    """
    prediction = [random.randint(0, 4)]

    # TODO: implement prediction method
    # video_frame_subject = next(video_generators[int(subject[-1]) - 1])
    # audio_value = next(audio_generator)

    return prediction
