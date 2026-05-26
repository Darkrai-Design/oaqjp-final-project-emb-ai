from flask import Flask
from flask import render_template
from flask import request

from EmotionDetection import emotion_detector

app = Flask(
    "Emotion Detector"
)


@app.route("/")
def render_index_page():
    """
    Render home page.
    """
    return render_template(
        'index.html'
    )


@app.route("/emotionDetector")
def emotion_detection():

    text_to_analyze = request.args.get(
        'textToAnalyze'
    )

    response = emotion_detector(
        text_to_analyze
    )

    formatted_response = (
        "For the given statement, "
        "the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} "
        f"and 'sadness': "
        f"{response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )

