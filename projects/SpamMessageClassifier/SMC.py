import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "message": [
        "Congratulations! You won a free ticket to Bahamas, claim now!",
        "Hello, how are you doing today?",
        "Win $1000 cash by entering this contest!!!",
        "Are we still meeting for lunch?",
        "Free entry in a weekly prize draw, text WIN to 12345",
        "Hey, can you send me the notes from class?",
    ],
    "label": ["span", "ham", "spam", "ham", "spam", "ham"]
}

df = pd.DataFrame(data)


x = df["message"]
y = df["label"].map({"ham":0, "span": 1})

vectorizer = TfidfVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(x)


x_train, x_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))


new_message = ["Claim yor free prize now!!!"]
new_vec = vectorizer.transform(new_message)
print("Prediction for new message:", "Span" if model.predict(new_vec)[0] == 1 else "Ham")

