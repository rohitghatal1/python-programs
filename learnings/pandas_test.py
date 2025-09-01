import pandas as pd

data = {
    "Name": ["Rohit", "Nikit", "Kshitij"],
    "Age": [24,12,22],
    "City": ["Kathmandu", "Lalitpur", "Bhaktapur"]
}

df = pd.DataFrame(data)

print (df)