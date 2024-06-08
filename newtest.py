from pydub import AudioSegment
from pydub.utils import make_chunks
import os

audio = AudioSegment.from_mp3("sample_audio.mp3")
chunk_size = 5000

chunks = make_chunks(audio, chunk_size)

for i in range(len(chunks)):
    chunks[i].export(f"temp_audio_folder/record_chunk_{i}.mp3")