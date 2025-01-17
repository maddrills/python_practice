import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #panda for data pre processing

dataset = pd.read_csv('../../../Mechine Learning/Logistics/pythonProject2/Data.csv')
x = dataset.iloc[:, :-1] # to exctract the features 1st arg in[] is rows 2nd is columns, LHS:RHS LHS lower bound RHS upper bound
y = dataset.iloc[:, -1]

print(x)
print(y)