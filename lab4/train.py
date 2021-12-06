from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

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

pipeline.fit(data,y.values.ravel())
dump(pipeline,'mymodel.joblib')