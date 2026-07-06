# Pydantic Computed Fields

This section contains my notes and practice code for learning **Computed Fields in Pydantic v2**.

The goal of this exercise is to understand how to create a field whose value is automatically calculated from other fields in a Pydantic model.

In this example, I created a `Booking` model where the `total_amount` is automatically calculated using:

```text
total_amount = nights × rate_per_night
```

---

## Topics Covered

* Pydantic `BaseModel`
* Pydantic `Field`
* Field Constraints
* `computed_field`
* Python `@property`
* Automatic Calculated Fields
* Type Hints
* Model Serialization
* Pydantic v2

---

## Booking Model Requirements

The `Booking` model contains the following fields:

| Field            | Type    | Required | Validation                           |
| ---------------- | ------- | -------- | ------------------------------------ |
| `user_id`        | `int`   | Yes      | Must be an integer                   |
| `room_id`        | `int`   | Yes      | Must be an integer                   |
| `nights`         | `int`   | Yes      | Must be greater than or equal to `1` |
| `rate_per_night` | `float` | Yes      | Must be a numeric value              |
| `total_amount`   | `float` | Computed | Automatically calculated             |

---

## Project Code

```python
from pydantic import BaseModel, Field, computed_field


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
```

---

## Understanding `BaseModel`

The `Booking` class inherits from Pydantic's `BaseModel`.

```python
class Booking(BaseModel):
    ...
```

This provides features such as:

* Automatic data validation
* Type checking
* Data parsing
* Serialization
* JSON conversion
* JSON Schema generation

---

## Understanding `Field`

The `nights` field is defined as:

```python
nights: int = Field(..., ge=1)
```

Here:

* `int` means the value should be an integer
* `...` means the field is required
* `ge=1` means greater than or equal to `1`

Therefore:

```text
nights >= 1
```

---

## Valid Nights

The following values are valid:

```python
nights=1
```

```python
nights=5
```

```python
nights=10
```

---

## Invalid Nights

The following value is invalid:

```python
nights=0
```

It fails validation because the minimum allowed value is `1`.

A negative value is also invalid:

```python
nights=-2
```

Pydantic automatically raises a validation error.

---

## Understanding `computed_field`

Pydantic v2 provides the `@computed_field` decorator for fields whose values are calculated from other model fields.

In this model:

```python
@computed_field
@property
def total_amount(self) -> float:
    return self.nights * self.rate_per_night
```

The `total_amount` is not entered manually.

Instead, it is automatically calculated from:

```text
nights × rate_per_night
```

---

## Understanding `@property`

The `@property` decorator allows a method to be accessed like a normal attribute.

Without `@property`, a method is called using:

```python
booking.total_amount()
```

With `@property`, it can be accessed using:

```python
booking.total_amount
```

This makes the computed value behave like a regular field.

---

## Why Use Both Decorators?

The model uses:

```python
@computed_field
@property
def total_amount(self) -> float:
    ...
```

Each decorator has a different role.

### `@property`

Makes the method accessible like an attribute:

```python
booking.total_amount
```

### `@computed_field`

Tells Pydantic to treat the property as a computed model field.

This means it can be included during model serialization.

---

## Creating a Booking

Example:

```python
booking = Booking(
    user_id=101,
    room_id=501,
    nights=3,
    rate_per_night=2500
)

print(booking)
```

Example output:

```text
user_id=101 room_id=501 nights=3 rate_per_night=2500.0 total_amount=7500.0
```

The calculation is:

```text
3 × 2500 = 7500
```

Therefore:

```text
total_amount = 7500
```

---

## Example Using My Name

```python
booking = Booking(
    user_id=77,
    room_id=201,
    nights=4,
    rate_per_night=1800
)

print(booking)
```

Calculation:

```text
4 × 1800 = 7200
```

Result:

```text
total_amount = 7200
```

This booking example represents my Pydantic practice as **Rahul Jharwal**.

---

## Accessing the Computed Field

The computed value can be accessed directly:

```python
print(booking.total_amount)
```

Example output:

```text
7200.0
```

There is no need to call it like a function:

```python
booking.total_amount()
```

Instead, use:

```python
booking.total_amount
```

because `@property` makes it behave like an attribute.

---

## Model Serialization

Pydantic v2 provides `model_dump()` to convert a model into a Python dictionary.

Example:

```python
booking = Booking(
    user_id=77,
    room_id=201,
    nights=4,
    rate_per_night=1800
)

print(booking.model_dump())
```

