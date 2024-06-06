from groq import Groq

with open('API-key-grok.json', 'r') as r:
    key = r.read()

with open("Lecture_transcript.txt", 'rb') as f:
    text = f.read()
    
Client = Groq(api_key= key)

complete_chat = Client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a diligent student taking study notes during a class lecture. Your task is to fully parse this transcript of the class lecture and generate a comprehensive and detailed study note. Your notes should be structured, information-rich, and focused on the concepts and key points discussed in the lecture. Do not include any mentions of individuals, their questions, interactions, or any administrative details. Aim for around 1000 words of content that captures the essence of the lectures subject matter."

        },
        {
            "role": "user",
            "content": str(text)[:5000]

        },
        {
            "role": "user",
            "content": str(text)[5001:10000]

        },
        {
            "role": "user",
            "content": str(text)[10001:14000]

        }
    ],
    model="mixtral-8x7b-32768",
    temperature=0
)

print(str(text))

with open('Groq_ClassNote.md', 'w') as f:
    f.write(complete_chat.choices[0].message.content)