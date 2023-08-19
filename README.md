# - Python Parallel and Concurrent Examples...!

Python offers various techniques for parallel and concurrent programming, allowing you to execute multiple tasks simultaneously. Let's explore some key concepts and examples.

## - Single Core Execution : 

In a single-core environment, tasks are executed sequentially. One task must complete before another begins. This limits performance and efficiency.

```python
import time

def task(name):
    print(f"Starting task: {name}")
    time.sleep(2)
    print(f"Completed task: {name}")

if __name__ == "__main__":
    tasks = ["Task1", "Task2", "Task3"]
    for task_name in tasks:
        task(task_name)
```

## - MultiCore Execution :

In a multi-core environment, tasks can run simultaneously on different CPU cores, improving performance. Python's multiprocessing and multithreading modules help achieve this.

```python
import multiprocessing
import time

def task(name):
    print(f"Starting task: {name}")
    time.sleep(2)
    print(f"Completed task: {name}")

if __name__ == "__main__":
    tasks = ["Task1", "Task2", "Task3"]
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(task, tasks)
```

## - Multitasking :

Multitasking involves running multiple tasks concurrently, even if only one CPU core is available. Python's cooperative multitasking, using generators or async/await syntax, enables efficient task switching.

## - Multiprocessing :

Python's `multiprocessing` module allows running multiple processes in separate memory spaces, leveraging multiple CPU cores. Each process has its own Python interpreter and memory space.

Example:

```python
import multiprocessing

def worker(task):
    print(f"Working on task {task}")

if __name__ == "__main__":
    tasks = ["Task1", "Task2", "Task3"]
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(worker, tasks)
```


## - Multithreading :
Python's threading module enables multithreading, where multiple threads share the same memory space but execute different tasks concurrently. However, due to the Global Interpreter Lock (GIL), true parallelism is limited.

```python
import threading

def worker(task):
    print(f"Working on task {task}")

if __name__ == "__main__":
    tasks = ["Task1", "Task2", "Task3"]
    threads = [threading.Thread(target=worker, args=(task,)) for task in tasks]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
```
