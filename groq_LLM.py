from groq import Groq
import time

with open('API-key-grok.json', 'r') as r:
    key = r.read()

with open("Lecture_transcript.txt", 'rb') as f:
    lecture = str(f.read())
    
Client = Groq(api_key= key)

max_token_length = 5000
split_lecture = [lecture[i : i + max_token_length] for i in range(0, len(lecture), max_token_length)]
generated_response = []

for i in range(0, len(split_lecture)-1, 2):
    # assistant_content = ''

    complete_chat = Client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are student at this class, from this lecture make 1000 words class-note for yourself for the exam"

            },
            {
                "role": "user",
                "content": split_lecture[i]

            },
            {
                "role": "user",
                "content": split_lecture[i+1]

            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0
    )

    # assistant_content = complete_chat.choices[0].message.content
    generated_response.append(complete_chat.choices[0].message.content)
    # time.sleep(1)

# print(generated_response)

with open('Groq_ClassNote2.md', 'w') as f:
    for each in generated_response:
        f.write('\n\n\n\n'+each)

# with open('Groq_ClassNote2.md', 'w') as f:
#     f.write(assistant_content)