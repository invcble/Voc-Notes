import whisper
import os
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

from Google_S2T import google_S2T


fs = 44100          # Audio sample rate
chunk_size = fs * 50        #50 seconds

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
recorded_audio_data = np.int16(audio_queue / np.max(np.abs(audio_queue)) * 32767)
record_chunks = [recorded_audio_data[i : i + chunk_size] for i in range(0, len(recorded_audio_data), chunk_size)]

lecture_text = ''

for i in range(len(record_chunks)):
    write(f"temp_audio_folder/record_chunk_{i}.wav", fs, record_chunks[i])

    text = google_S2T(f"temp_audio_folder/record_chunk_{i}.wav", fs)
    lecture_text += text + ' '

print('-' * 80)
print("Google Speech to Text billing seconds", i * 50)
print('-' * 80)

with open("new_lecture_transcript.txt", 'w') as f:
    f.write(lecture_text)
# model = whisper.load_model("whisper_models\\small.en.pt")
# result = model.transcribe("recording.wav")
# print(result["text"])