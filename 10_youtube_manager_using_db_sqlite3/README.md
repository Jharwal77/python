# 🎥 YouTube Video Manager (SQLite Database)

A simple command-line application built with Python and SQLite that allows users to manage a collection of YouTube videos. This project demonstrates how to perform CRUD (Create, Read, Update, Delete) operations using a relational database instead of JSON files.

---

# 📚 Concepts Practiced

* Python Functions
* SQLite Database
* SQL Queries
* CRUD Operations
* Database Connection
* Cursor Object
* Transactions (`commit()`)
* User Input
* Loops
* Conditional Statements
* Pattern Matching (`match-case`)

---

# 🛠 Technologies Used

* Python 3
* SQLite3 (Built-in Python Module)

---

# 📂 Project Structure

```
youtube-manager-sqlite/
│
├── youtube.py              # Main application
├── youtube_videos.db       # SQLite database (created automatically)
└── README.md
```

---

# 🚀 Features

### 1. List All Videos

Displays all videos stored in the SQLite database.

Example:

```
(1, 'Python Basics', '120')
(2, 'React Crash Course', '95')
```

---

### 2. Add Video

Insert a new video into the database.

Input

```
Video Name
Video Duration (minutes)
```

---

### 3. Update Video

Update an existing video's information using its ID.

Example

```
Video ID: 2
New Name: Django Tutorial
New Time: 150
```

---

### 4. Delete Video

Delete a video by its database ID.

---

### 5. Exit

Closes the application and database connection.

---

# 🗄 Database

The application automatically creates the database

```
youtube_videos.db
```

and creates the table

```sql
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
);
```

---

# 📖 SQL Operations Used

## Create Table

```sql
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
);
```

Creates the table if it does not already exist.

---

## Insert

```sql
INSERT INTO videos (name, time)
VALUES (?, ?)
```

Adds a new video to the database.

---

## Select

```sql
SELECT * FROM videos
```

Retrieves all videos.

---

## Update

```sql
UPDATE videos
SET name = ?, time = ?
WHERE id = ?
```

Updates the selected video.

---

## Delete

```sql
DELETE FROM videos
WHERE id = ?
```

Removes a video from the database.

---

# 📖 Functions Explained

## list_all_videos()

Retrieves all records from the database and prints them.

Uses

```python
cursor.fetchall()
```

---

## add_video(name, time)

Inserts a new video into the database.

Uses

```python
cursor.execute()
conn.commit()
```

---

## update_video(video_id, new_name, new_time)

Updates a video's details based on its ID.

---

## delete_video(video_id)

Deletes a video from the database.

---

## main()

Displays the menu, accepts user input, and calls the appropriate function until the user exits.

---

# 🧠 Python Concepts Used

## sqlite3 Module

Connect to a database

```python
conn = sqlite3.connect("youtube_videos.db")
```

---

## Cursor Object

Execute SQL statements

```python
cursor = conn.cursor()
```

---

## execute()

Runs SQL queries

```python
cursor.execute(sql_query)
```

---

## commit()

Saves changes permanently.

```python
conn.commit()
```

Without calling `commit()`, inserted, updated, or deleted data will not be saved.

---

## fetchall()

Returns every row from the SELECT query.

```python
rows = cursor.fetchall()
```

---

## Parameterized Queries

Instead of writing

```python
"... VALUES ('Python',120)"
```

we use

```python
VALUES (?, ?)
```

This helps prevent SQL Injection and makes the code cleaner and safer.

---

## match-case

Python's switch-like statement.

```python
match choice:
    case 1:
        ...
```

---

# ▶️ How to Run

Clone the repository

```bash
git clone <repository-url>
```

Go to the project folder

```bash
cd youtube-manager-sqlite
```

Run the application

```bash
python youtube.py
```

The database file will be created automatically on the first run.

---

# 📋 Sample Menu

```
Youtube Manager | Choose an Option

1. List all YouTube videos
2. Add a YouTube video
3. Update a YouTube video
4. Delete a YouTube video
5. Exit
```

---

# 🎯 Learning Outcomes

By completing this project, I learned:

* How relational databases work
* Connecting Python with SQLite
* Creating database tables
* Executing SQL queries
* Performing CRUD operations
* Using parameterized SQL queries
* Managing transactions with `commit()`
* Building a menu-driven CLI application

---

# 🚀 Future Improvements

* Display videos in a formatted table
* Search videos by name
* Sort videos by duration
* Store duration as INTEGER instead of TEXT
* Validate user input
* Prevent duplicate entries
* Add categories
* Add upload date
* Mark videos as watched/unwatched
* Export data to CSV or JSON

---

# 👨‍💻 Author

**Rahul Meena**

Learning Python, SQL, and Backend Development one project at a time. 🚀
