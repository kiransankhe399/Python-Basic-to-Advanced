import NumberReverse20_5
import NumberSeries20_5
import threading

def main():
    Str = int(input("Enter a Number : "))

    t1 = threading.Thread(target=NumberSeries20_5.NumSeries, args=(Str,), name = "NumSeries")
    t2 = threading.Thread(target=NumberReverse20_5.NumRev, args=(Str,), name = "NumRev")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Thread one :",t1.name)
    print("Thread two : ",t2.name)

if __name__ == "__main__":
    main()