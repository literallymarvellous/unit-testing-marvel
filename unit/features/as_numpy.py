import numpy as np
import re


def get_data_as_numpy_array(data, num_columns):
    with open(data) as file:
        f = [row.rstrip() for row in file]
        fs = [re.split(',|\t', str) for str in f]
        arr = np.array(fs, dtype='float64')
        arr = arr.reshape(len(arr), num_columns)
    return arr

