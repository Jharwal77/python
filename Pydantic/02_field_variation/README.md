# Pydantic Employee Model

This project demonstrates how to create a validated data model in Python using **Pydantic**.

The goal of this exercise is to understand how Pydantic models work, how to define field constraints, how to use optional fields, and how to validate incoming data automatically.

---

## Topics Covered

* Pydantic `BaseModel`
* Field Validation
* Required Fields
* Optional Fields
* Default Values
* String Length Constraints
* Numeric Constraints
* Type Hints
* Automatic Data Validation

---

## Employee Model Requirements

The `Employee` model contains the following fields:

| Field        | Type            | Required | Validation                                  | Default     |
| ------------ | --------------- | -------- | ------------------------------------------- | ----------- |
| `id`         | `int`           | Yes      | Must be an integer                          | None        |
| `name`       | `str`           | Yes      | Minimum 3 characters, maximum 50 characters | None        |
| `department` | `Optional[str]` | No       | String or `None`                            | `"General"` |
| `salary`     | `float`         | Yes      | Must be greater than or equal to `10000`    | None        |

---

## Project Code

```python id="0fj7vt"
from typing import Optional

from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples=["Rahul Jharwal"]
    )

    department: Optional[str] = "General"

    salary: float = Field(
        ...,
        ge=10000
    )
```

---

## Understanding `BaseModel`

`BaseModel` is the foundation of Pydantic models.

```python id="glbyq3"
class Employee(BaseModel):
    ...
```

By inheriting from `BaseModel`, the `Employee` class gets:

* Automatic validation
* Type checking
* Data parsing
* Serialization
* JSON conversion
* JSON Schema generation

---

## Understanding `Field`

The `Field()` function is used to add validation rules and metadata to model fields.

Example:

```python id="x7ax9e"
name: str = Field(
    ...,
    min_length=3,
    max_length=50,
    description="Employee Name",
    examples=["Rahul Jharwal"]
)
```

This means:

* `name` is required
* Minimum length is 3 characters
* Maximum length is 50 characters
* The field has descriptive metadata
* An example value is provided for generated schemas and documentation

---

## Understanding `...`

In Pydantic:

```python id="ynqk0c"
name: str = Field(...)
```

The ellipsis `...` means that the field is required.

Therefore, a value must be provided for `name`.

Example:

```python id="0fvybe"
employee = Employee(
    id=1,
    name="Rahul Jharwal",
    salary=25000
)
```

If `name` is missing, Pydantic raises a validation error.

---

## String Length Validation

The `name` field uses:

```python id="ejt6ql"
min_length=3
```

This ensures that the employee name contains at least 3 characters.

Valid:

```python id="uekgup"
name="Rahul Jharwal"
```

Invalid:

```python id="2wr5tc"
name="Ra"
```

The invalid value fails because it contains fewer than 3 characters.

The model also uses:

```python id="7eg2qq"
max_length=50
```

This prevents names longer than 50 characters.

---

## Optional Fields

The `department` field is defined as:

```python id="77sb0w"
department: Optional[str] = "General"
```

`Optional[str]` means the value can be:

```python id="2n8esj"
str
```

or:

```python id="ayom68"
None
```

Because the field has a default value, it does not need to be provided when creating an employee.

Example:

```python id="3q8gt3"
employee = Employee(
    id=1,
    name="Rahul Jharwal",
    salary=25000
)
```

The department automatically becomes:

```text id="gwbw9e"
General
```

---

## Numeric Validation

The salary field is defined as:

```python id="p2zq8r"
salary: float = Field(
    ...,
    ge=10000
)
```

Here:

```text id="v6o2a7"
ge = greater than or equal to
```

Therefore:

```text id="8qecgr"
salary >= 10000
```

Valid:

```python id="pdtpsn"
salary=10000
```

Valid:

```python id="bq8j2r"
salary=50000
```

Invalid:

```python id="g6x3lv"
salary=5000
```

The invalid value fails because it is below the minimum allowed salary.

---

## Creating a Valid Employee

```python id="ue8mj7"
employee = Employee(
    id=1,
    name="Rahul Jharwal",
    department="Engineering",
    salary=50000
)

print(employee)
```

Example output:

```text id="ryg1wp"
id=1 name='Rahul Jharwal' department='Engineering' salary=50000.0
```

