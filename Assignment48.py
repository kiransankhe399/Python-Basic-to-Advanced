import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvelleousPredictor():

    #Load the Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variable X :", X)
    print("Values of Dependent Variable Y :", Y)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    #Summation

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean of X :", mean_x)
    print("Mean of Y :", mean_y)

    n = len(X)

    numerator = 0
    denominator = 0

    # Calculate Slope ie m

    for i in range(n):
        numerator = numerator + ((X[i]-mean_x) * (Y[i]-mean_y))
        denominator = denominator + ((X[i]-mean_x)**2)

    m = numerator / denominator
    print("Slope of line m :", m)

    # y = mx + c

    c = mean_y - (m * mean_x)
    print("Y intercept os :", c)

    x = np.linspace(1,6,n)
    y = c + m * x

    plt.plot(x,y,color = 'g', label = "Regression Line")
    plt.scatter(X,Y, color = 'r', label = "Scattered plot")

    plt.xlabel("X : Independent Variables")
    plt.ylabel("Y : Dependent Variables")

    plt.legend()
    plt.show()
    

    
def main():
    MarvelleousPredictor()

if __name__ == "__main__":
    main()