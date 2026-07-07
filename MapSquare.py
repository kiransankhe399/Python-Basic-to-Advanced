#lambda function using map returns square of list

Square = lambda No : No **2

#def Square(x):
 #   return x**2

def main():
    ListX = [2,3,4,5,6,7]
    #Res = Square(ListX)
    MData = list(map(Square,ListX))
    print(MData)

if __name__ == "__main__":
    main()

