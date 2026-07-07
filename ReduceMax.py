#lambda function using reduce returns max of list

from functools import reduce

Max = lambda x, y: x if x > y else y

def main():
    ListX = [2,3,4,5,6,7]
    MData = reduce(Max,ListX)
    print(MData)

if __name__ == "__main__":
    main()

