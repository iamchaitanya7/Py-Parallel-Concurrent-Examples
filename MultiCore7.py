import os
import threading

def task1(val):
    print("PID of Task1 is: ", os.getpid())      #pid is same as running process pid 

def task2(val):
    print("PID of Task2 is: ", os.getpid())      #pid is same as running process pid 


def main():
    print("PID of Parent Process is: ", os.getppid())   #actual pid of current process which in our case is cmd process

    print("PID of Parent Process is: ", os.getpid())    #running process pid 
    no = 5
    t1 = threading.Thread(target = task1, args =(no,))
    t2 = threading.Thread(target = task2, args =(no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()