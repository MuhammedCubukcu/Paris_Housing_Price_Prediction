# import
import numpy as pd 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler



# Importing the dataset
dataset = pd.read_csv('ParisHousing.csv')
print(dataset.head())


# Taking care of missing data
print(dataset.isnull().sum())

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print("Training dataset : ", X_train.shape, y_train.shape)
print("Testing dataset : ", X_test.shape, y_test.shape)

# Feature Scaling

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the Simple Linear Regression model on the Training set

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)


# Visualizing the model
plt.scatter(y_test, y_pred, color='blue')
plt.title('Actual vs Predicted')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()




from sklearn.metrics import r2_score

# Calculate R2 score
r2 = r2_score(y_test, y_pred)
# Convert to percentage
r2_percentage = r2 * 100

print(f'R-squared (R2) score: {r2_percentage:.2f}%')


