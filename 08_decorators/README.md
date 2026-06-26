# 📘 Python Decorators

This directory contains beginner-friendly exercises to learn **Python Decorators**. Decorators allow you to extend or modify the behavior of functions without changing their original source code.

---

## 📂 Directory Structure

```
08_decorators/
├── 01_execution_timer.py
├── 02_debug_function_calls.py
├── 03_cache_return_values.py
└── README.md
```

---

## 🚀 Problems Covered

### 1. Timing Function Execution
**File:** `01_execution_timer.py`

Write a decorator that measures the time a function takes to execute.

---

### 2. Debugging Function Calls
**File:** `02_debug_function_calls.py`

Create a decorator to print the function name and the values of its arguments every time the function is called.

---

### 3. Cache Return Values
**File:** `03_cache_return_values.py`

Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

---

## 📚 Concepts Covered

- Introduction to Decorators
- Higher-Order Functions
- Nested Functions
- Wrapper Functions
- `*args` and `**kwargs`
- Function Execution Timing
- Debugging with Decorators
- Function Result Caching
- Improving Performance with Memoization
- Preserving Function Metadata (`functools.wraps`)

---

## 🎯 Learning Objectives

After completing these exercises, you will be able to:

- Understand what decorators are and why they are useful.
- Create custom decorators in Python.
- Wrap existing functions without modifying their implementation.
- Accept arbitrary positional and keyword arguments using `*args` and `**kwargs`.
- Measure function execution time.
- Log and debug function calls.
- Cache function results to improve performance.

---

## ▶️ Running an Exercise

```bash
python 01_execution_timer.py
```

Replace the filename with any exercise you want to run.

---

## 🛠 Prerequisites

- Python 3.x
- Basic understanding of:
  - Functions
  - `*args` and `**kwargs`
  - Nested functions

---

## 📖 What is a Decorator?

A **decorator** is a function that takes another function as input, adds extra functionality, and returns a new function without modifying the original function.

Decorators are commonly used for:

- Logging
- Authentication
- Performance measurement
- Caching (Memoization)
- Input validation
- Access control
- Debugging

---

Happy Coding! 🚀