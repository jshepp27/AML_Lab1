import numpy
import pandas as pd

# TODO
# Connect to and pull data from a GCP storage bucket

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv("data.csv", names=names)

pd.set_option('precision', 3)
print(data.head(10))
print(data.count(axis="index"))
print(data.dtypes)
print(data.shape)
print(data.describe())

# Data Distribution
class_counts = data.groupby("class").size()
print(class_counts)

# Pearsons Correlation Coefficient
print(data.corr(method="pearson"))

# Skew
print(data.skew())