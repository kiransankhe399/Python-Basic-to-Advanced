
import math


def EUCDistance(P1, P2):
    Ans = math.sqrt(((P1['X']-P2['X'])** 2 + (P1['Y']-P2['Y']) ** 2))
    return Ans

def KNNClassifier():

    DataSet = [
        {'Point': 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
        {'Point': 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
        {'Point': 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
        {'Point': 'D', 'X' : 6, 'Y' : 5, 'label' : 'Blue'},  
    ]

    for i in DataSet:
        print(i)

    x = int(input("Enter X coordinate of new point : "))
    y = int(input("Enter Y coordinate of new point : "))

    new_point = {'X' : x, 'Y' : y}

    for d in DataSet:
        d['Distance'] = EUCDistance(d, new_point)


    sorted_data = sorted(DataSet, key= lambda item : item['Distance'])
    print("Sorted Data:")

    for d in sorted_data:
        print(d)

    nearest = sorted_data[:3]
    print("Nearest 3 members are :")

    for d in nearest:
        print(d)

    votes = {}
    for neighbours in nearest:
        label = neighbours['label']
        votes[label] = votes.get(label,0) + 1

    print("Votes : ", votes)

    max_votes = 0
    predicted_label = ""
    for label in votes:
        if votes[label] > max_votes:
            max_votes = votes[label]
            predicted_label = label

    print("Predicted label for new point is : ", predicted_label)

def main():
    KNNClassifier()

if __name__ == "__main__":
    main()