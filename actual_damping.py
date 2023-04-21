import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

length = 10.8

actual_data = pd.read_csv("TRANSMISSION.CSV", usecols=[0], header=None)

actual_data = np.log(10 ** (abs(actual_data)/20))/length

actual_data = actual_data.values