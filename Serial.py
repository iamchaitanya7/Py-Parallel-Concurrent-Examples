#Demo to of Serial Execution or Processing using a Single Core

def fun(no):
    sum = 0
    for i in range(10000):
        sum = sum + (no*no)
    return sum

def main():
    print("Demo of Serial execution using Single Core")
    #no = int(input())
    ret = fun(10)
    print(ret)

if __name__ == "__main__":
    main()