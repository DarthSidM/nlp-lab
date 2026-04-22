from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# Training data
reviews = [
    "The movie was absolutely fantastic, I loved it",
    "What a great film, amazing acting and story",
    "It was a wonderful experience, truly inspiring",
    "The movie was boring and too long",
    "I did not like the film, it was disappointing",
    "Worst movie ever, waste of time"
]
labels = ["positive", "positive", "positive", "negative", "negative", "negative"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)
model = MultinomialNB()
model.fit(X, labels)
user_review = input("Enter a movie review:\n")
user_X = vectorizer.transform([user_review])
prediction = model.predict(user_X)
print("\nPredicted Sentiment:", prediction[0])
