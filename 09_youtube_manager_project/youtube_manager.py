import json

def load_data():
    try:
        with open("youtube.txt", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    print("\n")

    print(f"{'No':<5}{'Video Name':<25}{'Duration (Hours)':<15}")
    print("-" * 50)

    for index, video in enumerate(videos, start=1):
        print(f"{index:<5}{video['name']:<25}{video['time']/60:<15.2f}")
    
    print("\n")
    print("*" * 70)
    print("\n")


def add_video(videos):
    name = input("Enter video name: ")
    time = int(input("Enter video time in minutes: "))
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video_details(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to want update: "))

    if 1<= index <= len(videos):
        name = input("Enter the new video name: ")
        time = int(input("Enter the new video time in minutes: "))
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)

    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be delete: "))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)

    else:
        print("Invalid index selected")

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube video ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = int(input("Enter Your choice: "))

        match choice:
            case 1:
                list_all_videos(videos)
            
            case 2:
                add_video(videos)

            case 3:
                update_video_details(videos)

            case 4:
                delete_video(videos)

            case 5:
                break

            case _:
                print("Invalid choice , PLease choice between 1-5")
        


if __name__ == "__main__":
    main()
