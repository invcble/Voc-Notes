from google.cloud import speech

client = speech.SpeechClient.from_service_account_file("API-key.json")

with open("recording.wav", "rb") as f:
    audio_file = f.read()

audio_data = speech.RecognitionAudio(content = audio_file)


config = speech.RecognitionConfig(
    sample_rate_hertz = 44100,
    enable_automatic_punctuation = True,
    language_code = 'en-US'
)

response = client.recognize(
    config=config,
    audio=audio_data
)

print(response)
for each in response.results:
    print(each)
    print('-' * 40)