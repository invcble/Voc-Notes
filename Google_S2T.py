from google.cloud import speech
from pydub import AudioSegment

def google_S2T(file_path):
    audio = AudioSegment.from_mp3(file_path)
    client = speech.SpeechClient.from_service_account_file("API-key.json")

    with open(file_path, "rb") as f:
        audio_file = f.read()

    audio_data = speech.RecognitionAudio(content = audio_file)

    config = speech.RecognitionConfig(
        sample_rate_hertz = audio.frame_rate,
        enable_automatic_punctuation = True,
        language_code = 'en-US'
    )

    response = client.recognize(
        config=config,
        audio=audio_data
    )

    ttranscript = ""
    for each in response.results:
        ttranscript += each.alternatives[0].transcript

    return ttranscript

# model = whisper.load_model("whisper_models\\small.en.pt")
# result = model.transcribe("recording.wav")
# print(result["text"])