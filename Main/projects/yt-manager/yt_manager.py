import json

video_file = "youtube.txt"


def load_videos():
    try:
        with open(video_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(video_file, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video}")


def add_video(videos):
    name = input("Enter video name: ")
    time = input("enter completion time: ")
    if not name:
        print("Name cannot be empty.")
        return
    if not time:
        print("Time cannot be empty.")
        return
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video}")
    choice = int(input("Enter the video no you want to edit: "))
    name = input("Updated name: ")
    time = input("Updated time: ")
    if not name:
        print("Name cannot be empty.")
        return
    if not time:
        print("Time cannot be empty.")
        return
    videos[choice - 1] = {"name": name, "time": time}
    save_data_helper(videos)


def remove_video(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video}")
    choice = int(input("Enter the video no you want to remove: "))
    del videos[choice-1]
    save_data_helper(videos)

while True:
    videos = load_videos()

    print("\n Youtube Manager ")
    print("1. List all Youtube videos")
    print("2. Add a video")
    print("3. Update a video")
    print("4. Remove a video")
    print("5. Exit app")

    print(videos)
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            list_all_videos(videos)
        case "2":
            add_video(videos)
        case "3":
            update_video(videos)
        case "4":
            remove_video(videos)
        case "5":
            print("Exited!")
            break
        case _:
            print("Invalid choice.")
