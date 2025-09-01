import pandas as pd

data = {
    'Gender': [
        'Man', 'Woman', 'Woman', 'Man', 'Man', 'Woman', 'Man', 'Woman', 'Woman', 'Man',
        'Woman', 'Man', 'Woman', 'Man', 'Woman', 'Man', 'Woman', 'Man', 'Woman', 'Man'
    ],
    'Age': [
        12, 25, 19, 22, 30, 17, 14, 28, 23, 15,
        20, 18, 16, 29, 11, 13, 27, 24, 21, 26
    ],
    'Likes_Sport': [
        'Like', 'Not Like', 'Like', 'Like', 'Not Like', 'Like', 'Not Like', 'Like', 'Not Like', 'Like',
        'Like', 'Not Like', 'Like', 'Like', 'Not Like', 'Not Like', 'Like', 'Like', 'Not Like', 'Like'
    ]
}

df = pd.DataFrame(data)

df['Gender'] = df['Gender'].map({'Man': 1, 'Woman': 0})
df['Likes_Sport'] = df['Likes_Sport'].map({'Like': 1, 'Not Like': 0})

print("\nDataFrame after encoding: ")
df.head(4)