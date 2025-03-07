import json
import pickle

import numpy as np

model = None
data_columns = None

def load_artifacts():
    global model, data_columns

    with open('./artifacts/Diamonds_columns.json', 'r') as f:
        data_columns = json.load(f)['data_columns']

    with open('./artifacts/Diamond_linear_model.pickle', 'rb') as f:
        model = pickle.load(f)


def estimate_price(carat,cut,color,clarity,depth,table,x,y,z):
    load_artifacts()

    X = np.zeros(len(data_columns))
    X[0] = carat
    X[1] = cut
    X[2] = color
    X[3] = clarity
    X[4] = depth
    X[5] = table
    X[6] = x
    X[7] = y
    X[8] = z

    log_price =  model.predict([X])[0]
    return round(np.exp(log_price),2)



if __name__ == '__main__':

    print(estimate_price(0.21,4,6,3,59.8,61,3.89,3.84,2.31))