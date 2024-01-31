import pandas
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt


data = pandas.read_csv('../abalone.data',
                       names=['sex', 'len', 'diam', 'height',
                              'whole weight', 'shucked weight',
                              'viscera weight', 'shell weight',
                              'rings'])
