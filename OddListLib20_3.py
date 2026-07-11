#Library

def OddList(Num):
    OList = []
    Sum = 0
    for i in Num:
       if i % 2 != 0:
         OList.append(i)
    
    for i in OList:
        Sum = Sum + i

    print("Odd List is :",OList)
    print("Sum of Odd List is :",Sum)
    return Sum
