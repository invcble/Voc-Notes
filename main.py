import numpy as np
import sounddevice as sd
from pydub import AudioSegment
import time

from Google_S2T import google_S2T
from Audio_chop import audio_chop
from Groq_LLM import lecture_to_note


################## Handle audio file ##################
choice = input("Audio upload/record: ").lower()

if choice == "record":
    global audio_queue
    audio_queue = []

    def audio_callback(indata, frames, time, status):
        audio_queue.append(indata.copy())

    stream = sd.InputStream(callback=audio_callback, samplerate=44100, channels=1)

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
    ###### Normalize audio to [-1, 1] and scale to 16 bit integer
    recorded_audio_data = np.int16(audio_queue / np.max(np.abs(audio_queue)) * 32767)

    audio_segment = AudioSegment(
        recorded_audio_data.tobytes(), 
        frame_rate=44100,
        sample_width=recorded_audio_data.dtype.itemsize,
        channels=1
    )

    audio_path = "recorded_audio.mp3"
    audio_segment.export(audio_path)

elif choice == "upload":
    audio_path = input("Paste the path location: ").replace("\\", "\\\\")
else:
    print("Input not recognised!")


################## Split audio file ##################
chunk_list = audio_chop(audio_path)


################## Speech to text ##################
lecture_text = ''
for each_path in chunk_list:
    lecture_text += google_S2T(each_path) + ' '

with open("lecture_transcript.txt", 'w') as f:
    f.write(lecture_text)


################## LLM note conversion ##################
lecture_to_note("lecture_transcript.txt")#