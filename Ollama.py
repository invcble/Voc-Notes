import ollama

with open("Lecture_transcript.txt", 'rb') as f:
    text = f.read()

instruction = 'Fully parse this transcript of a class lecture of Software Architecture and write a 1000 words note for it as if you were in the class as a student, include details from the whole lecture, DO NOT SKIP ANYTHING ON THE TRANSCRIPT, omit student conversations \n'

content = ollama.generate(model='llama3', prompt=instruction + str(text))['response']

with open("Generated_Class_Note.md", 'w') as f:
    f.write(content)