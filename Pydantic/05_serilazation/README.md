# Pydantic Model Serialization with Nested Models and Custom JSON Encoding

This project demonstrates how to use **Pydantic** models for structured data validation, nested models, default values, Python dictionary serialization, JSON serialization, and custom `datetime` formatting.

## 📌 Topics Covered

* `BaseModel`
* Nested Pydantic models
* Type annotations
* `List[str]`
* `datetime`
* Default field values
* `ConfigDict`
* Custom JSON encoders
* `model_dump()`
* `model_dump_json()`
* Python dictionary vs JSON serialization

---

## 📦 Installation

Install Pydantic using pip:

```bash
pip install pydantic
```

Check the installed version:

```bash
pip show pydantic
```

This example uses **Pydantic v2**.

---

## 📁 Project Structure

```text
pydantic-serialization/
│
├── main.py
└── README.md
```

---

## 💻 Complete Code

```python
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")
        }
    )


# Create a user instance
user = User(
    id=1,
    name="hitesh",
    email="hitesh@hc.com",
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="something",
        city="Jaipur",
        zip_code="001144"
    ),
    is_active=False,
    tags=["premium", "subscriber"],
)


# Using model_dump() -> Python dictionary
python_dict = user.model_dump()
print(python_dict)

print("=============================\n")


# Using model_dump_json() -> JSON string
json_str = user.model_dump_json()
print(json_str)
```

---

# 1. Importing Required Modules

```python
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime
```

### `BaseModel`

`BaseModel` is the foundation of Pydantic models.

```python
class User(BaseModel):
    ...
```

It provides features such as:

* Data validation
* Type checking
* Serialization
* Parsing
* Nested model support

---

### `ConfigDict`

`ConfigDict` is used in Pydantic v2 to configure model behavior.

In this example, it is used to define a custom JSON encoder for `datetime`.

```python
model_config = ConfigDict(
    json_encoders={
        datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")
    }
)
```

---

### `List`

`List` is imported from Python's `typing` module.

```python
tags: List[str]
```

This means `tags` should contain a list of strings.

Example:

```python
tags = ["premium", "subscriber"]
```

---

### `datetime`

The `datetime` class is used to represent date and time values.

```python
createdAt: datetime
```

Example:

```python
datetime(2024, 3, 15, 14, 30)
```

This represents:

```text
15 March 2024, 14:30
```

---

# 2. Creating the `Address` Model

```python
class Address(BaseModel):
    street: str
    city: str
    zip_code: str
```

The `Address` model contains three fields:

| Field      | Type  | Description        |
| ---------- | ----- | ------------------ |
| `street`   | `str` | Street address     |
| `city`     | `str` | City name          |
| `zip_code` | `str` | Postal or ZIP code |

Example:

```python
Address(
    street="something",
    city="Jaipur",
    zip_code="001144"
)
```

## Why is `zip_code` a string?

The ZIP code is defined as:

```python
zip_code: str
```

instead of:

```python
zip_code: int
```

This is useful because postal codes can contain leading zeros.

For example:

```text
001144
```

If stored as an integer:

```python
1144
```

the leading zeros would be lost.

---

# 3. Creating the `User` Model

```python
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []
```

The `User` model contains multiple data types.

| Field       | Type        | Default  | Description            |
| ----------- | ----------- | -------- | ---------------------- |
| `id`        | `int`       | Required | Unique user ID         |
| `name`      | `str`       | Required | User name              |
| `email`     | `str`       | Required | Email address          |
| `is_active` | `bool`      | `True`   | Account status         |
| `createdAt` | `datetime`  | Required | Creation date and time |
| `address`   | `Address`   | Required | Nested address model   |
| `tags`      | `List[str]` | `[]`     | User tags              |

---

# 4. Default Values

The `is_active` field has a default value:

```python
is_active: bool = True
```

If no value is provided:

```python
user = User(
    ...
)
```

then Pydantic automatically uses:

```python
is_active = True
```

However, in this example:

```python
is_active=False
```

so the default value is overridden.

---

# 5. Nested Pydantic Models

The `User` model contains another Pydantic model:

```python
address: Address
```

This is called a **nested model**.

The relationship looks like this:

```text
User
│
├── id
├── name
├── email
├── is_active
├── createdAt
├── tags
│
└── address
    ├── street
    ├── city
    └── zip_code
```

The nested `Address` object is created like this:

```python
address=Address(
    street="something",
    city="Jaipur",
    zip_code="001144"
)
```

This provides a clean and structured way to represent complex data.

---

# 6. Creating a User Instance

```python
user = User(
    id=1,
    name="hitesh",
    email="hitesh@hc.com",
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="something",
        city="Jaipur",
        zip_code="001144"
    ),
    is_active=False,
    tags=["premium", "subscriber"],
)
```

Pydantic validates the data according to the declared field types.

For example:

```python
id: int
```

expects an integer.

```python
name: str
```

expects a string.

```python
is_active: bool
```

expects a boolean.

```python
address: Address
```

expects a valid `Address` model.

---

# 7. Custom JSON Encoding

The model contains custom configuration:

```python
model_config = ConfigDict(
    json_encoders={
        datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")
    }
)
```

This tells Pydantic how to convert `datetime` objects during JSON serialization.

