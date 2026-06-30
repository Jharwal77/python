# Python Async Programming

This repository contains my notes and practice code for learning **Asynchronous Programming in Python** using the `asyncio` module.

The goal of this section is to understand how Python executes asynchronous code, how coroutines work, and how to run multiple tasks concurrently.

---

# Topics Covered

- Synchronous vs Asynchronous Programming
- Coroutines
- Async Event Loop
- `async` and `await` Keywords
- Creating and Managing Tasks
- Practical Async Example

---

# 1. Synchronous vs Asynchronous

## Synchronous Programming

In synchronous programming, the program executes one task at a time.

- Every line waits for the previous line to finish.
- If one task takes a long time, the entire program waits.

### Example

```python
import time

def work():
    print("Task Started")
    time.sleep(3)
    print("Task Finished")

work()
print("Done")
```

Execution Flow

```
Start
 ↓
Task Starts
 ↓
Wait 3 seconds
 ↓
Task Ends
 ↓
Done
```

### Advantages

- Easy to understand
- Simple debugging

### Disadvantages

- Wastes time while waiting
- Poor performance for I/O operations

---

## Asynchronous Programming

Asynchronous programming allows multiple tasks to make progress without blocking the entire program.

Instead of waiting, Python switches to another task whenever one task is waiting.

This is ideal for:

- API requests
- File operations
- Database queries
- Web scraping
- Chat applications

---

# 2. Coroutines

A coroutine is a special function that can pause and resume execution.

Coroutines are created using the `async def` keyword.

Example:

```python
import asyncio

async def greet():
    print("Hello")
```

Unlike normal functions, calling a coroutine does not execute it immediately.

```python
greet()
```

This only creates a coroutine object.

To execute it:

```python
asyncio.run(greet())
```

---

# 3. Async Event Loop

The Event Loop is the heart of asynchronous programming.

It continuously checks:

- Which task is ready?
- Which task is waiting?
- Which task should execute next?

Flow

```
Task 1
 ↓
Waiting?
 ↓ Yes
Switch to Task 2
 ↓
Waiting?
 ↓
Switch to Task 3
 ↓
Return when ready
```

Python provides the event loop through the `asyncio` module.

Example

```python
import asyncio

async def main():
    print("Running")

asyncio.run(main())
```

---

# 4. async and await Keywords

## async

Used to create a coroutine.

```python
async def download():
    print("Downloading")
```

---

## await

Used to pause the current coroutine until another coroutine completes.

Example

```python
import asyncio

async def task():
    await asyncio.sleep(2)
    print("Finished")
```

Here,

- `asyncio.sleep()` does not block the entire program.
- Only the current coroutine pauses.
- The event loop can execute other tasks.

---

# 5. Tasks

A Task allows multiple coroutines to run concurrently.

Without tasks:

```python
await task1()
await task2()
```

Execution:

```
Task 1
 ↓
Complete
 ↓
Task 2
```

---

With Tasks:

```python
t1 = asyncio.create_task(task1())
t2 = asyncio.create_task(task2())

await t1
await t2
```

Execution:

```
Task 1
Task 2
Running Together
```

Tasks improve efficiency for I/O-bound programs.

---

# 6. Async Example

Sequential Version

```python
import asyncio

async def work(name):
    print(f"{name} Started")
    await asyncio.sleep(2)
    print(f"{name} Finished")

async def main():
    await work("Task 1")
    await work("Task 2")

asyncio.run(main())
```

Output

```
Task 1 Started
Task 1 Finished
Task 2 Started
Task 2 Finished
```

Total Time

```
≈ 4 seconds
```

---

Concurrent Version

```python
import asyncio

async def work(name):
    print(f"{name} Started")
    await asyncio.sleep(2)
    print(f"{name} Finished")

async def main():
    task1 = asyncio.create_task(work("Task 1"))
    task2 = asyncio.create_task(work("Task 2"))

    await task1
    await task2

asyncio.run(main())
```

Output

```
Task 1 Started
Task 2 Started
Task 1 Finished
Task 2 Finished
```

Total Time

```
≈ 2 seconds
```

Both tasks execute concurrently instead of waiting for one another.

---

# Important asyncio Functions

| Function | Purpose |
|----------|---------|
| `asyncio.run()` | Starts the event loop |
| `async def` | Creates a coroutine |
| `await` | Waits without blocking the event loop |
| `asyncio.sleep()` | Non-blocking delay |
| `asyncio.create_task()` | Runs coroutines concurrently |
| `asyncio.gather()` | Executes multiple coroutines together |

---

# Key Takeaways

- Synchronous code executes one task at a time.
- Asynchronous code improves efficiency by handling waiting periods effectively.
- Coroutines are defined using `async def`.
- The Event Loop schedules and executes asynchronous tasks.
- `await` pauses only the current coroutine, not the whole program.
- Tasks enable concurrent execution.
- `asyncio` is Python's built-in library for asynchronous programming.
- Asynchronous programming is especially useful for I/O-bound applications such as APIs, networking, databases, and web scraping.

---

# Folder Structure

```
Async-Programming/
│
├── 01_sync_vs_async.py
├── 02_coroutines.py
├── 03_event_loop.py
├── 04_async_await.py
├── 05_tasks.py
├── 06_async_example.py
└── README.md
```

---

# Learning Outcome

After completing this section, I can:

- Explain the difference between synchronous and asynchronous programming.
- Write and execute coroutines.
- Understand how the asyncio event loop works.
- Use `async` and `await` effectively.
- Create concurrent tasks with `asyncio.create_task()`.
- Build efficient Python programs for I/O-bound operations using `asyncio`.