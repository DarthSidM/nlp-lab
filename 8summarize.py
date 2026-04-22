import re
from collections import defaultdict

def summarize_text(text):
    # Split text into sentences using regex (looks for . ! or ? followed by a space)
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    # Extract all words and calculate their frequency across the whole text
    words = re.findall(r'\w+', text.lower())
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1
    
    # Score each sentence based on the frequency of the words it contains
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = re.findall(r'\w+', sentence.lower())
        score = sum(freq[word] for word in sentence_words)
        sentence_scores[sentence] = score
    
    # Return the sentence with the highest score
    if not sentence_scores:
        return ""
        
    best_sentence = max(sentence_scores, key=sentence_scores.get)
    return best_sentence

# --- Main Execution ---
article = input("Enter a long article:\n")
if article.strip():
    summary = summarize_text(article)
    print("\nSummary (Top Sentence):")
    print(summary)
else:
    print("No text provided.")
