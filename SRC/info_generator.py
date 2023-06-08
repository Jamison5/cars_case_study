import numpy as np 
import pandas as pd 
import matplotlib.pyplot 
import scipy.stats as stats 
import seaborn as sns 
import math 


def df_generator(file_path):
    '''Generates a df from cars.csv and cleans the data to prepare it for further examination. This function assumes that the dataset you are using is an updated version of cars.csv and has the same original
       structure. If the dataset you are inputing into this function is not an updated version of cars.csv it will not work as intended.'''

    df = pd.read_csv(file_path)
    '''Create dataframe from relative filepath.'''


    df.rename(columns={'model':'year'}, inplace=True)
    '''Renames column model to year.'''


    df['make'] = df['car_name'].str.split().str[0]
    df['model'] = df['car_name'].str.split().str[1:].str.join(' ')
    df.drop('car_name', axis=1, inplace=True)
    '''Splits the car_name column into two seperate columns that contain the make and model derived from the original column, car_name is the dropped.'''


    df['horsepower'].replace('?', 0, inplace=True)
    df['horsepower'] = df['horsepower'].astype(float)
    '''horsepower column is currently an object, despite having values that need to be agregated for later statistics. Replaces all ? str type objects with 0s and casts the column to type float.'''

    return df






if __name__ == "__main__":

    a = df_generator('../data/cars.csv')
    print(a.info())