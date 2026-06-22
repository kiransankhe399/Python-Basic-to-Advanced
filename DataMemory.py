print("-----------Display Data, Memory, Len--------------------------------------")

def Memory(No):
   Type = type(No)
   Id =  id(No)
   Len = bytes(len(No) )
   return Type,Id,Len

def main():
    Value = input("Enter a number: ")
    ValueType,ValueId, ValueLen = Memory(Value)
    print("Type is:", ValueType)
    print("Id is:", ValueId)
    print("len is:", ValueLen)


if __name__ == "__main__":
    main()