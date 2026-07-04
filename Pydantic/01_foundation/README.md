# 📦 Pydantic BaseModel – Product Model

This project demonstrates how to create a simple **data model** in Python using **Pydantic's `BaseModel`**.

## 📚 What I Learned

In this example, I learned:

* How to import `BaseModel` from Pydantic
* How to create a Pydantic model
* How to define typed fields
* How to define required fields
* How to define default values
* How Pydantic validates data

---

## 🧩 Code Example

```python
from pydantic import BaseModel  # type: ignore


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True
```

---

## 🔍 Understanding the Code

### 1. Import `BaseModel`

```python
from pydantic import BaseModel
```

`BaseModel` is the base class provided by Pydantic.

By inheriting from `BaseModel`, our Python class gets features such as:

* Data validation
* Type checking
* Automatic type conversion
* Default values
* Serialization

---

## 2. Create the `Product` Model

```python
class Product(BaseModel):
```

Here, the `Product` class inherits from `BaseModel`.

This means `Product` becomes a **Pydantic model**.

---

## 3. Define Model Fields

```python
id: int
name: str
price: float
in_stock: bool = True
```

Each field has a specific type.

| Field      | Type    | Required? | Default Value |
| ---------- | ------- | --------- | ------------- |
| `id`       | `int`   | Yes       | None          |
| `name`     | `str`   | Yes       | None          |
| `price`    | `float` | Yes       | None          |
| `in_stock` | `bool`  | No        | `True`        |

---

## ✅ Required Fields

The following fields are required:

```python
id: int
name: str
price: float
```

When creating a `Product` object, values for these fields must be provided.

Example:

```python
product = Product(
    id=1,
    name="Laptop",
    price=59999.99
)
```

---

## 🟢 Default Values

The `in_stock` field has a default value:

```python
in_stock: bool = True
```

This means if no value is provided, Pydantic automatically uses:

```python
True
```

Example:

```python
product = Product(
    id=1,
    name="Laptop",
    price=59999.99
)

print(product)
```

Output:

```text
id=1 name='Laptop' price=59999.99 in_stock=True
```

---

## 🔴 Override the Default Value

We can explicitly set `in_stock=False`.

```python
product = Product(
    id=2,
    name="Mouse",
    price=799.0,
    in_stock=False
)

print(product)
```

Output:

```text
id=2 name='Mouse' price=799.0 in_stock=False
```

---

## 🛡️ Data Validation

Pydantic validates input data based on the declared field types.

For example:

```python
product = Product(
    id="invalid",
    name="Keyboard",
    price=1499.99
)
```

Since `id` should be an integer:

```python
id: int
```

Pydantic raises a validation error because `"invalid"` cannot be converted into an integer.

---

## 🔄 Automatic Type Conversion

Pydantic can convert compatible values into the required type.

Example:

```python
product = Product(
    id="1",
    name="Laptop",
    price="59999.99"
)

print(product)
```

Pydantic can convert:

```text
"1" → 1
"59999.99" → 59999.99
```

So the validated object contains the correct Python types.

---

## 📤 Convert Model to Dictionary

A Pydantic model can be converted into a Python dictionary.

```python
product = Product(
    id=1,
    name="Laptop",
    price=59999.99
)

print(product.model_dump())
```

Example output:

```python
{
    "id": 1,
    "name": "Laptop",
    "price": 59999.99,
    "in_stock": True
}
```

---

## 📤 Convert Model to JSON

A Pydantic model can also be converted into JSON.

```python
product = Product(
    id=1,
    name="Laptop",
    price=59999.99
)

print(product.model_dump_json())
```

Example output:

```json
{
    "id": 1,
    "name": "Laptop",
    "price": 59999.99,
    "in_stock": true
}
```

---

## 🧠 Key Concepts

### Pydantic Model

A Pydantic model is a Python class that inherits from `BaseModel`.

```python
class Product(BaseModel):
    ...
```

---

### Type Annotations

Type annotations define the expected data type.

```python
id: int
name: str
price: float
```

---

### Required Field

A field without a default value is required.

```python
id: int
```

---

### Optional Input Through Default Value

A field with a default value does not need to be provided during object creation.

```python
in_stock: bool = True
```

---

### Validation

Pydantic checks whether input data matches the declared field types.

```python
id: int
```

---

### Serialization

Pydantic models can be converted into formats such as:

* Python dictionaries
* JSON strings

Using:

```python
product.model_dump()
product.model_dump_json()
```

---

## 📁 Suggested Project Structure

```text
pydantic-product-model/
│
├── main.py
└── README.md
```

---

## 🚀 Installation

Install Pydantic using pip:

```bash
pip install pydantic
```

Check the installed version:

```bash
pip show pydantic
```

---

## ▶️ Run the Program

```bash
python main.py
```

---

## 🎯 Complete Example

```python
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product = Product(
    id=1,
    name="Laptop",
    price=59999.99
)

print(product)
print(product.model_dump())
print(product.model_dump_json())
```

---

## 📝 Summary

In this example, I learned how to:

* Create a Pydantic model using `BaseModel`
* Define fields using Python type annotations
* Understand required fields
* Set default values
* Create model objects
* Validate input data
* Use automatic type conversion
* Convert models to dictionaries
* Convert models to JSON

This is a foundational concept for working with **Pydantic**, **FastAPI**, API request validation, response schemas, and structured Python applications.
