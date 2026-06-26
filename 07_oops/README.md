# 📘 Python Object-Oriented Programming (OOP)

This directory contains beginner-friendly Python exercises focused on **Object-Oriented Programming (OOP)**. Each exercise introduces an important OOP concept through practical implementation.

## 📂 Directory Structure

```
07_oop/
├── 01_basic_class_object.py
├── 02_class_method_self.py
├── 03_inheritance.py
├── 04_encapsulation.py
├── 05_polymorphism.py
├── 06_class_variables.py
├── 07_static_method.py
├── 08_property_decorator.py
├── 09_isinstance_inheritance.py
├── 10_multiple_inheritance.py
└── README.md
```

---

## 🚀 Problems Covered

### 1. Basic Class and Object
**File:** `01_basic_class_object.py`

Create a `Car` class with attributes like `brand` and `model`. Then create an instance of this class.

---

### 2. Class Method and Self
**File:** `02_class_method_self.py`

Add a method to the `Car` class that displays the full name of the car (brand and model).

---

### 3. Inheritance
**File:** `03_inheritance.py`

Create an `ElectricCar` class that inherits from the `Car` class and has an additional attribute `battery_size`.

---

### 4. Encapsulation
**File:** `04_encapsulation.py`

Modify the `Car` class to encapsulate the `brand` attribute, making it private, and provide a getter method for it.

---

### 5. Polymorphism
**File:** `05_polymorphism.py`

Demonstrate polymorphism by defining a method `fuel_type()` in both `Car` and `ElectricCar` classes, but with different behaviors.

---

### 6. Class Variables
**File:** `06_class_variables.py`

Add a class variable to `Car` that keeps track of the number of cars created.

---

### 7. Static Method
**File:** `07_static_method.py`

Add a static method to the `Car` class that returns a general description of a car.

---

### 8. Property Decorators
**File:** `08_property_decorator.py`

Use a property decorator in the `Car` class to make the `model` attribute read-only.

---

### 9. Class Inheritance and `isinstance()`
**File:** `09_isinstance_inheritance.py`

Demonstrate the use of `isinstance()` to check if `my_tesla` is an instance of both `Car` and `ElectricCar`.

---

### 10. Multiple Inheritance
**File:** `10_multiple_inheritance.py`

Create two classes, `Battery` and `Engine`, and let the `ElectricCar` class inherit from both, demonstrating multiple inheritance.

---

## 📚 OOP Concepts Covered

- Classes and Objects
- Instance Attributes
- Methods and `self`
- Constructors (`__init__`)
- Inheritance
- Encapsulation
- Polymorphism
- Class Variables
- Static Methods
- Property Decorators (`@property`)
- `isinstance()` Function
- Multiple Inheritance

---

## 🎯 Learning Objectives

After completing these exercises, you will be able to:

- Create classes and objects.
- Define instance attributes and methods.
- Understand the role of `self`.
- Reuse code with inheritance.
- Protect data using encapsulation.
- Implement polymorphism.
- Work with class variables.
- Create utility methods using `@staticmethod`.
- Use property decorators to control attribute access.
- Check object types with `isinstance()`.
- Apply multiple inheritance in Python.

---

## ▶️ Running an Exercise

```bash
python 01_basic_class_object.py
```

Replace the filename with any exercise you want to run.

---

## 🛠 Requirements

- Python 3.x

---

Happy Coding! 🚀