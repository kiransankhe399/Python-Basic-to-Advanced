import Small20_4
import Capital20_4
import Digits20_4
import threading

def main():
    Str = input("Enter a String : ")

    t1 = threading.Thread(target=Small20_4.Small, args=(Str,), name = "Small")
    t2 = threading.Thread(target=Capital20_4.Capital, args=(Str,), name = "Capital")
    t3 = threading.Thread(target=Digits20_4.Digits, args=(Str,), name = "Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Thread one",t1.name)
    print("Thread two",t2.name)
    print("Thread three",t3.name)

if __name__ == "__main__":
    main()