import multiprocessing
import os
#import time

def task1(value):
    print("Executing the First Task...")
    print("PID of Task 1 Parent process is: ", os.getppid())
    print("PID of Task 1 process is: ", os.getpid())


def task2(value):
    print("Executing the Second Task...")
    print("PID of Task 2 Parent process is: ", os.getppid())
    print("PID of Task 2 process is: ", os.getpid())

def main():
    print("Multiprocessing Demonstration")
    print("PID of Parent process is: ", os.getppid())
    print("PID of Running process is: ", os.getpid())

    no = 5
    p1 = multiprocessing.Process(target = task1 , args = (no,))  #we directly include the function of task1 into the process function to perform multiprocessing
    p2 = multiprocessing.Process(target = task2 , args = (no,))  

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    #p1.close()
    #p2.close()

    #task1()
    #task2()

if __name__ == "__main__":
    main()