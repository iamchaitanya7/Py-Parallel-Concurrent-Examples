#Demo of Serial Execution or Processing using Pool Method/Class

import time
import multiprocessing

def fun(no):
    sum = 0
    for i in range(10000):
        sum = sum + (no*no)
    return sum

def main():
    print("Demo of Serial execution using Single Core")
    
    starttime = time.time()
    p = multiprocessing.Pool()

    Result = []
    
    Result = p.map(fun, range(10000))
    p.close()
    p.join()
    endtime = time.time()
    print("Required Time: ", endtime - starttime)

if __name__ == "__main__":
    main()
