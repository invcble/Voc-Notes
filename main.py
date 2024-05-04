import whisper
import os

model = whisper.load_model("whisper_models\\small.en.pt")
result = model.transcribe("audio.mp3")
print(result["text"])

os.remove("audio.srt")
os.remove("audio.txt")
os.remove("audio.tsv")
os.remove("audio.vtt")