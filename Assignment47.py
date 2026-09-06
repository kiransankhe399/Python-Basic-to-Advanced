#1. 
#Cooeficient represent how much the output variable changeswhen the input feature increase by one unit
#IF  we want to predict salary (Y) based on Experience (X) and if X as an input changes the output Y also changes so the coeficient also changes

#2
# Y = 8X + 15
# Coeefieient is 8 and Intercept is 15
#The correlation coefficient (usually represented as \(r\)) tells us the strength and direction of the linear relationship between two variables, \(Y\) and \(X\).

#3
# If study hours increase by two then the output Marks also will get change and so the coeficient will also get change

#4
# Y = 12 * 2 +25 = Y = 49, Y = 12 * 5 +25 = Y, Y = 12 * 7 +25 

#5
#Negative coeficient indicates the graph will be -ve that is Input and output will be negative
# Y will be changed if X is increased by 1
# Y = -3 * 4 + 20 ; Y = -12 + 20

#6
#This is multiple regression model 
#Coefficient is diffrent for size and bedroom 
# larger the coeffiecent has the larger impact on house price

#7 Linear Regression
from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset
X = np.array([[1], [2], [3], [4], [5]])  # Study Hours
Y = np.array([50, 55, 60, 65, 70])       # Marks

# Train the regression model
model = LinearRegression()
model.fit(X, Y)

# Print coefficient and intercept
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict marks for 6 study hours
predicted = model.predict([[6]])
print("Predicted marks for 6 hours:", predicted[0])


#8
# Multiple Linear Regression
from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset
X = np.array([[1, 7],
              [2, 6],
              [3, 7],
              [4, 6],
              [5, 8]])  # StudyHours, SleepHours
Y = np.array([50, 55, 60, 65, 70])  # Marks

# Train the regression model
model = LinearRegression()
model.fit(X, Y)

# Print coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Predict marks for 6 study hours and 7 sleep hours
predicted = model.predict([[6, 7]])
print("Predicted marks for 6 study hours and 7 sleep hours:", predicted[0])
