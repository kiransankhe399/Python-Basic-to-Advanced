#Sum of Even using pool map()
import multiprocessing
import os

def SumOdd(Num):
    Sum = 0
    for i in range(1, Num + 1):
        for j in range(1,i+1):
          if i%2 != 0:
            Sum = Sum + i 
    return Sum

def main():
    IList = []
    Length = int(input("Enter length of a list : "))

    for i in range(Length):
        No = int(input("Enter a Element : "))
        IList.append(No)
        
    pObj = multiprocessing.Pool()
    Res = pObj.map(SumOdd,IList)
    pObj.close()
    pObj.join()

    print("List of input is :", IList)
    print("PID is :", os.getpid())
    print("Factorial is :", Res)



if __name__ == "__main__":
    main()