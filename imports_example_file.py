from pydataset import data
import pandas as pd

def get_data(dataset):
    '''
    this function reads the first 5 rows of a dataset into a dataframe
    '''
    df = data(dataset).head()
    return df