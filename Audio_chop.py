from pydub import AudioSegment
from pydub.utils import make_chunks
import os, shutil

def audio_chop(audio_path):
    shutil.rmtree("temp_audio_folder")
    os.makedirs("temp_audio_folder")

    audio = AudioSegment.from_mp3(audio_path)
    chunk_size = 50000

    chunks = make_chunks(audio, chunk_size)

    chunk_list = []
    for i in range(len(chunks)):
        chunks[i].export(f"temp_audio_folder/record_chunk_{i}.mp3")
        chunk_list.append(f"temp_audio_folder/record_chunk_{i}.mp3")
    
    return chunk_list