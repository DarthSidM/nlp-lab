import os
import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# --- 1. Data Acquisition ---
# Download the IMDB dataset
path = kagglehub.dataset_download("lakshmi25npathi/imdb-dataset-of-50k-movie-reviews")
print("Dataset path:", path)

# Locate the CSV file within the downloaded path
file_path = os.path.join(path, "IMDB Dataset.csv")
data = pd.read_csv(file_path)

# --- 2. Data Preprocessing ---
# Convert sentiment labels to binary (1 for positive, 0 for negative)
data['sentiment'] = data['sentiment'].map({'positive': 1, 'negative': 0})

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data['review'], data['sentiment'], test_size=0.2, random_state=42
)

# Initialize and fit the tokenizer
vocab_size = 5000
max_length = 100
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(X_train)

# Convert text reviews to sequences of integers
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

# Pad sequences so they all have the same length
X_train_pad = pad_sequences(X_train_seq, maxlen=max_length)
X_test_pad = pad_sequences(X_test_seq, maxlen=max_length)

# --- 3. Model Building ---
model = Sequential([
    # Embedding layer converts integer indices to dense vectors
    Embedding(input_dim=vocab_size, output_dim=64, input_length=max_length),
    # LSTM layer handles the sequential nature of the text
    LSTM(64),
    # Dense output layer with Sigmoid for binary classification
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# --- 4. Training ---
print("\nStarting Training...")
model.fit(X_train_pad, y_train, epochs=2, batch_size=64, validation_split=0.2)

# --- 5. Evaluation ---
loss, accuracy = model.evaluate(X_test_pad, y_test)
print(f"\nTest Accuracy: {accuracy:.4f}")

# --- 6. Real-time Prediction ---
user_review = input("\nEnter a movie review to test:\n")
user_seq = tokenizer.texts_to_sequences([user_review])
user_pad = pad_sequences(user_seq, maxlen=max_length)

prediction = model.predict(user_pad)

if prediction[0][0] > 0.5:
    print(f"\nPredicted Sentiment: Positive ({prediction[0][0]:.2f})")
else:
    print(f"\nPredicted Sentiment: Negative ({prediction[0][0]:.2f})")
