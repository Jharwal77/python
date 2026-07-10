# FastAPI with Pydantic and Dependency Injection

This project contains my practice code and notes for learning how **Pydantic integrates with FastAPI**.

The goal of this exercise is to understand how to:

* Create a FastAPI application
* Define request body models using Pydantic
* Validate email addresses using `EmailStr`
* Create GET and POST API endpoints
* Use default values in Pydantic models
* Create reusable dependencies
* Use FastAPI's `Depends()`
* Understand basic dependency injection

---

## Topics Covered

* FastAPI
* Pydantic `BaseModel`
* `EmailStr`
* Request Body Validation
* POST Endpoints
* GET Endpoints
* `Depends()`
* Dependency Injection
* Default Values
* Automatic Validation
* API Documentation

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

## Application Structure

This application contains:

### Pydantic Models

* `UserSignup`
* `Settings`

### Dependency Function

* `get_settings()`

### API Endpoints

* `POST /signup`
* `GET /settings`

The basic structure is:

```text
FastAPI Application
│
├── UserSignup Model
│
├── Settings Model
│
├── get_settings() Dependency
│
├── POST /signup
│
└── GET /settings
```

---

## Creating the FastAPI Application

The application starts with:

```python
app = FastAPI()
```

This creates the main FastAPI application instance.

Routes are registered on this object using decorators such as:

```python
@app.post(...)
```

and:

```python
@app.get(...)
```

---

## UserSignup Model

The signup request model is:

```python
class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str
```

This model defines the expected structure of the signup request body.

| Field      | Type       | Required | Description          |
| ---------- | ---------- | -------- | -------------------- |
| `username` | `str`      | Yes      | Username of the user |
| `email`    | `EmailStr` | Yes      | Valid email address  |
| `password` | `str`      | Yes      | User password        |

Because these fields do not have default values, all of them are required.

---

## Understanding `BaseModel`

The models inherit from:

```python
BaseModel
```

Example:

```python
class UserSignup(BaseModel):
    ...
```

`BaseModel` provides:

* Automatic validation
* Type checking
* Data parsing
* Serialization
* JSON Schema generation

FastAPI uses these capabilities to validate incoming request data.

---

## Understanding `EmailStr`

The email field is defined as:

```python
email: EmailStr
```

`EmailStr` validates whether the input follows a valid email format.

Valid examples:

```text
rahul@example.com
admin@chai.com
user@gmail.com
```

Invalid examples:

```text
rahul
rahul@
@example.com
```

If an invalid email is sent, Pydantic validation fails automatically.

---

## Installing Email Validation Support

`EmailStr` requires email validation support.

Using `pip`:

```bash
pip install email-validator
```

Or:

```bash
pip install "pydantic[email]"
```

Using `uv`:

```bash
uv add email-validator
```

---

## Signup Endpoint

The signup endpoint is:

```python
@app.post("/signup")
def signup(user: UserSignup):
    return {
        "message": f"User {user.username} signed up successfully"
    }
```

This creates:

```text
POST /signup
```

The endpoint expects request data matching the `UserSignup` model.

---

## Request Body Validation

The parameter:

```python
user: UserSignup
```

tells FastAPI that the request body should follow this structure:

```json
{
  "username": "Rahul Jharwal",
  "email": "rahul@example.com",
  "password": "secret123"
}
```

The request flow is:

```text
Client Request
      ↓
POST /signup
      ↓
JSON Request Body
      ↓
UserSignup Model
      ↓
Pydantic Validation
      ↓
Endpoint Function
      ↓
JSON Response
```

---

## Successful Signup Request

Example request:

```json
{
  "username": "Rahul Jharwal",
  "email": "rahul@example.com",
  "password": "secret123"
}
```

Expected response:

```json
{
  "message": "User Rahul Jharwal signed up successfully"
}
```

---

## Invalid Email Request

Example:

