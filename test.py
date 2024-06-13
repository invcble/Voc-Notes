import Mongo_connect

# Mongo_connect.upload_note("CS615_Groq_ClassNote.md", "dummy note")

print(Mongo_connect.list_notes())

print(Mongo_connect.pull_document('genNote_dummy note'))