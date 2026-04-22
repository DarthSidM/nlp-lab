import re
def word_tokenizer(text):
    tokens = re.findall(r"\b\w+(?:'\w+)?\b", text)
    return tokens
input_text = input("Enter a sentence: ")
tokens = word_tokenizer(input_text)
print("\nTokenized Words:")
for word in tokens:
print(word)
