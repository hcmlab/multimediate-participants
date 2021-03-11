import random
random.seed(42)


def predict(video_generators, audio_generators, subject):
    """
    Predicts eye contact. Must be implemented by challenge participants.

    :param video_generators: List of 4 generators for video frames from each camera
    :param audio_generators: List of 4 generators for audio samples from each microphone
    :param subject: Subject for which eye contact should be predicted
    :return: List with prediction (0 = no eye contact, 1 = eye contact with subject 1, 2 = eye contact with subject 2, etc.)
    """
    prediction = [random.randint(0, 4)]

    # TODO: implement prediction method
    # video_frame_cam1 = next(video_generators[0])
    # audio_value_mic1 = next(audio_generators[0])

    return prediction
