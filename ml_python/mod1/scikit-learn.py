import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix
import pickle
# Example data for X & Y

X = np.array([[25, 50000, 700],   
              # Applicant 1: Age=25, Income=50,000, Credit Score=700
              [40, 80000, 650],   
              # Applicant 2: Age=40, Income=80,000, Credit Score=650
              [35, 60000, 720]])
              # Applicant 3: Age=35, Income=60,000, Credit Score=720

# Labels for each applicant ( the answers )
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
# SVM classifier — a type of model that classifies things (in your case: approve or deny a loan).
# `gamma=0.001` controls the influence of a single training example
# Think of gamma as how far the model looks when deciding how to draw the decision boundary
  # Low gamma (0.001): You look at the big picture, not too focused on just a few people. Good for generalization. “People between ages 20–40 with medium income mostly dislike pineapple, so this person probably doesn’t either.”
  # High gamma: You judge based on very few, close neighbors, maybe too focused. Good for very detailed fitting “Oh, the person next to you loves pineapple? Then you probably do too.”

# `C=100.` controls the trade-off between achieving a low error and a simple model
  # High C means Be strict — try to classify everything correctly, even if the model becomes a little complicated.”
clf = svm.SVC(gamma=0.001, C=100.)


# Train the SVM model on the training dataset
  # .fit() means "learn from data".

  # X_train — the input features (like age, income, credit score)
  # y_train — the correct answers (loan approved or denied: 1 or 0)

  # “Use this data to figure out how to predict future decisions.”

  # It analyzes the inputs (X_train) and the labels (y_train)
  # It finds a decision boundary — like a smart line — that tries to separate "approved" vs "denied"
  # It remembers this rule, so it can apply it later to new applicants (using .predict())

  # Uses Support vectors: the closest data points to the boundary that affect its position. 
  # Optimization math: It moves the boundary to make the margin as wide as possible without misclassifying data.

clf.fit(X_train, y_train)

# Make predictions on the test set
yhat = clf.predict(X_test)

# Compute and print the confusion matrix to evaluate classification performance
# The confusion matrix shows the number of correct and incorrect predictions for each class
# `labels=[1,0]` ensures the rows/columns correspond to class 1 and class 0 respectively
print(confusion_matrix(y_test, yhat, labels=[1,0]))

""" 
               Predicted
             |  1   |  0
         ----------------
Actual  1 |  TP  | FN   ← (Actual approved)
        0 |  FP  | TN   ← (Actual denied)

        [[0 0]
        [0 1]]


✅ True Positives (TP) = 0 → The model correctly predicted approve for 0 people.
❌ False Negatives (FN) = 0 → It didn’t mess up any approves either.
❌ False Positives (FP) = 0 → It didn’t wrongly approve anyone.
✅ True Negatives (TN) = 1 → The model correctly predicted deny for 1 person.

based on chatgpt, this was just luck since the given was random

"""


# Serialize (save) the trained model using pickle
# This allows the model to be saved and loaded later without retraining
# The line s = pickle.dumps(clf) serializes (converts) the trained SVM model (clf) into a byte stream using the pickle module.
s = pickle.dumps(clf)

# 🔁 How can I use it again later?

# Save the model to a file
""" with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f) """

# Load the model from the file
""" with open('model.pkl', 'rb') as f:
    clf = pickle.load(f) """
  # Now you can use clf.predict(...) again!

""" 

Models like SVM can give a probability (or confidence level) because:

They don’t just classify into "approved" or "denied" based on a hard rule. Instead, they give a likelihood of an outcome based on patterns in the data.

For example, if the model says there’s a 70% chance the loan will be approved, that means it's fairly confident based on the features (but not certain).

SVM is an algorithm based on math and optimization. It’s a tool for learning patterns in data and making predictions.

It's a machine learning technique that can be used within AI systems, but it’s not AI by itself.

"""