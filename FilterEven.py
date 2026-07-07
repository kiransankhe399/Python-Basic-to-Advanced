#lambda function using filter returns even of list

Even = lambda No : No % 2 == 0

#def Square(x):
 #   return x**2

def main():
    ListX = [2,3,4,5,6,7]
    #Res = Square(ListX)
    MData = list(filter(Even,ListX))
    print(MData)

if __name__ == "__main__":
    main()

