# 📺 YouTube Manager (MongoDB)

A simple command-line YouTube Video Manager built with **Python** and **MongoDB**. This project demonstrates CRUD (Create, Read, Update, Delete) operations using the **PyMongo** library and securely stores the MongoDB connection string using a `.env` file.

---

## 🚀 Features

* 📋 List all videos
* ➕ Add a new video
* ✏️ Update video details
* ❌ Delete a video
* 🔒 Secure MongoDB connection using `.env`
* ✅ MongoDB connection verification using `ping()`
* ⚠️ Exception handling for invalid MongoDB Object IDs
* 📝 Input validation for video name and duration
* 📂 Videos sorted by latest added

---

## 🛠️ Technologies Used

* Python 3
* MongoDB
* PyMongo
* python-dotenv

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jharwal77/python.git

cd youtube-manager-mongodb
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```


## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
MONGODB_URL=your_mongodb_connection_string
```

Example:

```env
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

> **Note:** Never upload your `.env` file to GitHub.

---

## 📁 Project Structure

```
youtube-manager-mongodb/
│
├── .env
├── youtube_manager_mongodb.py
└── README.md
```

---

## ▶️ Run the Project

```bash
python youtube_manager_mongodb.py
```

---

## 📌 Menu

```
YouTube Manager

1. List all YouTube videos
2. Add a YouTube video
3. Update a YouTube video
4. Delete a YouTube video
5. Exit
```

---

## 📚 MongoDB Operations Used

### Connect to MongoDB

```python
MongoClient()
```

### Check Connection

```python
client.admin.command("ping")
```

### Insert Document

```python
insert_one()
```

### Find Documents

```python
find()
```

### Sort Documents

```python
sort()
```

### Update Document

```python
update_one()
```

### Delete Document

```python
delete_one()
```

### Convert String to ObjectId

```python
ObjectId()
```

---

## 📖 Python Concepts Practiced

* Functions
* Exception Handling (`try-except`)
* Environment Variables (`.env`)
* User Input
* Loops
* Match-Case Statement
* Lists
* Dictionaries
* MongoDB CRUD Operations
* Input Validation
* String Methods (`strip()`)
* Working with ObjectId

---

## 📷 Sample Output

```
✅ Connected to MongoDB Successfully.

YouTube Manager

1. List all YouTube videos
2. Add a YouTube video
3. Update a YouTube video
4. Delete a YouTube video
5. Exit

Enter Your Choice: 2

Enter the new video name: Python MongoDB CRUD
Enter the new video time in minutes: 45

✅ Video Added Successfully!
Inserted ID: 684f4e1d9d4f98e8a3b54f6c
```

---

## 🎯 Future Improvements

* Search videos by name
* Pagination
* Store upload date
* Video categories
* Logging
* Export data to CSV
* REST API using Flask/FastAPI
* GUI using Tkinter or Streamlit

---

## 👨‍💻 Author

**Rahul Meena**

GitHub: https://github.com/Jharwal77
