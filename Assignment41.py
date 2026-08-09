#Wine Case Study
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
##############################################################
#Step 1: Get Data
###############################################################

class Wine():
    def __init__(self,data_path):
        self.DataPath = data_path
        self.df = None
        self.model = None

    def GetData(self):
        self.df = pd.read_csv(self.DataPath)
        print("Data Loaded Successfully")
        print(self.df.head())
        return self.df        

##############################################################
#Step 2: Clean, Prepare and Manipulate data (EDA)
###############################################################
     
    def CleanData(self):
        X = self.df.drop("Class",axis=1)
        Y = self.df["Class"]
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X) #for large dataset we can use MinMaxScaler
        X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, train_size=0.2, random_state=42)
        print("Data Cleaned Successfully")
        return X_train, X_test, Y_train, Y_test 
    
# ##############################################################
# #Step 3: Train Data
# ###############################################################

    def modelTrain(self,X_train,Y_train):
        self.model.fit(X_train,Y_train)
        print("Model trained succesfully")
 

# ##############################################################
# #Step 4: Test Data
# ###############################################################
    def modelTest(self,X_test,Y_test):
        Y_pred = self.model.predict(X_test)
        print("Model Testing done")
        return(Y_pred)

# ##############################################################
# #Step 5: Calculate Accuracy
# ###############################################################
    
    def modelAccuracy(self,Y_test,Y_pred):
        accuracy = accuracy_score(Y_test,Y_pred)
        print("accuracy is ", accuracy*100)
        return accuracy
    

def main():
    objWine = Wine("WinePredictor.csv")
    objWine.GetData()
    X_train, X_test, Y_train, Y_test = objWine.CleanData()
    objWine.model = LogisticRegression()
    objWine.modelTrain(X_train, Y_train)
    Y_pred = objWine.modelTest(X_test, Y_test)
    objWine.modelAccuracy(Y_test, Y_pred)


if __name__ == "__main__":
    main()
