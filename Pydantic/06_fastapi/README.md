# FastAPI with Pydantic Validation and Dependency Injection

This section contains my notes and practice code for learning how **Pydantic integrates with FastAPI**.

The goal of this exercise is to understand how to:

* Create a FastAPI application
* Define request body schemas using Pydantic
* Validate email addresses using `EmailStr`
* Create API endpoints
* Accept validated request data
* Use dependency injection
* Use FastAPI's `Depends()`
* Inject application settings into endpoints

---

## Topics Covered

* FastAPI
* Pydantic `BaseModel`
* Request Body Validation
* `EmailStr`
* POST Endpoints
* GET Endpoints
* Dependency Injection
* `Depends()`
* Settings Models
* Automatic Validation
* Automatic API Documentation
* Type Hints

---

## Project Code

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr


app = FastAPI()


class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str


class Settings(BaseModel):
    app_name: str = "Chai App"
    admin_email: str = "admin@chai.com"


def get_settings():
    return Settings()


@app.post("/signup")
def signup(user: UserSignup):
    return {
        "message": f"User {user.username} signed up successfully"
    }


@app.get("/settings")
def get_setttings_endpoint(
    settings: Settings = Depends(get_settings)
):
    return settings
```

---

# Understanding the Application

The application contains two API endpoints:

| Method | Endpoint    | Purpose                     |
| ------ | ----------- | --------------------------- |
| `POST` | `/signup`   | Register a user             |
| `GET`  | `/settings` | Return application settings |

The application also contains two Pydantic models:

1. `UserSignup`
2. `Settings`

---

# Creating the FastAPI Application

The project imports:

```python
from fastapi import FastAPI, Depends
```

Then creates the application:

```python
app = FastAPI()
```

The `app` object is the main FastAPI application instance.

The general flow is:

```text
FastAPI
   ↓
app = FastAPI()
   ↓
Define Routes
   ↓
Handle HTTP Requests
   ↓
Return Responses
```

---

# Understanding `BaseModel`

The project imports:

```python
from pydantic import BaseModel
```

Pydantic's `BaseModel` is used to create structured and validated data models.

Example:

```python
class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str
```

FastAPI uses this model to:

* Read the request body
* Parse incoming JSON
* Validate field types
* Generate API documentation
* Return validation errors automatically

---

# User Signup Model

The signup model is:

```python
class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str
```

It contains:

| Field      | Type       | Required | Description         |
| ---------- | ---------- | -------- | ------------------- |
| `username` | `str`      | Yes      | User's username     |
| `email`    | `EmailStr` | Yes      | Valid email address |
| `password` | `str`      | Yes      | User's password     |

All fields are required because no default values are provided.

---

# Understanding `EmailStr`

The project imports:

```python
from pydantic import EmailStr
```

The field:

```python
email: EmailStr
```

ensures that the provided value has a valid email format.

Valid example:

```text
rahul@example.com
```

Another valid example:

```text
admin@chai.com
```

Invalid example:

```text
rahul
```

Another invalid example:

```text
rahul@
```

If an invalid email is provided, Pydantic automatically raises a validation error.

---

# Email Validation Dependency

To use `EmailStr`, install email validation support.

Using `pip`:

```bash
pip install email-validator
```

Or install Pydantic with email support:

```bash
pip install "pydantic[email]"
```

Using `uv`:

```bash
uv add email-validator
```

Without this package, `EmailStr` may raise an import error.

---

# Signup Endpoint

The signup endpoint is:

```python
@app.post("/signup")
def signup(user: UserSignup):
    return {
        "message": f"User {user.username} signed up successfully"
    }
```

This creates a:

```text
POST /signup
```

endpoint.

---

# Understanding `@app.post()`

The decorator:

```python
@app.post("/signup")
```

tells FastAPI:

```text
When a POST request arrives
          ↓
at /signup
          ↓
execute signup()
```

The request flow is:

```text
Client
  ↓
POST /signup
  ↓
JSON Request Body
  ↓
UserSignup Model
  ↓
Pydantic Validation
  ↓
signup() Function
  ↓
JSON Response
```

---

# Request Body Validation

The endpoint contains:

```python
def signup(user: UserSignup):
```

Because `user` has the type:

```python
UserSignup
```

FastAPI treats it as a request body.

The client should send JSON like:

```json
{
  "username": "Rahul Jharwal",
  "email": "rahul@example.com",
  "password": "secret123"
}
```

FastAPI automatically converts this JSON into a `UserSignup` object.

Conceptually:

```text
Incoming JSON
      ↓
FastAPI
      ↓
Pydantic Validation
      ↓
UserSignup Object
      ↓
Endpoint Function
```

---

# Accessing Validated Data

Inside the endpoint:

```python
user.username
```

accesses the validated username.

Other fields can be accessed using:

```python
user.email
```

and:

```python
user.password
```

Example:

```python
@app.post("/signup")
def signup(user: UserSignup):
    print(user.username)
    print(user.email)

    return {
        "message": f"User {user.username} signed up successfully"
    }
