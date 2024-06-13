import numpy as np
import sounddevice as sd
from pydub import AudioSegment
import time

from Google_S2T import google_S2T
from Audio_chop import audio_chop
from Groq_LLM import lecture_to_note


################## Handle audio file ##################

global audio_queue
global audio_path
audio_queue = []
audio_path = ''

def audio_callback(indata, frames, time, status):
    audio_queue.append(indata.copy())

stream = sd.InputStream(callback=audio_callback, samplerate=44100, channels=1)

def start_recording():
    if not stream.active:
        print("recording started")
        stream.start()

def stop_recording():
    global audio_queue
    global audio_path

    if stream.active:
        print("recording stopped")
        stream.stop()
        stream.close()

        # audio_queue = np.concatenate(audio_queue, axis=0)
        # ###### Normalize audio to [-1, 1] and scale to 16 bit integer
        # recorded_audio_data = np.int16(audio_queue / np.max(np.abs(audio_queue)) * 32767)

        # audio_segment = AudioSegment(
        #     recorded_audio_data.tobytes(), 
        #     frame_rate=44100,
        #     sample_width=recorded_audio_data.dtype.itemsize,
        #     channels=1
        # )

        # audio_path = "recorded_audio.mp3"
        # audio_segment.export(audio_path)

        generate_note()


def upload_recording(path):
    global audio_path

    audio_path = path.replace("\\", "\\\\")
    print("you uploaded ", audio_path)

    generate_note()

def generate_note():
    global audio_path

    ################## Split audio file ##################
    print("Splitting Audio to chunks...")
    chunk_list = audio_chop(audio_path)


    ################## Speech to text ##################
    print("Converting Speech to text...")
    lecture_text = ''
    for each_path in chunk_list:
        lecture_text += google_S2T(each_path) + ' '

    with open("lecture_transcript.txt", 'w') as f:
        f.write(lecture_text)


    ################## LLM note conversion ##################
    print("Sending data to LLM to generate Note...")
    lecture_to_note("lecture_transcript.txt")