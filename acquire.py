from pydataset import data
import pandas as pd

# data('iris', show_doc=True)

# df_iris = data('iris')

def get_iris_doc():
    return data('iris', show_doc=True)

def get_iris_data():
    iris_df = data('iris')
    return iris_df

def get_data(dataset):
    df = data(dataset)
    return df