```

---

# Successful Signup Request

Example request:

```json
{
  "username": "Rahul Jharwal",
  "email": "rahul@example.com",
  "password": "secret123"
}
```

Example response:

```json
{
  "message": "User Rahul Jharwal signed up successfully"
}
```

---

# Invalid Email Example

Consider this request:

```json
{
  "username": "Rahul Jharwal",
  "email": "rahul",
  "password": "secret123"
}
```

The email:

```text
rahul
```

is invalid.

Pydantic rejects the request before the endpoint logic executes.

FastAPI automatically returns a validation error response.

The HTTP status code is typically:

```text
422 Unprocessable Entity
```

---

# Settings Model

The second Pydantic model is:

```python
class Settings(BaseModel):
    app_name: str = "Chai App"
    admin_email: str = "admin@chai.com"
```

This model contains default application settings.

| Field         | Type  | Default            |
| ------------- | ----- | ------------------ |
| `app_name`    | `str` | `"Chai App"`       |
| `admin_email` | `str` | `"admin@chai.com"` |

Because both fields have default values, the model can be created without arguments.

Example:

```python
settings = Settings()
```

The resulting values are:

```text
app_name = "Chai App"
admin_email = "admin@chai.com"
```

---

# Dependency Function

The dependency function is:

```python
def get_settings():
    return Settings()
```

This function creates and returns a `Settings` object.

The flow is:

```text
get_settings()
      ↓
Settings()
      ↓
Settings Object
```

The returned object contains:

```json
{
  "app_name": "Chai App",
  "admin_email": "admin@chai.com"
}
```

---

# Understanding Dependency Injection

Dependency Injection means that an endpoint receives something it needs from another function instead of creating it directly.

Without dependency injection:

```python
@app.get("/settings")
def settings_endpoint():
    settings = Settings()

    return settings
```

Here, the endpoint creates the settings itself.

With dependency injection:

```python
@app.get("/settings")
def get_setttings_endpoint(
    settings: Settings = Depends(get_settings)
):
    return settings
```

FastAPI provides the settings object automatically.

---

# Understanding `Depends()`

The endpoint uses:

```python
settings: Settings = Depends(get_settings)
```

This tells FastAPI:

```text
Before executing the endpoint
          ↓
Call get_settings()
          ↓
Take its return value
          ↓
Pass it into settings
          ↓
Execute endpoint
```

The complete flow is:

```text
GET /settings
      ↓
FastAPI sees Depends(get_settings)
      ↓
FastAPI calls get_settings()
      ↓
get_settings() returns Settings()
      ↓
FastAPI injects the result
      ↓
settings parameter receives object
      ↓
Endpoint returns settings
```

---

# Settings Endpoint

The endpoint is:

```python
@app.get("/settings")
def get_setttings_endpoint(
    settings: Settings = Depends(get_settings)
):
    return settings
```

When a client sends:

```text
GET /settings
```

FastAPI first resolves the dependency.

Then it returns the settings.

Example response:

```json
{
  "app_name": "Chai App",
  "admin_email": "admin@chai.com"
}
```

---

# Why Use `Depends()`?

Dependency injection is useful for reusable logic.

Common use cases include:

* Authentication
* Database sessions
* Application configuration
* Current logged-in user
* Permission checking
* API key validation
* Shared services
* Repository objects
* Rate limiting

Example:

```text
Endpoint
   ↓
Depends()
   ↓
Reusable Dependency
   ↓
Injected Result
```

---

# Dependency Injection Example: Authentication

A future FastAPI application might use:

```python
def get_current_user():
    return {
        "username": "Rahul Jharwal"
    }
```

Then:

```python
@app.get("/profile")
def profile(
    current_user=Depends(get_current_user)
):
    return current_user
```

The flow becomes:

```text
GET /profile
      ↓
get_current_user()
      ↓
Current User
      ↓
Injected into Endpoint
      ↓
Response
```

This is why understanding `Depends()` is important for real backend applications.

---

# Running the FastAPI Application

Install FastAPI:

```bash
pip install fastapi
```

Install Uvicorn:

```bash
pip install uvicorn
```

Install email validation support:

```bash
pip install email-validator
```

Or using `uv`:

```bash
uv add fastapi uvicorn email-validator
```

---

# Start the Development Server

If the file is named:

```text
main.py
```

run:

```bash
uvicorn main:app --reload
```

Using `uv`:

```bash
uv run uvicorn main:app --reload
```

The server usually starts at:

```text
http://127.0.0.1:8000
```

---

# Understanding `main:app`

The command:

```bash
uvicorn main:app --reload
```

contains:

```text
main
 ↓
main.py file
```

and:

```text
app
 ↓
