import pandas as pd

df = pd.read_csv("mock_employees.csv")

print (df)
print ("headerss: ", df.head())
print ("tail: ", df.tail())
print ("mean of age: ", df['age'].mean())