#Radius of Circle

#def Circle(Radius):
#    return ( 2 * 3.14 * Radius)

Circle = lambda Radius: ( 2 * 3.14 * Radius)

def main():
    No = int(input("Enter radius of circle : "))
    Res = Circle(No)
    print("Area of circle is:", Res)

if __name__ == "__main__":
    main()