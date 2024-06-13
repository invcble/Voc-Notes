from pymongo import MongoClient
from datetime import datetime


def get_mongo_client():
    with open("API-key-mongo.json", "r") as f:
        mongo_uri = f.read()
    return MongoClient(mongo_uri)



def upload_transcript(transcript_path):
    client = get_mongo_client()
    db = client.get_database("VOC-NOTES-FILES")
    collection = db.get_collection("processed_transcript")

    with open(transcript_path, "r") as file:
        processed_text = file.read()

    document = {
        "filename": "ptscript_" + datetime.now().strftime("%H_%M"),
        "content": processed_text
    }

    collection.insert_one(document)
    print(f"Transcipt uploaded to Database")
    client.close()



def upload_note(note_path):
    client = get_mongo_client()
    db = client.get_database("VOC-NOTES-FILES")
    collection = db.get_collection("class_notes")

    with open(note_path, "r") as file:
        note_text = file.read()

    document = {
        "filename": "genNote_" + datetime.now().strftime("time_%H:%M"),
        "content": note_text
    }

    collection.insert_one(document)
    print(f"Class note uploaded to Database")
    client.close()



def list_notes():
    client = get_mongo_client()
    db = client.get_database("VOC-NOTES-FILES")
    collection = db.get_collection("class_notes")

    documents = collection.find({}, {"_id": 0, "filename": 1})
    filenames = [doc["filename"] for doc in documents]

    client.close()
    return filenames



def pull_document(document_name):
    client = get_mongo_client()
    db = client.get_database("VOC-NOTES-FILES")
    collection = db.get_collection("class_notes")

    document = collection.find_one({"filename": document_name}, {"_id": 0, "content": 1})
    client.close()
    return document["content"] if document else None