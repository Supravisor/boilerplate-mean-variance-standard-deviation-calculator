
import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        matrix = np.array(list).reshape(3, 3)

    calculations = {
        "mean": [(matrix.mean(axis=0).tolist()), (matrix.mean(axis=1).tolist()), (matrix.flatten().mean())],
        "variance": [(matrix.var(axis=0).tolist()), (matrix.var(axis=1).tolist()), (matrix.flatten().var())]
    }


    return calculations
