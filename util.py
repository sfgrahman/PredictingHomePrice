import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    p__data_columns = get_data_columns()
    try:
        loc_index = p__data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(p__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    model_predict = load_saved_artifacts()
    return round(model_predict.predict([x])[0],2)


def load_saved_artifacts():
    with open('banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    return __model

def get_location_names():
    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    return __locations

def get_data_columns():
    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location