from google.cloud import speech

def google_S2T(file_path, fs):
    client = speech.SpeechClient.from_service_account_file("API-key.json")

    with open(file_path, "rb") as f:
        audio_file = f.read()

    audio_data = speech.RecognitionAudio(content = audio_file)

    config = speech.RecognitionConfig(
        sample_rate_hertz = fs,
        enable_automatic_punctuation = True,
        language_code = 'en-US'
    )

    response = client.recognize(
        config=config,
        audio=audio_data
    )

    # print('-' * 80)
    # print("Google Speech to Text API time billed", response.total_billed_time)
    # print('-' * 80)

    ttranscript = ""
    for each in response.results:
        ttranscript += each.alternatives[0].transcript

    return ttranscript