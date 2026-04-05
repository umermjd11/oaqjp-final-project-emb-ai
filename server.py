"""Emotion Detection Flask Application"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """Detect emotion from text provided in query parameter."""
    text = request.args.get('textToAnalyze', '')
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    response = (f"For the given statement, the system response is 'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
                f"and 'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}.")



    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
