from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

# Collect documents from the user
print("Enter 3–5 news articles (press Enter after each one):")
documents = []
for i in range(3):
    doc = input(f"Article {i+1}: ")
    documents.append(doc)

# Convert text to a matrix of token counts (Term-Document Matrix)
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Initialize and fit the LDA model
# n_components=2 means we are looking for 2 distinct topics
lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(X)

# Extract the vocabulary
words = vectorizer.get_feature_names_out()

print("\nDiscovered Topics:")
# Iterate through the topics found by the model
for i, topic in enumerate(lda.components_):
    print(f"\nTopic {i+1}:")
    
    # Get the indices of the top 5 words for this topic
    top_word_indices = topic.argsort()[-5:][::-1]
    top_words = [words[j] for j in top_word_indices]
    
    print(", ".join(top_words))
