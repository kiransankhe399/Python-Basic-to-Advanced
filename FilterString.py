#lambda function using reduce returns max len of str of list


StrGreter = lambda x,y : x if len(x)  > len(y) else y

def main():
    ListX = ["ab","abc","ab3cd","abb","asd","nsd"]
    MData = list(filter(StrGreter,ListX))
    print(MData)

if __name__ == "__main__":
    main() 

