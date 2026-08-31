import numpy as np
import pandas as pd
# Numpy array operations
marks = np.array([72,85,91,68,77])
print("marks:",marks)
print("Mean:",np.mean(marks))
print("Maximum:",np.max(marks))
print("minimum:",np.min(marks))

# pandas dataframe Creation 
data = {
    "Name":["Amit","Riya","Sourav","Neha","rahul"],
    "Attendence":[88,92,76,95,81],
    "Marks":[72,85,68,91,77]
}
df=pd.DataFrame(data)
#Data exploration
print("\n--First five Records--")
print(df.head())

print("\n--Data Information--")
print(df.info())

print("\n---statistical Summary---")
print(df.describe())
print("\nAverage marks:",df["Marks"].mean())
