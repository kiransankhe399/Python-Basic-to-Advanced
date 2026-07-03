#Vowels

def Vowels(Char):
       if Char.lower() in ("a", "e", "i", "o", "u"):
            return True
       return False
            
def main():
    Value = input("Enter a Character : ")
    Res = Vowels(Value)
    if Res:
     print("Vowel") 
    else:
       print("Not Vowel")

if __name__ == "__main__":
    main()