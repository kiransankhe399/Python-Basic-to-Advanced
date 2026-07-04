#Add Sub Multi Div

#def Add(No1, No2):
# Add =No1+ No2
# return Add

Add = lambda No1,No2 : (No1 + No2)  #Functional

#def Sub(No1, No2):
#  Sub =No1- No2
#   return Sub

Sub = lambda No1,No2 : (No1 - No2)  #Functional

#def Multi(No1, No2):
#  Mult =No1 * No2
#  return Mult

Multi = lambda No1,No2 : (No1 * No2)

#def Div(No1, No2):
#  Div =No1 / No2
#    return Div

Div = lambda No1,No2 : (No1 / No2)

    
def main():
    Value1 = int(input("Enter first Num : "))
    Value2 = int(input("Enter second Num : "))

    Res1 = Add(Value1, Value2)
    print("Addition is :", Res1)

    Res2 = Sub(Value1, Value2)
    print("Substraction is :", Res2)

    Res3 = Multi(Value1, Value2)
    print("Multiplication is :", Res3)

    Res4 = Div(Value1, Value2)
    print("Division is :", Res4)

if __name__ == "__main__":
    main()