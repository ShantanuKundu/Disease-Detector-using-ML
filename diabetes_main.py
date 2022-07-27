#Importing modules
import numpy as np
import pandas as pd
import SplitData as sd
import DTTrain as dt
import LRTrain as lr

#Empty Datframes
X=pd.DataFrame()
Y=pd.DataFrame()
X_train=pd.DataFrame()
X_test=pd.DataFrame()
Y_train=pd.DataFrame()
Y_test=pd.DataFrame()
#User input for later checking of the algorithm
input_data = np.array([9,156,86,0,0,24.8,0.23,53])
_acc_dt=0.0
_acc_lr=0.0
def _for_diabetes():
        #Reading dataset: creditcard.csv
        dataset= pd.read_csv(r'ur_local_diabetes_data.csv_file_location')
        #print('Dataset Information:\n',dataset.info())
        print('Dataset Read')

        global  X,Y,X_train,X_test,Y_train,Y_test, input_data

        #Calling the split function
        X,Y,X_train,X_test,Y_train,Y_test=sd.dataset_split(dataset)
        print('Training Data\n',X_train.head())
        print('\nTesting Data\n',X_test.head())
        print('\nTraining Data\n',Y_train.head())
        print('\nTesting Data\n',Y_test.head())


        print('\nTraining Data:',X_train.shape,Y_train.shape,)
        print('\nTesting Data:',X_test.shape,Y_test.shape)

        print('\nDataset Split\n')
        
#Calling the respective algorithm to determine the model
def call_dt():
    global _acc_dt
    dt.model_dt(X_train,Y_train,X_test,Y_test,input_data)
    _acc_dt=dt.acc_dt()
def call_lr():
    global  _acc_lr
    lr.model_lr(X_train,Y_train,X_test,Y_test,input_data)
    _acc_lr=lr.acc_lr()
def better_algo():
        if _acc_dt > _acc_lr:
                return 'Decision Tree'
        else:
                return 'Logistic Regression'        
        
if __name__=='__main__':
    _for_diabetes()
    call_dt()
    call_lr()
    better_algo()
