from groq import Groq

with open('API-key-grok.json', 'r') as r:
    key = r.read()

with open("Lecture_transcript.txt", 'r') as f:
    lecture = str(f.read())
    
Client = Groq(api_key= key)

max_token_length = 10000
split_lecture = [lecture[i : i + max_token_length] for i in range(0, len(lecture), max_token_length)]
generated_response = ""

for chunk in split_lecture:
    print("check") #########
    note_chunks = Client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are student at this class, from this lecture make 1000 words class-note for yourself for the exam"

            },
            {
                "role": "user",
                "content": chunk
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0
    )

    generated_response += '\n\n\n'+ note_chunks.choices[0].message.content


print("Generated chunk sizes", len(generated_response))

final_note = Client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Can you please make the following a bit more cohorent and consistent, organize the details, remove duplicates, use markdown format"

            },
            {
                "role": "user",
                "content": generated_response

            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0
    )


print("Generated final size", len(final_note.choices[0].message.content))

with open('Groq_ClassNote.md', 'w') as f:
    f.write(final_note.choices[0].message.content)