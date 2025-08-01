"""
Flask server for NLP Emotion Detection App.
Provides a web interface for analyzing emotional content in text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the home page with the input form.
    """
    return render_template("index.html")

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Handle POST request with text input, return emotion analysis results.
    """
    data = request.get_json()
    text_to_analyze = data.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(debug=True)
