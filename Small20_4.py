#Count small case
import threading

def Small(Char):
    print("TID of Small thread is: ", threading.get_ident()) 
    print("Thread Name:", threading.current_thread().name)


    Count = len(Char)
    LowerCount = 0

    for ch in Char:
        if ch.islower():
            LowerCount += 1


    print(f"Total Count of {Char} is : ", Count)
    print(f"Total number of lower case in {Char} is : ", LowerCount)

    return LowerCount
