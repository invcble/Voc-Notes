import whisper
import os
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time


# Audio sample rate
fs = 44100
seconds = 3

global audio_queue
audio_queue = []

def audio_callback(indata, frames, time, status):
    audio_queue.append(indata.copy())

stream = sd.InputStream(callback=audio_callback, samplerate=fs, channels=1)

while True:
    command = input("Recording start/stop: ").lower()
    if command == 'start':
        stream.start()
        print("Recording started.")
    elif command == 'stop':
        if stream.active:
            stream.stop()
            stream.close()
            print("Recording stopped.")
            break
        else:
            print("No active Recording.")
    else:
        time.sleep(1)


audio_queue = np.concatenate(audio_queue, axis=0)
# Normalize audio to [-1, 1] and scale to 16 bit integer
recorded_audio = np.int16(audio_queue / np.max(np.abs(audio_queue)) * 32767)
write("recording.wav",  fs, recorded_audio)



model = whisper.load_model("whisper_models\\small.en.pt")
result = model.transcribe("recording.wav")
print(result["text"])



# for each in ["audio.srt", "audio.txt", "audio.tsv", "audio.vtt"]:
#     os.remove(each)