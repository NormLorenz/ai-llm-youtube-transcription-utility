from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request, render_template
from app import utilities
from config import Config

import gradio as gr

app = Flask(__name__)
app.config.from_object(Config)

# test url = 'https://www.youtube.com/watch?v=btJpw6uaZ4g&list=WL&index=12'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetch', methods=['POST'])
def ask():
    url = request.form['url']
    try:
        transcript = utilities.get_transcript(url)
        return render_template('index.html', transcript=transcript)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', error=error_message)


if __name__ == '__main__':
    app.run(debug=True)


# Do you have suggestions how I can improve this code?
