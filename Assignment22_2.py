#Calculate Factorial of multiple using pool map()
import multiprocessing
import os

def Fact(Num):
    if Num == 0 or Num == 1:
       return 1
    else:
       return Num * Fact(Num - 1)

def main():
    IList = []
    Length = int(input("Enter length of a list : "))

    for i in range(Length):
        No = int(input("Enter a Element : "))
        IList.append(No)
        
    pObj = multiprocessing.Pool()
    Res = pObj.map(Fact,IList)
    pObj.close()
    pObj.join()

    print("List of input is :", IList)
    print("PID is :", os.getpid())
    print("Factorial is :", Res)



if __name__ == "__main__":
    main()