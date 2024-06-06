from groq import Groq
import time

with open('API-key-grok.json', 'r') as r:
    key = r.read()

with open('Groq_ClassNote2.md', 'r') as f:
    summary = str(f.read())
    
Client = Groq(api_key= key)


    # assistant_content = ''

complete_chat = Client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Can you please make the following a bit more cohorent and consistant, use markdown format"

            },
            {
                "role": "user",
                "content": summary

            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0
    )

    # generated_response.append(complete_chat.choices[0].message.content)

# print(generated_response)

with open('Groq_ClassNote3.md', 'w') as f:
    f.write(complete_chat.choices[0].message.content)