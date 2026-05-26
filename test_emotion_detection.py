from EmotionDetection import emotion_detector


def test_emotion_detection():
    """
    Test emotion detection outputs.
    """

    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected in test_cases.items():

        response = emotion_detector(statement)

        dominant = response["dominant_emotion"]

        print(
            f"Input: {statement}"
        )

        print(
            f"Expected: {expected}"
        )

        print(
            f"Detected: {dominant}"
        )

        print()

        assert dominant == expected


test_emotion_detection()

print(
    "All tests passed"
)

