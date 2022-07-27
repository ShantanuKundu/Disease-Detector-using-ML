# Disease-Detector-using-ML
GUI based Python progarm that uses Supervised Machine Learning Algorithms to detect disease from a given dataset

Only 2 types of diseases can be detected: Heart disease and Diabetes

The Program uses Logistic Regression and Decision Tree Algorithm to determine the better Algorithm to determine the model, by comparing the Accuracies of each 
algorithms.

GUI based program for a more interactive experience

Program is divided into 6 modules: Separate Heart and Diabetes detector, Splitting the datasets into Training and Testing datasets, Logistic Regression, Decision Tree and Main Health.py Program to combine all together and implement the GUI part, where the specific disease is to be given as input in the Name of the Disease field, then the respective Dependent columns and Independent columns must be split into Training and Testing datasets{THIS PART IS DONE IN THE SHELL, WHILE THE GUI WINDOW WILL STILL BE RUNNING}. Then the User presses the button for Suitable Algorithm(s). And finally determine the best algorithm for the model. Only the accuracies will be displayed in the GUI window, rest of the output will the displaye in the Shell simultaneously.

Datasets used: 

1. heart_disease_data.csv:
This data set dates from 1988 and consists of four databases: Cleveland, Hungary, Switzerland, and Long Beach V. It contains 76 attributes, including the predicted attribute, but all published experiments refer to using a subset of 14 of them. The "target" field refers to the presence of heart disease in the patient. It is integer valued 0 = no disease and 1 = disease.

Content:

Attribute Information:

age
sex
chest pain type (4 values)
resting blood pressure
serum cholestoral in mg/dl
fasting blood sugar > 120 mg/dl
resting electrocardiographic results (values 0,1,2)
maximum heart rate achieved
exercise induced angina
oldpeak = ST depression induced by exercise relative to rest
the slope of the peak exercise ST segment
number of major vessels (0-3) colored by flourosopy
thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.

2. diabetes.csv:
This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

Content:
The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on. If Outcome=1, Diabetes detected, else not detected.

Acknowledgements:
Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus. In Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261--265). IEEE Computer Society Press.



