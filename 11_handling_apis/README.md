# 🌐 Python API Handling

A beginner-friendly Python project that demonstrates how to consume REST APIs using the **`requests`** library. This project interacts with the **FreeAPI** service to fetch real-time data and display it in the terminal.

The project includes two API examples:

* 👤 Random User API
* 😂 Random Joke API

---

## 📚 Concepts Practiced

* REST APIs
* HTTP GET Requests
* Python `requests` Library
* JSON Parsing
* Nested Dictionaries
* Lists in JSON
* Exception Handling
* Functions
* Returning Multiple Values

---

## 🛠 Tech Stack

* Python 3
* Requests Library
* FreeAPI

---

## 📂 Project Structure

```text
11_handling_apis/
│
├── random_user.py          # Fetches a random user's username and country
├── random_joke.py          # Fetches a random joke
└── README.md
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jharwal77/python.git
```

### 2. Navigate to the Project Folder

```bash
cd python/11_handling_apis
```

### 3. Install Dependencies

```bash
pip install requests
```

```text
requests
```

---

## 🌍 APIs Used

### 👤 Random User API

**Endpoint**

```text
https://api.freeapi.app/api/v1/public/randomusers/user/random
```

### Information Retrieved

* Username
* Country

Example Output

```text
Username: redostrich300
Country: Canada
```

---

### 😂 Random Joke API

**Endpoint**

```text
https://api.freeapi.app/api/v1/public/randomjokes/joke/random
```

### Information Retrieved

* Joke Categories
* Joke Content

Example Output

```text
Categories: []

Joke:
Chuck Norris named his price and saved 15% or more on car insurance when he switched to Allstate.
```

---

## 📖 Code Overview

### Random User API

* Sends a GET request using `requests.get()`
* Parses the JSON response
* Extracts:

  * Username
  * Country
* Returns the extracted data
* Handles API errors using exceptions

---

### Random Joke API

* Sends a GET request
* Parses the JSON response
* Extracts:

  * Categories
  * Joke Content
* Returns the extracted data
* Handles API errors using exceptions

---

## 🧠 Python Concepts Used

### Sending HTTP Requests

```python
response = requests.get(url)
```

---

### Parsing JSON

```python
data = response.json()
```

---

### Accessing Nested Dictionary Values

Random User

```python
username = data["data"]["login"]["username"]
country = data["data"]["location"]["country"]
```

Random Joke

```python
categories = data["data"]["categories"]
content = data["data"]["content"]
```

---

### Returning Multiple Values

```python
return username, country
```

```python
username, country = fetch_random_user_freeapi()
```

---

### Exception Handling

```python
try:
    username, country = fetch_random_user_freeapi()
except Exception as e:
    print(e)
```

---

## ▶️ Running the Programs

Run the Random User API example:

```bash
python random_user.py
```

Run the Random Joke API example:

```bash
python random_joke.py
```

---

## 📋 Sample Output

### Random User

```text
Username: redostrich300
Country: Canada
```

### Random Joke

```text
Categories: []

Joke:
Chuck Norris named his price and saved 15% or more on car insurance when he switched to Allstate.
```

---

## 🎯 Learning Outcomes

After completing this project, I learned how to:

* Consume REST APIs in Python
* Send HTTP GET requests using `requests`
* Parse JSON responses
* Work with nested dictionaries and lists
* Handle API errors gracefully
* Build simple API-based command-line applications

---

## 🚀 Future Improvements

* Add request timeout handling
* Display HTTP status codes
* Fetch multiple users and jokes
* Save API responses to JSON files
* Create a menu-driven application
* Use authenticated APIs
* Add colored terminal output

---

## 👨‍💻 Author

**Rahul Meena**

GitHub: **https://github.com/Jharwal77**

Learning Python one project at a time. 🚀