Example output:

```python
{
    "user_id": 77,
    "room_id": 201,
    "nights": 4,
    "rate_per_night": 1800.0,
    "total_amount": 7200.0
}
```

Notice that the computed field is included:

```python
"total_amount": 7200.0
```

---

## Convert Model to JSON

The model can also be converted into JSON:

```python
print(booking.model_dump_json())
```

Example output:

```json
{
    "user_id": 77,
    "room_id": 201,
    "nights": 4,
    "rate_per_night": 1800.0,
    "total_amount": 7200.0
}
```

The computed field is automatically included in the serialized output.

---

## Validation Error Example

Consider this booking:

```python
booking = Booking(
    user_id=77,
    room_id=201,
    nights=0,
    rate_per_night=1800
)
```

This is invalid because:

```text
nights >= 1
```

But the provided value is:

```text
nights = 0
```

Pydantic automatically raises a `ValidationError`.

---

## Handling Validation Errors

```python
from pydantic import ValidationError

try:
    booking = Booking(
        user_id=77,
        room_id=201,
        nights=0,
        rate_per_night=1800
    )

except ValidationError as error:
    print(error)
```

This allows invalid booking data to be handled safely.

---

## Complete Practice Example

```python
from pydantic import BaseModel, Field, computed_field


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night


booking = Booking(
    user_id=77,
    room_id=201,
    nights=4,
    rate_per_night=1800
)

print(booking)

print("Total Amount:", booking.total_amount)

print(booking.model_dump())

print(booking.model_dump_json())
```

---

## Expected Output

```text
user_id=77 room_id=201 nights=4 rate_per_night=1800.0 total_amount=7200.0

Total Amount: 7200.0

{
    'user_id': 77,
    'room_id': 201,
    'nights': 4,
    'rate_per_night': 1800.0,
    'total_amount': 7200.0
}
```

---

## Key Concepts Learned

### `BaseModel`

Used to create a Pydantic model.

```python
class Booking(BaseModel):
    ...
```

---

### `Field`

Used to add validation rules and constraints.

```python
nights: int = Field(..., ge=1)
```

---

### `ge`

Means:

```text
greater than or equal to
```

Example:

```python
ge=1
```

means:

```text
value >= 1
```

---

### `computed_field`

Used to create a field whose value is automatically calculated.

```python
@computed_field
```

---

### `property`

Allows a method to behave like an attribute.

```python
@property
```

---

### Return Type Hint

The computed field includes:

```python
def total_amount(self) -> float:
```

The `-> float` indicates that the method returns a floating-point number.

---

## Real-World Use Cases

Computed fields are useful when values depend on other fields.

Examples include:

### Hotel Booking

```text
total_amount = nights × rate_per_night
```

### E-commerce

```text
total_price = quantity × price
```

### Employee Salary

```text
annual_salary = monthly_salary × 12
```

### Shopping Cart

```text
final_price = subtotal + tax - discount
```

### Loan Calculation

```text
total_payment = principal + interest
```

---

## Why This Matters for Agentic AI

In Agentic AI applications, data often needs to be validated and transformed before being passed between:

* LLMs
* Tools
* APIs
* Databases
* External services

For example:

```python
class ToolCost(BaseModel):
    tokens_used: int
    price_per_token: float

    @computed_field
    @property
    def total_cost(self) -> float:
        return self.tokens_used * self.price_per_token
```

An AI agent can provide the raw values:

```text
tokens_used
price_per_token
```

and the application automatically calculates:

```text
total_cost
```

This helps keep derived values consistent and reduces manual calculations.

---

## Project Structure

```text
Pydantic/
│
├── booking.py
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
python booking.py
```

Using `uv`:

```bash
uv run booking.py
```

---

## Learning Outcome

After completing this exercise, I can:

* Create Pydantic models using `BaseModel`
* Add field constraints using `Field`
* Validate minimum numeric values
* Use `@property`
* Create computed fields using `@computed_field`
* Calculate values automatically from other model fields
* Access computed values like normal attributes
* Serialize computed fields using `model_dump()`
* Convert Pydantic models to JSON
* Understand practical use cases for computed fields

---

## Conclusion

This exercise helped me understand how **computed fields work in Pydantic v2**.

The `Booking` model validates booking data and automatically calculates:

```text
total_amount = nights × rate_per_night
```

The main concept learned in this section is how `@computed_field` and `@property` work together to create automatically calculated fields that can also be included in serialized Pydantic model output.
