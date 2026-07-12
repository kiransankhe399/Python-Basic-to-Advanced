#Sum of Even using pool map()
import multiprocessing
import os

def SumOdd(Num):
    k = (Num + 1) // 2  
    return k * k

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
    print("OddCount is :", Res)



if __name__ == "__main__":
    main()
