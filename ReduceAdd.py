#lambda function using reduce returns add of list

from functools import reduce

Add = lambda No1, No2 : No1 + No2

def main():
    ListX = [2,3,4,5,6,7]
    MData = reduce(Add,ListX)
    print(MData)

if __name__ == "__main__":
    main()

