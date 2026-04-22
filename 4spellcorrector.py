import re
from collections import Counter
def words(text):
    return re.findall(r'\w+', text.lower())
def train(text):
    return Counter(words(text))
text_data = input("Enter a paragraph (this will act as dictionary data):\n")
WORD_COUNTS = train(text_data)
def P(word):
    N = sum(WORD_COUNTS.values())
    return WORD_COUNTS[word] / N if N > 0 else 0
def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
    deletes = [L + R[1:] for L, R in splits if R]
    inserts = [L + c + R for L, R in splits for c in letters]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    return set(deletes + inserts + replaces + transposes)
def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
def known(words_list):
    return set(w for w in words_list if w in WORD_COUNTS)
def candidates(word):u
    return (known([word]) or
known(edits1(word)) or
known(edits2(word)) or
[word])
def correction(word):
    return max(candidates(word), key=P)
input_word = input("\nEnter a word to correct:\n")
print("\nCorrected Word:")
print(correction(input_word))
