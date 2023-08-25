import multiprocessing
import os
#import time

def task1(value):
    print("Executing the First Task...")
    for i in range(value):
        print("Task1: ",i)


def task2(value):
    print("Executing the Second Task...")
    for i in range(value):
        print("Task2: ",i)

def main():
    print("Multiprocessing Demonstration")

    no1 = 5
    no2 = 8

    p1 = multiprocessing.Process(target = task1 , args = (no1,))  #we directly include the function of task1 into the process function to perform multiprocessing
    p2 = multiprocessing.Process(target = task2 , args = (no2,))  

    p1.start() #parallel exceution of process
    p2.start()
    
    p1.start() #serial exceution of process
    p1.join()

    p2.start()
    p2.join()

if __name__ == "__main__":
    main()