```json
{
  "username": "Rahul Jharwal",
  "email": "rahul",
  "password": "secret123"
}
```

The value:

```text
rahul
```

is not a valid email address.

The validation flow is:

```text
Invalid Request
      ↓
Pydantic Validation
      ↓
EmailStr Validation Fails
      ↓
Endpoint Does Not Execute
      ↓
FastAPI Returns Validation Error
```

FastAPI normally returns:

```text
422 Unprocessable Entity
```

---

## Settings Model

The second Pydantic model is:

```python
class Settings(BaseModel):
    app_name: str = "Chai App"
    admin_email: str = "admin@chai.com"
```

This model stores basic application settings.

| Field         | Type  | Default            |
| ------------- | ----- | ------------------ |
| `app_name`    | `str` | `"Chai App"`       |
| `admin_email` | `str` | `"admin@chai.com"` |

Both fields have default values.

Therefore, this works:

```python
settings = Settings()
```

The resulting object contains:

```text
app_name = "Chai App"
admin_email = "admin@chai.com"
```

---

## Dependency Function

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

The returned data is:

```json
{
  "app_name": "Chai App",
  "admin_email": "admin@chai.com"
}
```

---

## Settings Endpoint

The settings endpoint is:

```python
@app.get("/settings")
def get_setttings_endpoint(
    settings: Settings = Depends(get_settings)
):
    return settings
```

This creates:

```text
GET /settings
```

The endpoint uses FastAPI dependency injection.

---

## Understanding `Depends()`

The important line is:

```python
settings: Settings = Depends(get_settings)
```

This tells FastAPI to call:

```python
get_settings()
```

before executing the endpoint.

The returned value is then passed into:

```python
settings
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
Result is injected into settings
      ↓
Endpoint executes
      ↓
Settings are returned
```

---

## Understanding Dependency Injection

Dependency Injection means that a function receives something it needs from an external provider instead of creating that object directly.

Without dependency injection:

```python
@app.get("/settings")
def get_settings_endpoint():
    settings = Settings()
    return settings
```

The endpoint creates the object itself.

With dependency injection:

```python
@app.get("/settings")
def get_settings_endpoint(
    settings: Settings = Depends(get_settings)
):
    return settings
```

FastAPI provides the object automatically.

---

## Why Use Dependency Injection?

Dependency injection helps make code:

* Reusable
* Modular
* Easier to test
* Easier to maintain
* Less repetitive

Common FastAPI dependencies include:

* Database sessions
* Authentication
* Current logged-in user
* Application settings
* API key validation
* Permission checking
* Shared services

---

## Example: Database Dependency

A future application might contain:

```python
def get_db():
    return database_connection
```

Then:

```python
@app.get("/users")
def get_users(
    db=Depends(get_db)
):
    return db.get_users()
```

The flow becomes:

```text
GET /users
    ↓
Depends(get_db)
    ↓
Database Connection
    ↓
Endpoint
```

---

## Example: Authentication Dependency

A protected endpoint might use:

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
Depends(get_current_user)
      ↓
Current User
      ↓
Endpoint
      ↓
Response
```

---

## Running the Application

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

Or install everything using:

```bash
pip install fastapi uvicorn email-validator
```

Using `uv`:

```bash
uv add fastapi uvicorn email-validator
```

---

## Start the Development Server

If the Python file is named:

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

---

## Understanding `main:app`

In:

```bash
uvicorn main:app --reload
```

`main` refers to:

```text
main.py
```

`app` refers to:

```python
app = FastAPI()
```

Therefore:

```text
main:app
```

means:

```text
main.py
   ↓
find
   ↓
