# Pydantic Nested Models

This section contains my notes and practice code for learning **Nested Models in Pydantic**.

The goal of this exercise is to understand how multiple Pydantic models can be connected to represent hierarchical and structured data.

In this example, I created a course structure where:

```text
Course
  └── Modules
        └── Lessons
```

A `Course` contains multiple `Module` objects, and each `Module` contains multiple `Lesson` objects.

---

## Topics Covered

* Pydantic `BaseModel`
* Nested Models
* Lists of Models
* Hierarchical Data Structures
* `List` Type Hint
* Automatic Nested Validation
* Data Parsing
* Model Serialization
* JSON Conversion
* Structured Data Modeling

---

## Project Code

```python
from pydantic import BaseModel
from typing import List


class Lesson(BaseModel):
    lesson_id: int
    topic: str


class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]


class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]
```

---

## Understanding the Model Structure

This project contains three Pydantic models:

1. `Lesson`
2. `Module`
3. `Course`

The relationship between them is:

```text
Course
│
├── Module
│   ├── Lesson
│   ├── Lesson
│   └── Lesson
│
└── Module
    ├── Lesson
    └── Lesson
```

This is called a **nested model structure**.

---

## 1. Lesson Model

The smallest model in the hierarchy is `Lesson`.

```python
class Lesson(BaseModel):
    lesson_id: int
    topic: str
```

Each lesson contains:

| Field       | Type  | Description                      |
| ----------- | ----- | -------------------------------- |
| `lesson_id` | `int` | Unique identifier for the lesson |
| `topic`     | `str` | Topic of the lesson              |

Example:

```python
lesson = Lesson(
    lesson_id=1,
    topic="Introduction to Pydantic"
)
```

---

## 2. Module Model

The `Module` model contains multiple lessons.

```python
class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]
```

Each module contains:

| Field       | Type           | Description                      |
| ----------- | -------------- | -------------------------------- |
| `module_id` | `int`          | Unique identifier for the module |
| `name`      | `str`          | Name of the module               |
| `lessons`   | `List[Lesson]` | List of lesson objects           |

The important part is:

```python
lessons: List[Lesson]
```

This means that `lessons` must contain a list of valid `Lesson` objects.

Example:

```python
module = Module(
    module_id=1,
    name="Pydantic Fundamentals",
    lessons=[
        Lesson(
            lesson_id=1,
            topic="Introduction to Pydantic"
        ),
        Lesson(
            lesson_id=2,
            topic="Understanding BaseModel"
        )
    ]
)
```

---

## 3. Course Model

The `Course` model is the top-level model.

```python
class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]
```

Each course contains:

| Field       | Type           | Description                      |
| ----------- | -------------- | -------------------------------- |
| `course_id` | `int`          | Unique identifier for the course |
| `title`     | `str`          | Course title                     |
| `modules`   | `List[Module]` | List of module objects           |

The important part is:

```python
modules: List[Module]
```

This means a course can contain multiple modules.

---

## Understanding `List`

The project imports:

```python
from typing import List
```

This allows us to define lists containing specific types.

Example:

```python
lessons: List[Lesson]
```

This means:

```text
A list containing Lesson objects
```

Similarly:

```python
modules: List[Module]
```

means:

```text
A list containing Module objects
```

---

## Complete Course Example

Here is a complete example using my Pydantic learning journey:

```python
course = Course(
    course_id=101,
    title="Python for Agentic AI",
    modules=[
        Module(
            module_id=1,
            name="Pydantic Fundamentals",
            lessons=[
                Lesson(
                    lesson_id=1,
                    topic="Introduction to Pydantic"
                ),
                Lesson(
                    lesson_id=2,
                    topic="BaseModel"
                ),
                Lesson(
                    lesson_id=3,
                    topic="Field Validation"
                )
            ]
        ),
        Module(
            module_id=2,
            name="Advanced Pydantic",
            lessons=[
                Lesson(
                    lesson_id=4,
                    topic="Computed Fields"
                ),
                Lesson(
                    lesson_id=5,
                    topic="Nested Models"
                )
            ]
        )
    ]
)

print(course)
```

---

## Hierarchical Representation

The created data looks like this:

```text
Python for Agentic AI
│
├── Pydantic Fundamentals
│   ├── Introduction to Pydantic
│   ├── BaseModel
│   └── Field Validation
│
└── Advanced Pydantic
    ├── Computed Fields
    └── Nested Models
```

This structure represents real-world hierarchical data.

---

## Automatic Nested Validation

One of the most powerful features of Pydantic is automatic nested validation.

Consider this input:

```python
course = Course(
    course_id=101,
    title="Python for Agentic AI",
    modules=[
        {
            "module_id": 1,
            "name": "Pydantic Fundamentals",
            "lessons": [
                {
                    "lesson_id": 1,
                    "topic": "BaseModel"
                }
            ]
        }
    ]
)
```

