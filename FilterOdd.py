#lambda function using filter returns odd of list

Odd = lambda No : No % 2 != 0

def main():
    ListX = [2,3,4,5,6,7]
    #Res = Square(ListX)
    MData = list(filter(Odd,ListX))
    print(MData)

if __name__ == "__main__":
    main()

