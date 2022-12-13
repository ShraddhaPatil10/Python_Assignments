import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):
    #Load the data
    data = pd.read_csv(data_path,index_col=0)

    print("Size of actual dataset:",len(data))
    print("")

    #Clean,Prepare and Manipulate data
    Features_name = ['Whether','Temperature']

    print("Name of the features:",Features_name)
    print("")

    wheather = data.Whether
    Temperature = data.Temperature
    play = data.Play

    #Creating labelEncoder
    le = preprocessing.LabelEncoder()

    #Converting string label into numbers
    wheather_encoded = le.fit_transform(wheather)
    print(wheather_encoded)
    print("")

    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    print(temp_encoded)
    print("")

    #Combining whether and temp into single list of tuple
    features = list(zip(wheather_encoded,temp_encoded))

    #Train data
    model = KNeighborsClassifier(n_neighbors=3)

    #Train data model using the training sets
    model.fit(features,label)

    #Test data
    predicted = model.predict([[0,2]])  #0:overcast  2:mild
    print(predicted)
    print("")

    if predicted==1:
        print("You are allowed for playing")

    else:
        print("You are not allowed for playing")

def main():
    print("--------------------------------------Shraddha Patil--------------------------------")
    print("Machine Learning Application")

    print("Play Predictor application using K Nearest KNeighbor algorithm")
    print("")

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__=="__main__":
    main()