import numpy_ as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import svm
# Example data for X & Y

X = np.array([[25, 50000, 700],   
              # Applicant 1: Age=25, Income=50,000, Credit Score=700
              [40, 80000, 650],   
              # Applicant 2: Age=40, Income=80,000, Credit Score=650
              [35, 60000, 720]])
              # Applicant 3: Age=35, Income=60,000, Credit Score=720

# Labels for each applicant 
y = np.array([0, 1, 0])  
  # y[0] = 0: Loan denied for Applicant 1.
  # y[1] = 1: Loan approved for Applicant 2.
  # y[2] = 0: Loan denied for Applicant 3.


# Standardize features by removing the mean and scaling to unit variance
# This is important to ensure all features contribute equally to the model.
# The fit() method learns the parameters and The transform() method applies the transformation
X = preprocessing.StandardScaler().fit(X).transform(X)


# Split dataset into training (67%) and testing (33%) sets
# `test_size=0.33` means 33% of the data is used for testing
# split a dataset into two parts:
  # Training set: Used to train the machine learning model (e.g., 67% of the data).
  # Testing set: Used to evaluate the model's performance (e.g., 33% of the data).
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

  # X: The input features (independent variables).
  # y: The target labels (dependent variable).
  # test_size: The proportion of the dataset to include in the test split (e.g., 0.33 means 33% for testing and 67% for training).

# Create an SVM classifier with specified hyperparameters
# `gamma=0.001` controls the influence of a single training example
# `C=100.` controls the trade-off between achieving a low error and a simple model
clf = svm.SVC(gamma=0.001, C=100.)