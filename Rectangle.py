#rectangle

#def Area(Len,Width):
# return  Len * Width

Area = lambda Len,Width : Len * Width

def main():
    No1 = int(input("Enter length :"))
    No2 = int(input("Enter Width :"))
    Res = Area(No1,No2)
    print("Area of rectangle is", Res)

if __name__ == "__main__":
    main()