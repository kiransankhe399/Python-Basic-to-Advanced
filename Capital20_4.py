import threading

def Capital(Char):
    print("TID of Capital thread is: ", threading.get_ident()) 
    print("Thread Name:", threading.current_thread().name)


    Count = len(Char)
    UpperCount = 0

    for ch in Char:
        if ch.isupper():
            UpperCount += 1

    print(f"Total Count of {Char} is : ", Count)
    print(f"Total number of Upper case in {Char} is : ", UpperCount)

    return UpperCount