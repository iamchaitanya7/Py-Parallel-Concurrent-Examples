import multiprocessing
import os
import time

def task1():
    print("Executing the First Task...")
    print("PID of Task 1 process is: ", os.getpid())


def task2():
    print("Executing the Second Task...")
    print("PID of Task 2 process is: ", os.getpid())


def task3():
    print("Executing the Third Task...")
    print("PID of Task 3 process is: ", os.getpid())

def main():
    print("Multiprocessing Demonstration")
    print("PID of Parent process is: ", os.getppid())
    print("PID of Running process is: ", os.getpid())

    task1()
    task2()
    task3()

if __name__ == "__main__":
    main()