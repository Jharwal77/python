from bson import ObjectId
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("MONGODB_URL")

if not api_key:
    print("Error: MONGODB_URL not found in .env file.")
    exit()

try:
    client = MongoClient(api_key, tlsAllowInvalidCertificates=True)
    client.admin.command("ping")
    print("✅ Connected to MongoDB Successfully.\n")
except Exception as e:
    print("❌ MongoDB Connection Failed!")
    print(e)
    exit()

db = client["ytmanager_python"]
list_of_video_collection = db["videos"]

def list_all_videos():
    videos = list(list_of_video_collection.find().sort("_id", -1))

    if not videos:
        print("\nNo videos found.")
        return

    print("\n========== VIDEO LIST ==========")

    for index, video in enumerate(videos, start=1):
        print(f"""
Video #{index}
----------------------------------------
ID   : {video['_id']}
Name : {video['name']}
Time : {video['time']}
----------------------------------------
""")


def add_video(name, time):
    if not name.strip():
        print("❌ Video name cannot be empty.")
        return

    if not time.strip():
        print("❌ Video duration cannot be empty.")
        return

    result = list_of_video_collection.insert_one(
        {
            "name": name.strip(),
            "time": time.strip()
        }
    )

    print("\n✅ Video Added Successfully!")
    print(f"Inserted ID: {result.inserted_id}")

def update_video(video_id, new_name, new_time):
    try:

        result = list_of_video_collection.update_one(
            {"_id": ObjectId(video_id)},
            {
                "$set": {
                    "name": new_name.strip(),
                    "time": new_time.strip()
                }
            }
        )

        if result.matched_count == 0:
            print("❌ Video not found.")
            return

        if result.modified_count:
            print("✅ Video Updated Successfully.")
        else:
            print("No changes were made.")

    except InvalidId:
        print("❌ Invalid Video ID.")

    except Exception as e: 
        print(e)

def delete_video(video_id):
    try:

        confirm = input("Are you sure? (y/n): ").lower()

        if confirm != "y":
            print("Delete cancelled.")
            return

        result = list_of_video_collection.delete_one(
            {"_id": ObjectId(video_id)}
        )

        if result.deleted_count:
            print("✅ Video Deleted Successfully.")
        else:
            print("❌ Video not found.")

    except InvalidId:
        print("Invalid Video ID.")

    except Exception as e:
        print(e)

def main():
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube video ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Enter Your choice: ").strip()

        match choice:
            case '1':
                list_all_videos()
            
            case '2':
                name = input("Enter the new video name: ")
                time = input("Enter the new video time in minutes: ")
                add_video(name, time)

            case '3':
                video_id = (input("Enter the video Id to want update: "))
                name = input("Enter the new video name: ")
                time = input("Enter the new video time in minutes: ")
                update_video(video_id, name, time)

            case '4':
                video_id = input("Enter the video Id to want delete: ")
                delete_video(video_id)

            case '5':
                print("\nThank you for using YouTube Manager.")
                client.close()
                print("MongoDB Connection Closed.")
                break

            case _:
                print("Invalid choice , PLease choice between 1-5")
        

if __name__ == "__main__":
    main()
