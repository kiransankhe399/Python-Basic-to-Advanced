import threading
import EvenThreadLib20_1
import OddThreadLib20_1

def main():
    Value = int(input("Enter a number : "))
    t1 = threading.Thread(target=EvenThreadLib20_1.Even, args=(Value,), name="Even Thread")
    t2 = threading.Thread(target=OddThreadLib20_1.Odd, args=(Value,), name="Odd Thread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Thread one is :", t1.name)
    print("Thread two is :", t2.name)


if __name__ == "__main__":
    main()


