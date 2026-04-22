import random
import re
from collections import defaultdict
def preprocess(text):
# Convert to lowercase and remove unwanted characters
    text = text.lower()
    text = re.findall(r"\b\w+(?:'\w+)?\b", text)
    return text
def build_bigram_model(tokens):
    bigram_counts = defaultdict(lambda: defaultdict(int))
    unigram_counts = defaultdict(int)
    vocabulary = set(tokens)
# Count unigrams and bigrams
    for i in range(len(tokens) - 1):
        unigram_counts[tokens[i]] += 1
        bigram_counts[tokens[i]][tokens[i+1]] += 1
        unigram_counts[tokens[-1]] += 1
    return bigram_counts, unigram_counts, vocabulary
def generate_text(bigram_counts, unigram_counts, vocabulary, start_word, length=10):
    current_word = start_word.lower()
    sentence = [current_word]
    V = len(vocabulary)
    for _ in range(length - 1):
        next_words = vocabulary
        probabilities = []
# Calculate probabilities with Laplace smoothing
        for word in next_words:
            prob = (bigram_counts[current_word][word] + 1) / (unigram_counts[current_word] + V)
            probabilities.append(prob)
# Choose next word based on probabilities
        next_word = random.choices(list(next_words), weights=probabilities)[0]
        sentence.append(next_word)
        current_word = next_word
    return ' '.join(sentence)
text_input = input("Enter a paragraph (training data):\n")
start_word = input("Enter a starting word:\n")
# Preprocess text
tokens = preprocess(text_input)
bigram_counts, unigram_counts, vocabulary = build_bigram_model(tokens)
generated = generate_text(bigram_counts, unigram_counts, vocabulary, start_word)
print("\nGenerated Text:")
print(generated)
