# A simple English-to-French dictionary mapping
translation_dict = {
    "hello": "bonjour",
    "hi": "salut",
    "how": "comment",
    "are": "êtes",
    "you": "vous",
    "i": "je",
    "am": "suis",
    "fine": "bien",
    "thank": "merci",
    "thanks": "merci",
    "good": "bon",
    "morning": "matin",
    "night": "nuit",
    "bye": "au revoir",
    "food": "nourriture",
    "water": "eau",
    "friend": "ami"
}

def translate(sentence):
    # Normalize input and split into a list of words
    words = sentence.lower().split()
    translated = []
    
    for word in words:
        # Get the translated word; if not found, keep the original word
        translated_word = translation_dict.get(word, word)
        translated.append(translated_word)
        
    return ' '.join(translated)

# --- Execution ---
english_sentence = input("Enter a short English sentence:\n")

if english_sentence.strip():
    french_sentence = translate(english_sentence)
    print("\nTranslated Sentence (French):")
    print(french_sentence)
else:
    print("Please enter a valid sentence.")
