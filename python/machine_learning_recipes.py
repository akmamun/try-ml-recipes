import sklearn

features = [[140,"smooth"],[130, "smooth"],[150, "bumpy"],[170,"bumpy"]]
labels =["apple", "apple", "orange", "orange"]

"""# Define feature as a number and lables also
smooth = 0
bumpy = 0
apple = 0
orange = 1
"""

from sklearn import tree

features = [[140,1],[130,1],[150, 0],[170,0]]
labels =[0,0,1,1]

classifier = tree.DecisionTreeClassifier()

classifier.fit(features, labels)
print(classifier.predict([[150,0]]))

"""**Traning Visualisation wih Pandas Data Frame**
All Data in kilogram
"""

import pandas as pd
data = {'features' :  [[140,"smooth"],[130, "smooth"],[150, "bumpy"],[170,"bumpy"]],
        'labels' : ["apple", "apple", "orange", "orange"],
       'decition': [0,0,1,1]
       }
pf = pd.DataFrame(data)
print(pf)
