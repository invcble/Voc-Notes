import streamlit as st
from Engine import start_recording, stop_recording

st.title("Welcome to Voc-Notes!")
st.write("Hi student!")

# st.write("Imon you are from ", answer)

st.write("What do you want to do?")
click_record = st.button("Record Audio")
click_upload = st.button("Upload Audio")
# st.download_button()

if "recording" not in st.session_state:
    st.session_state.record = False

if "upload" not in st.session_state:
    st.session_state.upload = False

if click_record:
    st.session_state.record = True
    st.session_state.upload = False
    click_start = st.button("Start Recording.")
    click_stop = st.button("Stop Recording.")
    # start_recording()

# if click_stop:
#     st.session_state.record = False
#     stop_recording()

# if st.session_state.record:
#     st.write("Recording started!")

# if click_upload:
#     answer = st.text_input("Paste the audio path below.")
#     if answer:
#         st.write("You pasted", answer)

# import time
# while True:
#     command = input("Recording start/stop: ").lower()
#     if command == 'start':
#         print("Recording started.")
#     elif command == 'stop':
#         print("Recording stopped.")
#         break
#     else:
#         time.sleep(1)
# import numpy as np
# import sounddevice as sd
# from pydub import AudioSegment
# import time


# ################## Handle audio file ##################
# choice = input("Audio upload/record: ").lower()

# if choice == "record":
#     global audio_queue
#     audio_queue = []

#     def audio_callback(indata, frames, time, status):
#         audio_queue.append(indata.copy())

#     stream = sd.InputStream(callback=audio_callback, samplerate=44100, channels=1)

#     while True:
#         command = input("Recording start/stop: ").lower()
#         if command == 'start':
#             stream.start()
#             print("Recording started.")
#         elif command == 'stop':
#             if stream.active:
#                 stream.stop()
#                 stream.close()
#                 print("Recording stopped.")
#                 break
#             else:
#                 print("No active Recording.")
#         else:
#             time.sleep(1)


#     audio_queue = np.concatenate(audio_queue, axis=0)
#     ###### Normalize audio to [-1, 1] and scale to 16 bit integer
#     recorded_audio_data = np.int16(audio_queue / np.max(np.abs(audio_queue)) * 32767)

#     audio_segment = AudioSegment(
#         recorded_audio_data.tobytes(), 
#         frame_rate=44100,
#         sample_width=recorded_audio_data.dtype.itemsize,
#         channels=1
#     )

#     audio_path = "recorded_audio.mp3"
#     audio_segment.export(audio_path)

# elif choice == "upload":
#     audio_path = input("Paste the path location: ").replace("\\", "\\\\")
# else:
#     print("Input not recognised!")