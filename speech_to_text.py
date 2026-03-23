import whisper

model = whisper.load_model("base")

def convert_audio_to_text(file_path):

    result = model.transcribe(file_path)

    return result["text"]