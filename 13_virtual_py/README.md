# 🐍 Python Virtual Environment (venv)

This project demonstrates how to create and manage a Python Virtual Environment (`venv`). It covers creating a virtual environment, activating it, installing packages, generating a `requirements.txt` file, uninstalling packages, and deactivating the environment.

---

# 📚 What is a Virtual Environment?

A **Virtual Environment** is an isolated Python environment that allows a project to have its own Python interpreter and installed packages without affecting the global Python installation or other projects.

### Why use a Virtual Environment?

* Isolates project dependencies
* Avoids package version conflicts
* Makes projects portable
* Keeps the global Python installation clean
* Makes collaboration easier

---

# 🛠 Technologies Used

* Python 3
* venv
* pip
* PowerShell (Windows)

---

# 📁 Project Structure

```text
13_virtual_py/
│
├── .venv/
├── requirements.txt
└── README.md
```

---

# 🚀 Create a Virtual Environment

Open the terminal inside your project folder and run:

```bash
python -m venv .venv
```

This creates a folder named `.venv` containing:

* Python Interpreter
* pip
* Scripts
* Installed packages
* Configuration files

---

# ▶️ Activate the Virtual Environment

## Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

---

## Linux / macOS

```bash
source .venv/bin/activate
```

---

# ✅ Verify the Virtual Environment

Check the Python version:

```bash
python --version
```

Check installed packages:

```bash
pip list
```

---

# 📦 Install Packages

Install a package:

```bash
pip install pymongo
```

Install multiple packages:

```bash
pip install Django
```

---

# 📋 View Installed Packages

```bash
pip list
```

Example output:

```text
Package   Version
--------- -------
Django    6.0.6
asgiref   3.11.1
dnspython 2.8.0
pip       26.1.1
sqlparse  0.5.5
tzdata    2026.2
```

---

# 🗑 Uninstall a Package

```bash
pip uninstall pymongo
```

---

# 📄 Generate requirements.txt

Generate a list of installed packages:

```bash
pip freeze > requirements.txt
```

Example:

```text
Django==6.0.6
asgiref==3.11.1
dnspython==2.8.0
sqlparse==0.5.5
tzdata==2026.2
```

> **Note:** `pip freeze` is recommended over `pip list` because it includes exact package versions and uses the correct format for reinstalling dependencies.

---

# 📥 Install Packages from requirements.txt

```bash
pip install -r requirements.txt
```

This installs all project dependencies listed in the file.

---

# ❌ Deactivate the Virtual Environment

When you're finished working:

```bash
deactivate
```

Your terminal prompt will no longer display `(.venv)`.

---

# 📚 Commands Practiced

| Command                           | Description                               |
| --------------------------------- | ----------------------------------------- |
| `python -m venv .venv`            | Create a virtual environment              |
| `.\.venv\Scripts\Activate.ps1`    | Activate virtual environment (PowerShell) |
| `python --version`                | Check Python version                      |
| `pip list`                        | List installed packages                   |
| `pip install package_name`        | Install a package                         |
| `pip uninstall package_name`      | Remove a package                          |
| `pip freeze > requirements.txt`   | Save dependencies                         |
| `pip install -r requirements.txt` | Install dependencies                      |
| `deactivate`                      | Exit the virtual environment              |

---

# 📖 Concepts Learned

* What is a Virtual Environment
* Why Virtual Environments are important
* Creating a virtual environment
* Activating and deactivating a virtual environment
* Installing packages with pip
* Removing packages
* Listing installed packages
* Managing project dependencies
* Creating and using `requirements.txt`
* Isolated project environments

---

# ⚠️ Common Mistakes

### Wrong folder name

```powershell
.\.venv\Script\activate
```

Correct:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### Incorrect version command

Wrong:

```bash
python --v
```

Correct:

```bash
python --version
```

---

### Using `which` on Windows PowerShell

Wrong:

```powershell
which python
```

Correct:

```powershell
Get-Command python
```

or

```powershell
where python
```

---

# 📌 Best Practices

* Create a new virtual environment for every project.
* Do not commit the `.venv` folder to Git.
* Always include a `requirements.txt` file.
* Activate the virtual environment before installing packages.
* Keep dependencies updated when necessary.

---

# 📄 .gitignore

```gitignore
.venv/
__pycache__/
*.pyc
```

---

# 👨‍💻 Author

**Rahul Meena**

GitHub: https://github.com/Jharwal77
