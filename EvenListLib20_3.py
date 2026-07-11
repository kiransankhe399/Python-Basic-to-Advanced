#Library

def EvenList(Num):
    EList = []
    Sum = 0
    for i in Num:
       if i % 2 == 0:
         EList.append(i)
    
    for i in EList:
        Sum = Sum + i

    print("Even List is :",EList)
    print("Sum of Even List is :",Sum)
    return Sum
