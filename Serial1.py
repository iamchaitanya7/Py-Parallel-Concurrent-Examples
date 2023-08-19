#Demo to of Serial Execution or Processing using a Single Core checking the processing speed

def fun(no):
    sum = 0
    for i in range(10000):
        sum = sum + (no*no)
    return sum

def main():
    print("Demo of Serial execution using Single Core")
    Result = []
    for no in range(10000):
        Result.append(fun(no))

if __name__ == "__main__":
    main()