FastAPI application object
```

Therefore:

```text
main:app
```

means:

```text
Find app inside main.py
```

---

# Automatic API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

This opens Swagger UI.

You can test:

* `POST /signup`
* `GET /settings`

directly from the browser.

FastAPI also provides ReDoc documentation at:

```text
http://127.0.0.1:8000/redoc
```

---

# Testing the Signup Endpoint

Open:

```text
/docs
```

Select:

```text
POST /signup
```

Click:

```text
Try it out
```

Provide:

```json
{
  "username": "Rahul Jharwal",
  "email": "rahul@example.com",
  "password": "secret123"
}
```

Then execute the request.

Expected response:

```json
{
  "message": "User Rahul Jharwal signed up successfully"
}
```

---

# Testing the Settings Endpoint

Select:

```text
GET /settings
```

Execute the request.

Expected response:

```json
{
  "app_name": "Chai App",
  "admin_email": "admin@chai.com"
}
```

---

# Complete Request Flow

## Signup Flow

```text
Client
  ↓
POST /signup
  ↓
JSON Body
  ↓
UserSignup
  ↓
Pydantic Validation
  ↓
FastAPI Endpoint
  ↓
JSON Response
```

## Settings Flow

```text
Client
  ↓
GET /settings
  ↓
Depends(get_settings)
  ↓
get_settings()
  ↓
Settings()
  ↓
Dependency Injection
  ↓
Endpoint
  ↓
JSON Response
```

---

# Key Concepts Learned

## `FastAPI`

Creates the web application.

```python
app = FastAPI()
```

---

## `BaseModel`

Creates validated data models.

```python
class UserSignup(BaseModel):
    ...
```

---

## `EmailStr`

Validates email addresses.

```python
email: EmailStr
```

---

## `@app.post()`

Creates a POST endpoint.

```python
@app.post("/signup")
```

---

## `@app.get()`

Creates a GET endpoint.

```python
@app.get("/settings")
```

---

## `Depends()`

Declares a FastAPI dependency.

```python
Depends(get_settings)
```

---

## Dependency Function

Provides reusable data or logic.

```python
def get_settings():
    return Settings()
```

---

## Dependency Injection

FastAPI automatically provides the dependency result to the endpoint.

```python
settings: Settings = Depends(get_settings)
```

---

# Real-World Use Cases

These concepts are commonly used in production FastAPI applications.

## User Registration

```text
Signup Request
      ↓
Pydantic Validation
      ↓
Create User
```

---

## Authentication

```text
Request
   ↓
Depends(get_current_user)
   ↓
Authenticated User
   ↓
Protected Endpoint
```

---

## Database Sessions

```text
Endpoint
   ↓
Depends(get_db)
   ↓
Database Session
```

---

## Application Settings

```text
Endpoint
   ↓
Depends(get_settings)
   ↓
Application Configuration
```

---

## Permission Checking

```text
Request
   ↓
Depends(require_admin)
   ↓
Authorization Check
   ↓
Endpoint
```

---

# Why This Matters for Agentic AI

FastAPI and Pydantic are highly relevant to Agentic AI systems.

AI applications often expose agents through APIs.

Example architecture:

```text
Frontend
   ↓
FastAPI Endpoint
   ↓
Pydantic Validation
   ↓
AI Agent
   ↓
LLM
   ↓
Tool Calls
   ↓
Structured Response
```

For example:

```python
class AgentRequest(BaseModel):
    query: str
    user_id: int
```

Then:

```python
@app.post("/agent")
def run_agent(request: AgentRequest):
    return {
        "query": request.query
    }
```

Dependency injection can also provide:

* LLM clients
* Database connections
* Vector databases
* Authentication
* Agent configuration
* Tool registries
* API clients

Example:

```text
Agent Endpoint
      ↓
Depends(get_llm_client)
      ↓
LLM Client
      ↓
Agent Execution
```

This makes FastAPI's dependency injection system particularly useful for building structured AI backends.

---

# Project Structure

```text
FastAPI-Pydantic/
│
├── main.py
└── README.md
```

---

# Installation

Using `pip`:

```bash
pip install fastapi uvicorn email-validator
```

Using `uv`:

```bash
uv add fastapi uvicorn email-validator
```

---

# Run the Application

Using Uvicorn:

```bash
uvicorn main:app --reload
```

Using `uv`:

```bash
uv run uvicorn main:app --reload
```

---

# Learning Outcome

After completing this exercise, I can:

* Create a FastAPI application
* Create Pydantic request models
* Validate request bodies automatically
* Validate email addresses using `EmailStr`
* Create POST endpoints
* Create GET endpoints
* Access validated Pydantic model data
* Create application settings models
* Define dependency functions
* Use FastAPI's `Depends()`
* Understand dependency injection
* Return Pydantic models from endpoints
* Use automatic API documentation
* Understand how FastAPI and Pydantic work together

---

# Conclusion

This exercise helped me understand how **Pydantic integrates with FastAPI**.

The main request-validation flow is:

```text
JSON Request
     ↓
FastAPI
     ↓
Pydantic Model
     ↓
Automatic Validation
     ↓
Endpoint Function
```

I also learned how dependency injection works:

```text
Endpoint
    ↓
Depends(get_settings)
    ↓
Dependency Function
    ↓
Settings Object
    ↓
Injected into Endpoint
```

The most important concepts learned in this section are:

* Pydantic request body validation
* `EmailStr`
* FastAPI endpoints
* `Depends()`
* Dependency injection
* Application settings

These concepts provide a foundation for building backend APIs and Agentic AI services with FastAPI and Pydantic.
