#!/usr/bin/env python
# coding: utf-8

# In[19]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.image as mpimg 


# In[20]:


data = pd.read_csv('data/The_Actual_Final_Dataset2.csv')
data.fillna('No')
data.head()
data= data[data['Inflation_Adj_Cost1'] != 0]


# In[21]:


data.columns


# In[22]:


#data2 = pd.get_dummies(data)
#data2.head()
#data2['Inflation_Adj_Cost1']= data2['Inflation_Adj_Cost1'].astype('int')
#data2['Inflation_Adj_Cost2']= data2['Inflation_Adj_Cost2'].astype('int')


#data2


# In[23]:


#Took about total value because that's the whole point of the project

X = data[['bedrooms', 'bathrooms', 'living_area',
       'half_baths', 'construction_quality',
       'condition_score', 'garage_type', 'finished_basement_No', 'total_land',
       'zipcodes', 'house_age']]
y = data['Inflation_Adj_Cost1'].values.reshape(-1, 1)
print(X.shape, y.shape)


# In[24]:


# Split the data into training and testing

### BEGIN SOLUTION
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
### END SOLUTION
print(X_train)


# In[25]:


from sklearn.preprocessing import StandardScaler

# Create a StandardScater model and fit it to the training data

### BEGIN SOLUTION
X_scaler = StandardScaler().fit(X_train)
y_scaler = StandardScaler().fit(y_train)
### END SOLUTION'


# In[26]:


# Transform the training and testing data using the X_scaler and y_scaler models

### BEGIN SOLUTION
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
y_train_scaled = y_scaler.transform(y_train)
y_test_scaled = y_scaler.transform(y_test)
### END SOLUTION
print(X_train_scaled)


# In[27]:


# Create a LinearRegression model and fit it to the scaled training data

### BEGIN SOLUTION
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_scaled, y_train_scaled)
### END SOLUTION


# In[28]:


# Make predictions using the X_test_scaled data
# Plot y_test_scaled vs y_test_scaled
# Scatter plot y_test_scaled vs predictions

### BEGIN SOLUTION
predictions = model.predict(X_test_scaled)
# model.fit(X_train_scaled, y_train_scaled)
plt.scatter(model.predict(X_train_scaled), model.predict(X_train_scaled) - y_train_scaled, c="blue", label="Training Data")
plt.scatter(model.predict(X_test_scaled), model.predict(X_test_scaled) - y_test_scaled, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_scaled.min(), xmax=y_test_scaled.max())
plt.title("Residual Plot")
plt.show()


# In[29]:


# Used X_test_scaled, y_test_scaled, and model.predict(X_test_scaled) to calculate MSE and R2

### BEGIN SOLUTION
from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(y_test_scaled, predictions)
r2 = model.score(X_test_scaled, y_test_scaled)
### END SOLUTION

print(f"MSE: {MSE}, R2: {r2}")


# In[30]:


# LASSO model
# Note: Use an alpha of .01 when creating the model for this activity
from sklearn.linear_model import Lasso

### BEGIN SOLUTION
lasso = Lasso(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = lasso.predict(X_test_scaled)

MSE = mean_squared_error(y_test_scaled, predictions)
r2 = lasso.score(X_test_scaled, y_test_scaled)
### END SOLUTION

print(f"MSE: {MSE}, R2: {r2}")


# In[31]:


# Ridge model
# Note: Use an alpha of .01 when creating the model for this activity
from sklearn.linear_model import Ridge

### BEGIN SOLUTION
ridge = Ridge(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = ridge.predict(X_test_scaled)

MSE = mean_squared_error(y_test_scaled, predictions)
r2 = ridge.score(X_test_scaled, y_test_scaled)
### END SOLUTION

print(f"MSE: {MSE}, R2: {r2}")


# In[32]:


# ElasticNet model
# Note: Use an alpha of .01 when creating the model for this activity
from sklearn.linear_model import ElasticNet

### BEGIN SOLUTION
elasticnet = ElasticNet(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = elasticnet.predict(X_test_scaled)

MSE = mean_squared_error(y_test_scaled, predictions)
r2 = elasticnet.score(X_test_scaled, y_test_scaled)
### END SOLUTION

print(f"MSE: {MSE}, R2: {r2}")


# In[33]:


from sklearn.linear_model import ElasticNet

### BEGIN SOLUTION
elasticnet = ElasticNet(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = elasticnet.predict(X_test_scaled)

MSE = mean_squared_error(y_test_scaled, predictions)
r2 = elasticnet.score(X_test_scaled, y_test_scaled)
### END SOLUTION

print(f"MSE: {MSE}, R2: {r2}")


# In[34]:


data.columns


# In[35]:


# 1. bedrooms
# 2. bathrooms
# 3. living_area
# 5. half_baths
# 6. construction_quality
# 7. condition_score
# 8. garage_type
# 9. finished_basement_No 
# 10. total_land
# 11. zipcodes
# 12. house_age


# In[75]:


Sample = np.array([[3,1,1932,1,5,6,2,2,10800,6,71]])
SS = X_scaler.transform(Sample)
SS
Outcome = y_scaler.inverse_transform(elasticnet.predict(SS))

Outcome


# In[ ]:





# ## 
