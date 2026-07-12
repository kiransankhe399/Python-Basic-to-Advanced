#Calculate of N number in list using pool map()
import multiprocessing
import os
import time

def Multiple(No):
    return sum(i**5 for i in range(1, No+1))

def main():
    IList = []
    Length = int(input("Enter length of a list : "))

    for i in range(Length):
        No = int(input("Enter a Element : "))
        IList.append(No)
        
    start_time = time.perf_counter()

    pObj = multiprocessing.Pool()
    Res = pObj.map(Multiple,IList)
    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print("List of input is :", IList)
    print("PID is :", os.getpid())
    print("Multiple is :", Res)
    print(f"Time required is : {end_time - start_time :.4f}Seconds")

if __name__ == "__main__":
    main()