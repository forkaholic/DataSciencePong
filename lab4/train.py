from sklearn.linear_model import SGDRegressor, SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd
import csv
from joblib import dump

data = None

with open('pong_data.csv', newline='') as file:
    reader = csv.reader(file)
    c = 0
    temp = []
    for row in reader:
        if str(row) == '[]' or c == 0:
            c=1
        else:
            temp.append(row)
    data = pd.DataFrame(np.array(temp).astype(np.int16))
#[b0.x, b0.y, b0.vx, b0.vy, dir, p0.y, Ball.RADIUS, Paddle.L, Paddle.STEP, CONSTS.WIDTH, CONSTS.HEIGHT, CONSTS.BORDER, CONSTS.VELOCITY, CONSTS.FPS]
data = pd.DataFrame(data[data[0] > 550])
y = data[[5]]
data.drop(columns=[5], inplace=True)


pipeline = Pipeline([
    ("Standard Scaling", StandardScaler()),
    ("SGD Regression", SGDRegressor())
])

#X1, X2, y1, y2 = train_test_split(data, y, random_state=0, train_size=0.75)
pipeline.fit(data,y.values.ravel())

from sklearn.model_selection import cross_val_score
scores = cross_val_score(pipeline, data, y, cv=10)
print(scores)

#y_model = model.predict(X2)
# print(model.predict([[176,0,80]]))
dump(pipeline,'mymodel.joblib')