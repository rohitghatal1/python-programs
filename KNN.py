import numpy as np
import pandas as pd
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier

data = [
  {"Weight": 260, "Height": 162, "Animal": "Horse"},
  {"Weight": 33, "Height": 90, "Animal": "Dog"},
  {"Weight": 150, "Height": 210, "Animal": "Horse"},
  {"Weight": 25, "Height": 70, "Animal": "Dog"},
  {"Weight": 38, "Height": 82, "Animal": "Dog"},
  {"Weight": 320, "Height": 175, "Animal": "Horse"},
  {"Weight": 29, "Height": 98, "Animal": "Dog"},
  {"Weight": 200, "Height": 170, "Animal": "Horse"},
  {"Weight": 39, "Height": 108, "Animal": "Dog"},
  {"Weight": 210, "Height": 172, "Animal": "Horse"},
  {"Weight": 45, "Height": 85, "Animal": "Dog"},
  {"Weight": 275, "Height": 185, "Animal": "Horse"},
  {"Weight": 20, "Height": 75, "Animal": "Dog"},
  {"Weight": 300, "Height": 178, "Animal": "Horse"},
  {"Weight": 50, "Height": 95, "Animal": "Dog"},
  {"Weight": 180, "Height": 165, "Animal": "Horse"},
  {"Weight": 65, "Height": 100, "Animal": "Dog"},
  {"Weight": 240, "Height": 180, "Animal": "Horse"},
  {"Weight": 28, "Height": 72, "Animal": "Dog"},
  {"Weight": 210, "Height": 170, "Animal": "Horse"}
]

df = pd.DataFrame(data)

df['Label'] = df['Animal'].map({'Dob': 0, 'Horse': 1})

x = df[['Weight', 'Height']].values
y = df[['Label']].values