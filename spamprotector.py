
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    'message': [
        'Congratulations! You have won a $1000 Walmart gift card. Go to http://bit.ly/12345 to claim now.',
        'Hey, are we still meeting for lunch today?',
        'URGENT! Your account has been compromised. Reply immediately!',
        'Are you coming to the party tonight?',
        'Free entry in 2 a weekly competition to win FA Cup final tickets text FA to 12345'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam']
}

df = pd.DataFrame(data)

df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})


X = df['message']
y = df['label_num']

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)


model = MultinomialNB()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


sample_email = ["Congratulations! You've been selected for a free cruise to Bahamas! Call now!"]
sample_vectorized = vectorizer.transform(sample_email)
prediction = model.predict(sample_vectorized)

print("\nSample Email Prediction:", "Spam" if prediction[0] else "Ham")
