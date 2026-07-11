#
import EvenListLib20_3
import OddListLib20_3
import threading

def main():
    IntList = []
    
    Length = int(input("Enter a Length of list : "))

    for i in range(Length):
        No = int(input("Enter element : "))
        IntList.append(No)
    
    t1 = threading.Thread(target = EvenListLib20_3.EvenList, args = (IntList,), name = "EvenList")
    t2 = threading.Thread(target = OddListLib20_3.OddList, args = (IntList,), name = "OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of Even List is ", t1.name)
    print("Sum of Odd List is ", t1.name)

    
if __name__ == "__main__":
    main()
