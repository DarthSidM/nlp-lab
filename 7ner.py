import sklearn_crfsuite

# Function to extract features for each word in a sentence
def word2features(sentence, i):
    word = sentence[i]
    features = {
        'word.lower()': word.lower(),
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
    }
    
    # Features for the previous word
    if i > 0:
        prev_word = sentence[i-1]
        features.update({
            '-1:word.lower()': prev_word.lower(),
            '-1:word.istitle()': prev_word.istitle(),
        })
    else:
        features['BOS'] = True  # Beginning of sentence

    # Features for the next word
    if i < len(sentence) - 1:
        next_word = sentence[i+1]
        features.update({
            '+1:word.lower()': next_word.lower(),
            '+1:word.istitle()': next_word.istitle(),
        })
    else:
        features['EOS'] = True  # End of sentence
        
    return features

def sent2features(sentence):
    return [word2features(sentence, i) for i in range(len(sentence))]

# --- Training Data ---
train_sentences = [
    ["Virat", "Kohli", "plays", "for", "India"],
    ["Apple", "is", "based", "in", "California"],
    ["Elon", "Musk", "founded", "SpaceX"]
]

train_labels = [
    ["B-PER", "I-PER", "O", "O", "B-LOC"],
    ["B-ORG", "O", "O", "O", "B-LOC"],
    ["B-PER", "I-PER", "O", "B-ORG"]
]

# Prepare features for training
X_train = [sent2features(s) for s in train_sentences]
y_train = train_labels

# --- Model Initialization and Training ---
# algorithm='lbfgs' is a common default for CRF
model = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True
)
model.fit(X_train, y_train)

# --- Prediction ---
user_input = input("Enter a sentence:\n")
sentence = user_input.split()

X_test = [sent2features(sentence)]
predicted = model.predict(X_test)[0]

print("\nNamed Entities:")
for word, tag in zip(sentence, predicted):
    print(f"{word} --> {tag}")
