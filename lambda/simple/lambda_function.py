import numpy as np


def lambda_handler(event, context):
    a = np.array([1, 2, 3])
    print(f"The array: {[1, 2, 3]}")
    print(f"The min value of the array is: {a.min()}")
    print(f"The max value of the array is: {a.max()}")
    print(f"The sum value of the array is: {a.sum()}")
