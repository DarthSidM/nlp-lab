import re
from gensim.models import Word2Vec

def preprocess(text):
    # Split text into sentences based on periods
    sentences = text.split('.')
    processed = []
    
    for sentence in sentences:
        # Extract alphanumeric words and lowercase them
        words = re.findall(r'\w+', sentence.lower())
        if words:
            processed.append(words)
    return processed

# --- Data Collection ---
print("Enter a small corpus (3–5 sentences):")
corpus = input()
processed_corpus = preprocess(corpus)

# --- Model Training ---
# vector_size: dimensionality of the word vectors
# window: maximum distance between the current and predicted word
# min_count: ignores words with total frequency lower than this
model = Word2Vec(
    sentences=processed_corpus, 
    vector_size=50, 
    window=2, 
    min_count=1, 
    workers=1
)

# --- Similarity Query ---
word = input("\nEnter a word from your text to find similar words:\n").lower()

if word in model.wv:
    print(f"\nWords similar to '{word}':")
    similar_words = model.wv.most_similar(word)
    for w, score in similar_words:
        print(f"{w} ({score:.2f})")
else:
    print(f"\nWord '{word}' not found in vocabulary.")
