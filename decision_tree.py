#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

age = {"Young": 1, "Prepresbyopic": 2, "Presbyopic": 3}
spectacle = {"Myope": 1, "Hypermetrope": 2}
astigmatism = {"Yes": 1, "No": 2}
tear = {"Reduced": 1, "Normal": 2}
lenses = {"No": 0, "Yes": 1}

#encode the original categorical training features into numbers and add to the 4D array X.
#--> add your Python code here
# X =
for row in db:
    X.append([age[row[0]], spectacle[row[1]], astigmatism[row[2]], tear[row[3]]])


#encode the original categorical training classes into numbers and add to the vector Y.
#--> addd your Python code here
# Y =
for row in db:
    Y.append(lenses[row[4]])

#fitting the decision tree to the data using entropy as your impurity measure
#--> addd your Python code here
#clf =
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X, Y)

#plotting the decision tree
plt.figure(figsize=(8,6))
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes', 'No'], filled=True, rounded=True)
plt.show()