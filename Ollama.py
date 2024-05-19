import ollama

with open("Lecture_transcript.txt", 'rb') as f:
    text = f.read()

instruction = 'Parse this transcript of a class lecture of Software Architecture and write a 500 words note for it as if you were in the class as a student \n'

content = ollama.generate(model='llama3', prompt=instruction + str(text))['response']

with open("Generated_Class_Note.md", 'w') as f:
    f.write(content)