app
```

---

## Automatic API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

This opens Swagger UI.

You can test:

```text
POST /signup
```

and:

```text
GET /settings
```

directly from the browser.

FastAPI also provides ReDoc at:

```text
http://127.0.0.1:8000/redoc
```

---

## Testing `/signup`

Open Swagger UI and select:

```text
POST /signup
```

Use this request body:

```json
{
  "username": "Rahul Jharwal",
  "email": "rahul@example.com",
  "password": "secret123"
}
```

Expected response:

```json
{
  "message": "User Rahul Jharwal signed up successfully"
}
```

---

## Testing `/settings`

Send:

```text
GET /settings
```

Expected response:

```json
{
  "app_name": "Chai App",
  "admin_email": "admin@chai.com"
}
```

---

## Complete Application Flow

### Signup Flow

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
signup()
  ↓
JSON Response
```

### Settings Flow

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

## Key Concepts Learned

### `FastAPI`

Creates the API application:

```python
app = FastAPI()
```

### `BaseModel`

Creates validated Pydantic models:

```python
class UserSignup(BaseModel):
    ...
```

### `EmailStr`

Validates email addresses:

```python
email: EmailStr
```

### `@app.post()`

Creates a POST endpoint:

```python
@app.post("/signup")
```

### `@app.get()`

Creates a GET endpoint:

```python
@app.get("/settings")
```

### `Depends()`

Declares a dependency:

```python
Depends(get_settings)
```

### Dependency Function

Provides reusable data:

```python
def get_settings():
    return Settings()
```

### Dependency Injection

Injects the dependency result into an endpoint:

```python
settings: Settings = Depends(get_settings)
```

---

## Why This Matters for Backend Development

These concepts are widely used in backend applications.

For example:

```text
Frontend
   ↓
FastAPI Endpoint
   ↓
Pydantic Validation
   ↓
Business Logic
   ↓
Database
   ↓
JSON Response
```

Pydantic ensures incoming data has the correct structure before application logic runs.

---

## Why This Matters for Agentic AI

Agentic AI systems frequently use FastAPI to expose agents as web services.

Example architecture:

```text
Frontend
   ↓
FastAPI
   ↓
Pydantic Request Model
   ↓
AI Agent
   ↓
LLM
   ↓
Tools
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
def run_agent(
    request: AgentRequest
):
    return {
        "query": request.query
    }
```

FastAPI dependencies can also provide:

* LLM clients
* Database connections
* Authentication
* Agent configuration
* Tool registries
* Vector database clients
* External API clients

Example flow:

```text
Agent Endpoint
      ↓
Depends(get_agent)
      ↓
Agent Instance
      ↓
Execute Task
      ↓
Return Response
```

---

## Project Structure

```text
FastAPI-Pydantic/
│
├── main.py
└── README.md
```

---

## Installation

Using `pip`:

```bash
pip install fastapi uvicorn email-validator
```

Using `uv`:

```bash
uv add fastapi uvicorn email-validator
```

---

## Run the Application

Using Uvicorn:

```bash
uvicorn main:app --reload
```

Using `uv`:

```bash
uv run uvicorn main:app --reload
```

---

## Learning Outcome

After completing this exercise, I can:

* Create a FastAPI application
* Define Pydantic models
* Validate request bodies
* Validate email addresses using `EmailStr`
* Create POST endpoints
* Create GET endpoints
* Use default values in Pydantic models
* Create dependency functions
* Use FastAPI's `Depends()`
* Understand basic dependency injection
* Return Pydantic models from endpoints
* Test APIs using Swagger UI
* Understand how FastAPI and Pydantic work together

---

## Conclusion

This exercise helped me understand how **FastAPI and Pydantic work together**.

For request validation:

```text
JSON Request
     ↓
FastAPI
     ↓
Pydantic Model
     ↓
Automatic Validation
     ↓
Endpoint
```

For dependency injection:

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

The main concepts learned in this exercise are:

* Pydantic request body validation
* `EmailStr`
* FastAPI GET and POST endpoints
* `Depends()`
* Dependency injection
* Application settings

These concepts provide a strong foundation for learning FastAPI backend development and building API-based Agentic AI applications.
