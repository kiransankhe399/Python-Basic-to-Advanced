#Calculate Count prime number in list using pool map()
import multiprocessing
import os

def Prime(IList):
    Count = 0

    for No in IList:
        if No <= 1:
            continue

        IsPrime = True

        for i in range(2, No):
            if No % i == 0:
                IsPrime = False
                break

        if IsPrime:
            Count += 1

    return Count

def main():
    IList = []
    Length = int(input("Enter length of a list : "))

    for i in range(Length):
        No = int(input("Enter a Element : "))
        IList.append(No)
        
    pObj = multiprocessing.Pool()
    Res = pObj.map(Prime,IList)
    pObj.close()
    pObj.join()

    print("List of input is :", IList)
    print("PID is :", os.getpid())
    print("Factorial is :", Res)


if __name__ == "__main__":
    main()