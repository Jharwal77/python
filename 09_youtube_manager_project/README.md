# 🎥 YouTube Video Manager (Python)

A simple command-line application built using Python to manage a list of YouTube videos. This project helped me practice Python fundamentals such as functions, file handling, JSON, loops, conditions, exception handling, and match-case statements.

---

## 📚 Concepts Practiced

- Functions
- Lists
- Dictionaries
- JSON Module
- File Handling
- Exception Handling (`try-except`)
- User Input
- Loops (`while`)
- Conditional Statements (`if-else`)
- `enumerate()`
- String Formatting (f-strings)
- Pattern Matching (`match-case`)

---

## 📂 Project Structure

```
youtube-manager/
│
├── youtube.py          # Main application
├── youtube.txt         # Stores video data in JSON format
└── README.md
```

---

## 🚀 Features

### 1. List All Videos
Displays every saved video in a formatted table.

Example:

```
No   Video Name               Duration (Hours)
--------------------------------------------------
1    Python Basics            1.50
2    Django Tutorial          2.25
```

---

### 2. Add Video

Allows the user to add a new video.

Input:

```
Enter video name:
Enter video time in minutes:
```

---

### 3. Update Video

- Shows all videos
- Select video number
- Enter new details
- Saves automatically

---

### 4. Delete Video

- Shows all videos
- Select video number
- Removes selected video

---

### 5. Exit

Closes the application.

---

## 💾 Data Storage

The application stores data inside

```
youtube.txt
```

Example:

```json
[
    {
        "name": "Python Tutorial",
        "time": 120
    },
    {
        "name": "React Crash Course",
        "time": 95
    }
]
```

`time` is stored in **minutes**.

During display, it is converted into **hours**.

Example:

```python
video['time'] / 60
```

---

## 📖 Functions Explained

### load_data()

Loads data from the JSON file.

If the file does not exist, returns an empty list.

---

### list_all_videos(videos)

Prints every saved video in a clean table.

Uses:

- enumerate()
- f-strings
- formatting

---

### add_video(videos)

Adds a new video to the list and saves it.

---

### update_video_details(videos)

Updates an existing video's name and duration.

---

### delete_video(videos)

Deletes a selected video.

---

### save_data_helper(videos)

Writes all video data into the JSON file.

Uses

```python
json.dump()
```

---

### main()

Controls the complete application.

- Displays menu
- Takes user choice
- Calls corresponding function
- Repeats until Exit

---

## 🧠 Python Concepts Used

### enumerate()

Instead of writing

```python
for i in range(len(videos)):
```

we use

```python
for index, video in enumerate(videos, start=1):
```

Benefits

- Cleaner code
- Easy indexing
- More Pythonic

---

### JSON Module

Convert Python objects to JSON

```python
json.dump(data, file)
```

Read JSON into Python

```python
json.load(file)
```

---

### Exception Handling

```python
try:
    ...
except FileNotFoundError:
    return []
```

Prevents the program from crashing if the file doesn't exist.

---

### Match Case

Python 3.10 introduced

```python
match choice:
```

It works similarly to switch-case in other programming languages.

Example

```python
match choice:
    case 1:
        ...
    case 2:
        ...
```

---

### File Handling

Reading

```python
with open("youtube.txt", "r") as file:
```

Writing

```python
with open("youtube.txt", "w") as file:
```

Using `with` automatically closes the file.

---

## ▶️ How to Run

Clone the repository

```bash
git clone <repository-url>
```

Go into the project folder

```bash
cd youtube-manager
```

Run

```bash
python youtube.py
```

---

## Sample Menu

```
Youtube Manager | choose an option

1. List all youtube video
2. Add a youtube video
3. Update a youtube video details
4. Delete a youtube video
5. Exit the app
```

---

## 🎯 Learning Outcomes

After completing this project, I understood:

- How JSON stores data
- Reading and writing files
- Building menu-driven applications
- Working with lists and dictionaries
- Exception handling
- Using functions effectively
- Formatting output
- Python pattern matching (`match-case`)

---

## 🔮 Future Improvements

- Search videos
- Sort videos
- Store duration in HH:MM format
- Input validation
- Prevent duplicate videos
- Add categories
- Add upload date
- Add watch status (Completed / Pending)
- Export data to CSV

---

## 👨‍💻 Author

**Rahul Meena**

Learning Python one project at a time 🚀