The format string is:

```python
"%d-%m-%Y %H:%M:%S"
```

Meaning:

| Format | Meaning                |
| ------ | ---------------------- |
| `%d`   | Day                    |
| `%m`   | Month                  |
| `%Y`   | Four-digit year        |
| `%H`   | Hour in 24-hour format |
| `%M`   | Minute                 |
| `%S`   | Second                 |

Given:

```python
datetime(2024, 3, 15, 14, 30)
```

the JSON output becomes:

```text
15-03-2024 14:30:00
```

---

# 8. Using `model_dump()`

```python
python_dict = user.model_dump()
print(python_dict)
```

The `model_dump()` method converts the Pydantic model into a Python dictionary.

Return type:

```python
dict
```

Conceptual output:

```python
{
    "id": 1,
    "name": "hitesh",
    "email": "hitesh@hc.com",
    "is_active": False,
    "createdAt": datetime(2024, 3, 15, 14, 30),
    "address": {
        "street": "something",
        "city": "Jaipur",
        "zip_code": "001144"
    },
    "tags": [
        "premium",
        "subscriber"
    ]
}
```

## Important Point

With:

```python
user.model_dump()
```

the `createdAt` value remains a Python `datetime` object.

The custom JSON encoder is mainly applied during JSON serialization.

---

# 9. Using `model_dump_json()`

```python
json_str = user.model_dump_json()
print(json_str)
```

The `model_dump_json()` method converts the Pydantic model into a JSON string.

Return type:

```python
str
```

Output:

```json
{
    "id": 1,
    "name": "hitesh",
    "email": "hitesh@hc.com",
    "is_active": false,
    "createdAt": "15-03-2024 14:30:00",
    "address": {
        "street": "something",
        "city": "Jaipur",
        "zip_code": "001144"
    },
    "tags": [
        "premium",
        "subscriber"
    ]
}
```

The actual printed JSON may appear on a single line.

Notice that:

```json
"createdAt": "15-03-2024 14:30:00"
```

uses the custom datetime format defined in `ConfigDict`.

---

# 10. `model_dump()` vs `model_dump_json()`

| Feature             | `model_dump()`                      | `model_dump_json()`               |
| ------------------- | ----------------------------------- | --------------------------------- |
| Return type         | `dict`                              | `str`                             |
| Output format       | Python dictionary                   | JSON string                       |
| Nested models       | Converted to dictionaries           | Converted to JSON objects         |
| `datetime`          | Usually remains `datetime`          | Serialized to string              |
| Custom JSON encoder | Not normally applied in Python mode | Applied during JSON serialization |
| Best use case       | Internal Python processing          | APIs, files, network transfer     |

---

## Example: `model_dump()`

```python
data = user.model_dump()

print(type(data))
```

Output:

```text
<class 'dict'>
```

---

## Example: `model_dump_json()`

```python
data = user.model_dump_json()

print(type(data))
```

Output:

```text
<class 'str'>
```

---

# 11. Python Dictionary vs JSON

A Python dictionary may contain Python-specific objects:

```python
{
    "createdAt": datetime(2024, 3, 15, 14, 30)
}
```

A JSON string cannot directly store a Python `datetime` object.

It needs a serializable representation:

```json
{
    "createdAt": "15-03-2024 14:30:00"
}
```

This is why custom serialization is useful.

---

# 12. Data Flow

The complete flow of the program is:

```text
Create Address Model
        │
        ▼
Create User Model
        │
        ▼
Add Nested Address
        │
        ▼
Add datetime Object
        │
        ▼
Create User Instance
        │
        ├──────────────────────┐
        ▼                      ▼
  model_dump()          model_dump_json()
        │                      │
        ▼                      ▼
 Python Dictionary         JSON String
        │                      │
        ▼                      ▼
 datetime object       Custom formatted datetime
```

---

# 13. Practical Use Cases

This pattern is commonly used in:

* REST APIs
* FastAPI applications
* User profile systems
* Database applications
* Backend services
* Configuration management
* Request validation
* Response serialization
* JSON file generation
* Microservices

For example, a backend application may receive user data, validate it with Pydantic, and serialize it into JSON before sending an API response.

---

# 14. Recommended Improvement

For modern Python, this:

```python
from typing import List
```

and:

```python
tags: List[str] = []
```

can be written as:

```python
tags: list[str] = []
```

A stronger pattern for list defaults is:

```python
from pydantic import BaseModel, Field

tags: list[str] = Field(default_factory=list)
```

This makes the intent of creating a fresh default list explicit.

Example:

```python
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: list[str] = Field(default_factory=list)
```

---

# 15. Key Learnings

After completing this example, I learned:

* How to create Pydantic models using `BaseModel`
* How to define typed model fields
* How to use default values
* How to create nested Pydantic models
* How to work with `datetime`
* How to configure models using `ConfigDict`
* How to define custom JSON encoders
* How to serialize models using `model_dump()`
* How to serialize models using `model_dump_json()`
* The difference between Python dictionaries and JSON strings
* How Pydantic handles nested serialization

---

## 🚀 Technologies Used

* Python
* Pydantic v2
* Python `datetime`
* Python type hints

---

## 👨‍💻 Author

**Rahul Meena**

Learning Python, Pydantic, backend development, and modern API development.
