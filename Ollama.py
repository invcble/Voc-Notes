import ollama

with open("Lecture_transcript.txt", 'rb') as f:
    text = f.read()

instruction = 'You are a diligent student taking study notes during a class lecture. Your task is to fully parse this transcript of the class lecture and generate a comprehensive and detailed study note. Your notes should be structured, information-rich, and focused on the concepts and key points discussed in the lecture. Do not include any mentions of individuals, their questions, interactions, or any administrative details. Aim for around 1000 words of content that captures the essence of the lectures subject matter.\n'

content = ollama.generate(model='llama3', prompt=instruction + str(text))['response']

with open("MOD_Generated_Class_Note.md", 'w') as f:
    f.write(content)