import threading
import EvenFactLib20_2
import OddFactLib20_2

def main():
    Value = int(input("Enter a number : "))

    t1 = threading.Thread(target=EvenFactLib20_2.EvenFactor, args=(Value,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactLib20_2.OddFactor, args=(Value,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Thread one is :", t1.name)
    print("Thread two is :", t2.name)
    print("Exit from main")

if __name__ == "__main__":
    main()


