from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    
     
    text=request.args.get('textToAnalyze', '')
    result = emotion_detector(text)
    result = emotion_detector(text)
    return f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

if __name__ == "__main__":
    '''This function executes the flask app and deploys it on localhost:5000 in debug mode, 
    which allows for easier troubleshooting and development. The host is set to "0.0.0.0" 
    to allow external connections.'''
    app.run(host="0.0.0.0", port=5000, debug=True)