Notice that we passed normal Python dictionaries instead of manually creating `Module` and `Lesson` objects.

Pydantic automatically converts:

```text
Dictionary
    ↓
Module Model
```

and:

```text
Dictionary
    ↓
Lesson Model
```

This is one of the major advantages of nested Pydantic models.

---

## Example Using Dictionaries

```python
course = Course(
    course_id=101,
    title="Python for Agentic AI",
    modules=[
        {
            "module_id": 1,
            "name": "Pydantic Fundamentals",
            "lessons": [
                {
                    "lesson_id": 1,
                    "topic": "Introduction to Pydantic"
                },
                {
                    "lesson_id": 2,
                    "topic": "BaseModel"
                }
            ]
        }
    ]
)

print(course)
```

Pydantic automatically validates and converts the nested dictionaries into the correct model types.

---

## Checking Nested Object Types

We can verify the generated object types:

```python
print(type(course))
print(type(course.modules[0]))
print(type(course.modules[0].lessons[0]))
```

Expected output:

```text
<class '__main__.Course'>
<class '__main__.Module'>
<class '__main__.Lesson'>
```

This confirms that Pydantic automatically created nested model objects.

---

## Accessing Nested Data

We can access the course title:

```python
print(course.title)
```

Access the first module:

```python
print(course.modules[0])
```

Access the first module name:

```python
print(course.modules[0].name)
```

Access the first lesson:

```python
print(course.modules[0].lessons[0])
```

Access the first lesson topic:

```python
print(course.modules[0].lessons[0].topic)
```

Example output:

```text
Introduction to Pydantic
```

---

## Iterating Through Modules

We can loop through all modules:

```python
for module in course.modules:
    print(module.name)
```

Example output:

```text
Pydantic Fundamentals
Advanced Pydantic
```

---

## Iterating Through Lessons

We can loop through every lesson inside every module:

```python
for module in course.modules:
    print(f"Module: {module.name}")

    for lesson in module.lessons:
        print(f"  Lesson: {lesson.topic}")
```

Example output:

```text
Module: Pydantic Fundamentals
  Lesson: Introduction to Pydantic
  Lesson: BaseModel
  Lesson: Field Validation

Module: Advanced Pydantic
  Lesson: Computed Fields
  Lesson: Nested Models
```

---

## Model Serialization

Pydantic v2 provides:

```python
model_dump()
```

This converts the complete nested model into a Python dictionary.

Example:

```python
course_dict = course.model_dump()

print(course_dict)
```

Example output:

```python
{
    "course_id": 101,
    "title": "Python for Agentic AI",
    "modules": [
        {
            "module_id": 1,
            "name": "Pydantic Fundamentals",
            "lessons": [
                {
                    "lesson_id": 1,
                    "topic": "Introduction to Pydantic"
                },
                {
                    "lesson_id": 2,
                    "topic": "BaseModel"
                }
            ]
        }
    ]
}
```

Pydantic automatically serializes the entire nested structure.

---

## Convert Nested Model to JSON

Use:

```python
print(course.model_dump_json(indent=2))
```

Example output:

```json
{
  "course_id": 101,
  "title": "Python for Agentic AI",
  "modules": [
    {
      "module_id": 1,
      "name": "Pydantic Fundamentals",
      "lessons": [
        {
          "lesson_id": 1,
          "topic": "Introduction to Pydantic"
        },
        {
          "lesson_id": 2,
          "topic": "BaseModel"
        }
      ]
    }
  ]
}
```

This is especially useful when sending structured data through APIs.

---

## Validation Example

Consider invalid nested data:

```python
course = Course(
    course_id=101,
    title="Python for Agentic AI",
    modules=[
        {
            "module_id": "invalid",
            "name": "Pydantic Fundamentals",
            "lessons": [
                {
                    "lesson_id": 1,
                    "topic": "BaseModel"
                }
            ]
        }
    ]
)
```

The field:

```python
module_id: int
```

expects an integer.

But the provided value is:

```python
"invalid"
```

Pydantic automatically raises a validation error.

---

## Handling Nested Validation Errors

```python
from pydantic import ValidationError

try:
    course = Course(
        course_id=101,
        title="Python for Agentic AI",
        modules=[
            {
                "module_id": "invalid",
                "name": "Pydantic Fundamentals",
                "lessons": [
                    {
                        "lesson_id": 1,
                        "topic": "BaseModel"
                    }
                ]
            }
        ]
    )

except ValidationError as error:
    print(error)
```

Pydantic identifies exactly where the invalid data exists inside the nested structure.

---

## Complete Practice Example

