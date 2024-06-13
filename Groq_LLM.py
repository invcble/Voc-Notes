from groq import Groq

def lecture_to_note(lecture_path):
    with open('API-key-grok.json', 'r') as r:
        key = r.read()

    with open(lecture_path, 'r') as f:
        lecture = str(f.read())

    if len(lecture) < 5001:
        lecture += ' ' * (5001 - len(lecture))

    Client = Groq(api_key= key)

    max_token_length = 5000
    split_lecture = [lecture[i : i + max_token_length] for i in range(0, len(lecture), max_token_length)]
    generated_response = ""

    print("Generating response using mixtral..")
    for i in range(0, len(split_lecture)-1, 2):

        # print('check') #########
        note_chunks = Client.chat.completions.create(
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

        generated_response += '\n\n\n'+ note_chunks.choices[0].message.content


    print("Generated chunk sizes", len(generated_response))

    print("Generating response using llama3..")
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
            model="llama3-70b-8192",
            temperature=0
        )


    print("Generated final size", len(final_note.choices[0].message.content))

    return final_note.choices[0].message.content