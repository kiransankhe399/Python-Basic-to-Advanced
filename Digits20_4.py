import threading

def Digits(Char):
    print("TID of Digits thread is: ", threading.get_ident()) 
    print("Thread Name:", threading.current_thread().name)

    
    DigitCount = 0


    for i in Char:
        if i.isdigit():
            DigitCount += 1

    print(f"Total digits in {Char}", DigitCount)
    return DigitCount

