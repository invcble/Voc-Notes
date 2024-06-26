import numpy as np
import sounddevice as sd
from pydub import AudioSegment
import os

from Google_S2T import google_S2T
from Audio_chop import audio_chop
from Groq_LLM import lecture_to_note
import Mongo_connect, Data_tableauhyper


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

def upload_recording(path):
    global audio_path

    audio_path = path.replace("\\", "\\\\")
    print("you uploaded ", audio_path)

def split_audio():
    global audio_path
    global chunk_list

    print("Splitting Audio to chunks...")
    chunk_list = audio_chop(audio_path)

def speech2text():
    global chunk_list

    print("Converting Speech to text...")
    lecture_text = ''
    for each_path in chunk_list:
        lecture_text += google_S2T(each_path) + ' '

    with open("lecture_transcript.txt", 'w') as f:
        f.write(lecture_text)

    Mongo_connect.upload_transcript("lecture_transcript.txt")

def LLM_call():
    global gen_data

    print("Sending data to LLM to generate Note...")
    gen_data = lecture_to_note("lecture_transcript.txt")

    with open('Groq_ClassNote.md', 'w') as f:
        f.write(gen_data)

    Mongo_connect.upload_note('Groq_ClassNote.md')
    return gen_data

def display_notes():
    return Mongo_connect.list_notes()

def download_note(note_name):
    content = Mongo_connect.pull_document(note_name)

    print(f"Downloading {note_name}")
    os.makedirs("Voc-Note Downloads", exist_ok=True)
    with open(f"Voc-Note Downloads/{note_name}.md", 'w') as f:
        f.write(content)

def gen_hyper():
    Data_tableauhyper.create_hyper('lecture_transcript.txt')