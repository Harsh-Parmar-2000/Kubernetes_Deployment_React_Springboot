from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyse/sentiment", methods=['POST'])
def analyse_sentiment():
    try:
        data = request.get_json()
        sentence = data.get('sentence')
        if sentence is None:
            return jsonify(error="Invalid request data"), 400

        text_blob = TextBlob(sentence)
        if len(text_blob.sentences) == 0:
            return jsonify(error="No valid sentences to analyze"), 400

        polarity = text_blob.sentences[0].polarity
        return jsonify(
            sentence=sentence,
            polarity=polarity
        )
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)