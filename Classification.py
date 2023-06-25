from joblib import dump, load
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.metrics import accuracy_score


def Train_SVM_Classifier(Train_Signals, Labels):
#def Train_SVM_Classifier(Train_Signals, Labels, Test_Signals, TestLabels):
    # Create the SVM classifier
    SVM_Model = SVC(kernel='linear', C=1, random_state=42)
    # Train the classifier on the training set
    SVM_Model.fit(Train_Signals, Labels)
    SaveModel(SVM_Model,'SVM')
    scores = cross_val_score(SVM_Model, Train_Signals, Labels, cv=5)
    trainAcc = np.mean(scores)
    # y_pred = SVM_Model.predict(Test_Signals)
    # Evaluate the accuracy of the model
    # accuracy = accuracy_score(TestLabels, y_pred)
    print("SVM Train Acc = %.2f%%" % round(trainAcc * 100, 2))
    # print("SVM Test Accuracy: {:.2f}%".format(accuracy * 100))
    return trainAcc

def Train_RF_Classifier(Train_Signals, Labels):
# def Train_RF_Classifier(Train_Signals, Labels, Test_Signals, TestLabels):
    RF_Model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=0)
    RF_Model.fit(Train_Signals, Labels)
    scores = cross_val_score(RF_Model, Train_Signals, Labels, cv=5)
    SaveModel(RF_Model,'RF')
    trainAcc = np.mean(scores)
    # y_pred = RF_Model.predict(Test_Signals)
    # Evaluate the accuracy of the model
    # accuracy = accuracy_score(TestLabels, y_pred)
    print("RF Train Acc = %.2f%%" % round(trainAcc * 100, 2))
    # print("RF Test Accuracy: {:.2f}%".format(accuracy * 100))
    return trainAcc

def Train_LR_Classifier(Train_Signals, Labels):
# def Train_LR_Classifier(Train_Signals, Labels, Test_Signals, TestLabels):
    LR_Model =  LogisticRegression(multi_class='ovr')
    LR_Model.fit(Train_Signals, Labels)
    SaveModel(LR_Model, 'LR')
    scores = cross_val_score(LR_Model, Train_Signals, Labels, cv=5)
    trainAcc = np.mean(scores)
    # y_pred = LR_Model.predict(Test_Signals)
    # Evaluate the accuracy of the model
    # accuracy = accuracy_score(TestLabels, y_pred)
    print("RF Train Acc = %.2f%%" % round(trainAcc * 100, 2))
    # print("RF Test Accuracy: {:.2f}%".format(accuracy * 100))

    return trainAcc
def Train_DT_Classifier(Train_Signals, Labels):
# def Train_DT_Classifier(Train_Signals, Labels, Test_Signals, TestLabels):
    DT_Model = DecisionTreeClassifier(random_state=0)
    DT_Model.fit(Train_Signals, Labels)
    SaveModel(DT_Model, 'DT')
    accuracy = DT_Model.score(Train_Signals, Labels)
    # y_pred = DT_Model.predict(Test_Signals)
    # Evaluate the accuracy of the model
    # testaccuracy = accuracy_score(TestLabels, y_pred)
    print("DT Train Acc = %.2f%%" % round(np.mean(accuracy) * 100, 2))
    # print("DT Test Accuracy: {:.2f}%".format(testaccuracy * 100))
    return np.mean(accuracy)

def GetLabels (Singnals):
    Labels = []
    ClassLength = len(Singnals)/4
    for i in range(len(Singnals)):
        X = i/ClassLength
        Labels.append(int(X))
    return Labels

def SaveModel(Model,Name:str):
    Name = Name.upper()
    # Save the model
    dump(Model, Name + 'model.joblib')

def LoadModel(Name):
    Name = Name.upper()
    # Load the model
    Model = load(Name + 'model.joblib')
    return Model
