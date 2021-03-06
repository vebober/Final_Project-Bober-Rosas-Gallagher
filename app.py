import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.image as mpimg 
import json
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from flask import Flask, jsonify, render_template,request

# DATA CLEANING
data = pd.read_csv('data/The_Actual_Final_Dataset2.csv')
data.fillna('No')
data.head()
data= data[data['Inflation_Adj_Cost1'] != 0]
X = data[['bedrooms', 'bathrooms', 'half_baths', 'living_area', 'construction_quality', 'condition_score', 'garage_type', 
'finished_basement_No', 'total_land', 'house_age']]
y = data['Inflation_Adj_Cost1'].values.reshape(-1, 1)

# MAKING THE MODEL
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
X_scaler = StandardScaler().fit(X_train)
y_scaler = StandardScaler().fit(y_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
y_train_scaled = y_scaler.transform(y_train)
y_test_scaled = y_scaler.transform(y_test)
model = LinearRegression()
model.fit(X_train_scaled, y_train_scaled)

# USING ELASTICNET METHOD
elasticnet = ElasticNet(alpha=.01).fit(X_train_scaled, y_train_scaled)
predictions = elasticnet.predict(X_test_scaled)
MSE = mean_squared_error(y_test_scaled, predictions)
r2 = elasticnet.score(X_test_scaled, y_test_scaled)

# USING INPUT DATA (Samples here)
# We need to change these variables to the things that people input 


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Calculator")
def Calculator():

    test = (1,2,3,4)
    print(test)
    ml_input = (json.loads(request.args.get('input')))
    ml_input = ml_input.split(",")
    print(ml_input)
    my_list = [float(i) for i in ml_input]
    print(my_list)
    Sample= [np.asarray(my_list)]
    SS = X_scaler.transform(Sample)
    SS
    Outcome = y_scaler.inverse_transform(elasticnet.predict(SS))
    print("YOUR PRICE IS ")
    print(Outcome)
    Outcome = float(Outcome)
    Outcome = f'${Outcome:.2f}'
    return jsonify(Outcome)

if __name__ == "__main__":
    app.run()