```python
from pydantic import BaseModel
from typing import List


class Lesson(BaseModel):
    lesson_id: int
    topic: str


class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]


class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]


course = Course(
    course_id=101,
    title="Python for Agentic AI",
    modules=[
        Module(
            module_id=1,
            name="Pydantic Fundamentals",
            lessons=[
                Lesson(
                    lesson_id=1,
                    topic="Introduction to Pydantic"
                ),
                Lesson(
                    lesson_id=2,
                    topic="BaseModel"
                ),
                Lesson(
                    lesson_id=3,
                    topic="Field Validation"
                )
            ]
        ),
        Module(
            module_id=2,
            name="Advanced Pydantic",
            lessons=[
                Lesson(
                    lesson_id=4,
                    topic="Computed Fields"
                ),
                Lesson(
                    lesson_id=5,
                    topic="Nested Models"
                )
            ]
        )
    ]
)


print(course)

print("\nCourse Title:")
print(course.title)

print("\nModules and Lessons:")

for module in course.modules:
    print(f"\nModule: {module.name}")

    for lesson in module.lessons:
        print(f"- {lesson.topic}")


print("\nDictionary Output:")
print(course.model_dump())


print("\nJSON Output:")
print(course.model_dump_json(indent=2))
```

---

## Key Concepts Learned

### `BaseModel`

Used to create Pydantic models.

```python
class Lesson(BaseModel):
    ...
```

---

### Nested Models

One Pydantic model can contain another Pydantic model.

Example:

```python
lessons: List[Lesson]
```

Here, the `Module` model contains multiple `Lesson` models.

---

### Lists of Models

Pydantic supports lists containing model objects.

```python
modules: List[Module]
```

This means the `Course` contains multiple modules.

---

### Automatic Parsing

Pydantic can automatically convert nested dictionaries into model objects.

```text
dict
 ↓
Course
 ↓
Module
 ↓
Lesson
```

---

### Automatic Validation

Every nested level is validated.

```text
Course validation
    ↓
Module validation
    ↓
Lesson validation
```

If any nested value is invalid, Pydantic raises a validation error.

---

## Modern Python Alternative

In modern Python versions, the same model can be written using built-in generic types:

```python
from pydantic import BaseModel


class Lesson(BaseModel):
    lesson_id: int
    topic: str


class Module(BaseModel):
    module_id: int
    name: str
    lessons: list[Lesson]


class Course(BaseModel):
    course_id: int
    title: str
    modules: list[Module]
```

Instead of:

```python
from typing import List
```

and:

```python
List[Lesson]
```

we can use:

```python
list[Lesson]
```

Since I am learning modern Python for backend development and Agentic AI, the `list[Lesson]` syntax is useful to know.

---

## Real-World Use Cases

Nested models are useful for representing structured data such as:

### E-Learning Platforms

```text
Course
 └── Module
      └── Lesson
```

### E-Commerce Applications

```text
Order
 └── Order Items
      └── Product
```

### Social Media Applications

```text
User
 └── Posts
      └── Comments
```

### Company Systems

```text
Company
 └── Departments
      └── Employees
```

### AI Agent Systems

```text
Agent
 └── Tools
      └── Parameters
```

---

## Why This Matters for Agentic AI

Nested models are highly relevant to Agentic AI because agents frequently work with deeply structured data.

For example:

```python
class ToolParameter(BaseModel):
    name: str
    type: str


class Tool(BaseModel):
    name: str
    parameters: list[ToolParameter]


class Agent(BaseModel):
    name: str
    tools: list[Tool]
```

This creates the structure:

```text
Agent
 └── Tools
      └── Parameters
```

Pydantic validates the complete hierarchy before the data is used by an AI system.

Nested models are commonly useful for:

* Structured LLM outputs
* Tool calling
* API request bodies
* API responses
* Agent configuration
* Workflow definitions
* Multi-agent systems

---

## Project Structure

```text
Pydantic/
│
├── nested_models.py
└── README.md
```

---

## Installation

Install Pydantic using `pip`:

```bash
pip install pydantic
```

Or using `uv`:

```bash
uv add pydantic
```

---

## Run the Program

Using Python:

```bash
python nested_models.py
```

Using `uv`:

```bash
uv run nested_models.py
```

---

## Learning Outcome

After completing this exercise, I can:

* Create multiple Pydantic models
* Connect models using nested relationships
* Use `List` with Pydantic models
* Create lists of nested objects
* Understand hierarchical data structures
* Validate nested data automatically
* Convert dictionaries into nested Pydantic objects
* Access deeply nested fields
* Iterate through nested models
* Serialize nested models using `model_dump()`
* Convert nested models into JSON
* Understand real-world uses of nested data structures

---

## Conclusion

This exercise helped me understand how **Nested Models work in Pydantic**.

The final structure is:

```text
Course
  └── List[Module]
        └── List[Lesson]
```

The most important concept learned is that Pydantic can automatically validate, parse, and serialize complete hierarchical data structures.

This is especially useful when working with REST APIs, FastAPI, structured LLM outputs, tool calling, and Agentic AI systems.
