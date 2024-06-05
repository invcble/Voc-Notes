
import logging
import time
from deepgram import (
    SpeakOptions,
    DeepgramClient,
    DeepgramClientOptions,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
)
from groq import Groq


import asyncio
import os
from dotenv import load_dotenv
import pygame

load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")




class TranscriptCollector:
    def __init__(self):
        self.reset()

    def reset(self):
        self.transcript_parts = []

    def add_part(self, part):
        self.transcript_parts.append(part)

    def get_full_transcript(self):
        return ' '.join(self.transcript_parts)

transcript_collector = TranscriptCollector()

async def get_transcript():
    transcription_complete = asyncio.Event()
    try:
        config = DeepgramClientOptions(options={"keepalive": "true"})
        deepgram: DeepgramClient = DeepgramClient(DEEPGRAM_API_KEY, config)

        dg_connection = deepgram.listen.asynclive.v("1")
        print("Listening...")
        async def on_message(self, result, **kwargs):
            # print (result)
            sentence = result.channel.alternatives[0].transcript
            if not result.speech_final:
                transcript_collector.add_part(sentence)
            else:
                # This is the final part of the current sentence
                transcript_collector.add_part(sentence)
                full_sentence = transcript_collector.get_full_transcript()
                if len(full_sentence.strip()) > 0:
                    full_sentence = full_sentence.strip()
                    print(f"Human: {full_sentence}")
                    messages.append({"role": "user", "content": full_sentence})
                    print("sent to model")
                    # send_to_model(messages)
                    transcript_collector.reset()
                    transcription_complete.set()

        dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)

        options = LiveOptions(
            model="nova-2",
            punctuate=True,
            language="en-US",
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            endpointing=True
        )

        await dg_connection.start(options)

        # Open a microphone stream on the default input device
        microphone = Microphone(dg_connection.send)

        # start microphone
        microphone.start()

        await transcription_complete.wait()

        # Wait for the microphone to close
        microphone.finish()

        # Indicate that we've finished
        await dg_connection.finish()

    except Exception as e:
        print(f"Could not open socket: {e}")
        return

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)

def send_to_model(messages):
    # response = groq_client.chat.completions.create(
    #     model="llama3-8b-8192",
    #     messages=messages
    #     )
    while True:
        response = groq_client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=messages
        )
        if response.choices[0].message.content != "":
            break
        
    
    return response
    

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
deepgram_client = DeepgramClient(api_key=DEEPGRAM_API_KEY)

def text_to_speech(text, output_file_path):
    try:
        options = SpeakOptions(
            model="aura-luna-en",  # Change voice if needed
            encoding="linear16",
            container="wav"
        )
        SPEAK_OPTIONS = {"text": text}
        deepgram_client.speak.v("1").save(output_file_path, SPEAK_OPTIONS, options)
        print("AI : ", text)
        play_audio(output_file_path)
    except Exception as e:
        logging.error(f"Failed to convert text to speech: {e}")

def play_audio(file_path):
    try:
        pygame.mixer.init()  # Initialize pygame mixer here
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.music.stop()
        pygame.mixer.quit()  # Quit pygame mixer here
    except pygame.error as e:
        logging.error(f"Failed to play audio: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred while playing audio: {e}")

messages = []

messages.append({"role": "user", "content": '''You are a conversational assistant named Eliza.
Your response should be under 30 words.
Do not respond with any code, only conversation.
Reply with context to this conversation.'''})

class ConversationManager:
    def __init__(self):
        self.transcription_response = ""
        self.llm = None

    async def main(self):
        while True:
            await get_transcript()
            # Check for "goodbye" to exit the loop
            if "goodbye" in self.transcription_response.lower():
                break
            
            response = send_to_model(messages)
            print("-----------------------------")
            print(response.choices[0])
            text_to_speech(response.choices[0].message.content, "output.wav")
            # Reset transcription_response for the next loop iteration
            self.transcription_response = ""

if __name__ == "__main__":
    manager = ConversationManager()
    asyncio.run(manager.main())