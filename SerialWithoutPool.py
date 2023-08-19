# Single core assignment of work/task demo without pooling

import time

def square(no):
    return no * no

def main():
    arr = [10,20,30,40]
    Result = []
    starttime = time.time()
    for val in arr:
        Ans = square(val)
        Result.append(Ans)
    print(Result)
    endtime = time.time()
    print("Required Time: ", endtime - starttime)

if __name__ == "__main__":
    main()