---

## Using the Default Department

```python id="pcghx7"
employee = Employee(
    id=2,
    name="Rahul Jharwal",
    salary=30000
)

print(employee)
```

Example output:

```text id="c3gduz"
id=2 name='Rahul Jharwal' department='General' salary=30000.0
```

Since no department was provided, Pydantic automatically uses:

```text id="2nbv8q"
General
```

---

## Validation Error Example

```python id="oc9bq4"
employee = Employee(
    id=3,
    name="Ra",
    salary=5000
)
```

This data is invalid because:

* `name` has fewer than 3 characters
* `salary` is below `10000`

Pydantic automatically raises a `ValidationError`.

---

## Handling Validation Errors

```python id="mp2yfv"
from pydantic import ValidationError

try:
    employee = Employee(
        id=3,
        name="Ra",
        salary=5000
    )

except ValidationError as error:
    print(error)
```

This allows validation failures to be handled safely.

---

## Pydantic v2 Serialization

Convert the model into a Python dictionary:

```python id="n6g4r1"
employee = Employee(
    id=1,
    name="Rahul Jharwal",
    salary=25000
)

print(employee.model_dump())
```

Example output:

```python id="7k0vqp"
{
    "id": 1,
    "name": "Rahul Jharwal",
    "department": "General",
    "salary": 25000.0
}
```

---

## Convert Model to JSON

```python id="8u7yye"
print(employee.model_dump_json())
```

Example output:

```json id="z6fkm5"
{
    "id": 1,
    "name": "Rahul Jharwal",
    "department": "General",
    "salary": 25000.0
}
```

---

## Generate JSON Schema

Pydantic can automatically generate a JSON Schema from the model.

```python id="g8hr41"
print(Employee.model_json_schema())
```

This feature is especially useful in:

* FastAPI
* REST APIs
* LLM structured outputs
* AI agents
* Tool calling systems
* Data validation pipelines

---

## Key Concepts Learned

### `BaseModel`

Used to create validated Pydantic models.

```python id="kqxy6u"
class Employee(BaseModel):
    ...
```

### `Field`

Used to define validation constraints and metadata.

```python id="sxjrv9"
Field(...)
```

### `min_length`

Defines the minimum allowed string length.

```python id="e5y1a7"
min_length=3
```

### `max_length`

Defines the maximum allowed string length.

```python id="4ob27j"
max_length=50
```

### `ge`

Means greater than or equal to.

```python id="brc4ws"
ge=10000
```

### `Optional`

Allows a field value to be either the specified type or `None`.

```python id="tzv7oc"
Optional[str]
```

---

## Project Structure

```text id="s85yyd"
Pydantic-Employee-Model/
│
├── employee.py
├── requirements.txt
└── README.md
```

---

## Installation

Install Pydantic:

```bash id="7s52h4"
pip install pydantic
```

Or using `uv`:

```bash id="f5aznn"
uv add pydantic
```

---

## Run the Project

Using Python:

```bash id="f9g21d"
python employee.py
```

Using `uv`:

```bash id="x9ppr3"
uv run employee.py
```

---

## Learning Outcome

After completing this exercise, I can:

* Create validated data models using Pydantic
* Use `BaseModel` to define structured Python models
* Apply field constraints using `Field()`
* Define required fields
* Define optional fields
* Set default values
* Validate string lengths
* Validate numeric ranges
* Handle validation errors
* Serialize Pydantic models
* Generate JSON Schema
* Understand how Pydantic models are used in APIs and AI applications

---

## Why This Matters for Agentic AI

AI agents frequently exchange structured data between:

* LLMs
* APIs
* Tools
* Databases
* External services

Pydantic helps ensure that this data follows a strict and predictable structure.

For example, an AI agent could require tool input like:

```python id="9xf7x0"
class SearchToolInput(BaseModel):
    query: str
    limit: int = Field(default=5, ge=1, le=20)
```

This makes tool inputs safer, validated, and easier to integrate with structured LLM workflows.

---

## Conclusion

This project demonstrates the fundamentals of Pydantic model creation and field validation.

The `Employee` model validates:

* Integer IDs
* Employee name length
* Optional department values
* Default values
* Minimum salary requirements

These concepts provide a strong foundation for building reliable Python applications, FastAPI APIs, and structured Agentic AI systems.
