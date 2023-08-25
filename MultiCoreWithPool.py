# multi core assignment of work/task demo with pooling
import multiprocessing
import time
def square(no):
    return no * no

def main():
    arr = [10,20,30,40]
    Result = []
    starttime = time.time()
    p = multiprocessing.Pool()
    Result = p.map(square, arr)
    p.close()
    p.join()
    print(Result)
    endtime = time.time()
    print("Required Time: ", endtime - starttime)

if __name__ == "__main__":
    main()