from flask import Flask, jsonify, request
from flask_cors import CORS
import whisper
from io import BytesIO, StringIO
import os
import tempfile

app = Flask(__name__)
CORS(app)

model = whisper.load_model("base")

def transcribe(audio_data):
    audio_file = BytesIO(audio_data.read())

    # Get the current script directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Create a temporary file with a .wav extension in the same directory
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False, dir=script_dir) as temp_file:
        temp_file.write(audio_file.read())
        temp_file_path = temp_file.name

    try:
        # Load audio from the temporary file
        print(temp_file_path)
        audio = whisper.load_audio(temp_file_path)

        mel = whisper.log_mel_spectrogram(audio).to(model.device)

        # _, probs = model.detect_language(mel)
        # detected_language = max(probs, key=probs.get)

        # options = whisper.DecodingOptions()
        options = {
                    "language": "en", # input language, if omitted is auto detected
                    "task": "transcribe" # or "transcribe" if you just want transcription
                    }
        result = whisper.transcribe(model, mel, **options)
        # result = whisper.decode(model, mel, options)
        print(result.text)

        # return {"text": result.text, "detected_language": detected_language}
        return {"text": result.text}
    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")
    #     # Handle the error as needed, e.g., log it, return an error response, etc.
    #     # return {"error": f"An error occurred: {str(e)}"}
    
    finally:
        # Clean up: delete the temporary file
        os.remove(temp_file.name)

@app.route('/transcribe', methods=['POST'])
def transcribe_endpoint():
    if 'audio' not in request.files:
        return jsonify({"error": "Audio file not provided"}), 400
    
    audio_file = request.files['audio']
    result = transcribe(audio_file)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
