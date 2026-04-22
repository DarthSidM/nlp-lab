import re
def text_normalizer(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F700-\U0001F77F"
    "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
input_text = "<div>Hey there! Check out https://mysite.com today!!</div> Learning NLP is fun."
normalized_text = text_normalizer(input_text)
print("Original Text:")
print(input_text)
print("\nNormalized Text:")
print(normalized_text)
