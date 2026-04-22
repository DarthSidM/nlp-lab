import torch
import kagglehub
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# --- 1. Dataset Acquisition ---
# (Note: Using the path you provided)
path = kagglehub.dataset_download("saurabhshahane/fake-news-classification")
print("Path to dataset files:", path)

# --- 2. Model Setup ---
# We'll use a pre-trained BERT model fine-tuned for fake news detection
model_name = "mrm8488/bert-tiny-finetuned-fake-news-detection"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# --- 3. Prediction Function ---
def predict(text):
    # Set model to evaluation mode
    model.eval()
    
    # Tokenize and prepare input tensors
    inputs = tokenizer(
        text, 
        return_tensors="pt", 
        truncation=True, 
        padding=True, 
        max_length=128
    )
    
    # Disable gradient calculation for faster inference
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        # Get the index of the highest logit
        predicted_class = torch.argmax(logits, dim=1).item()
    
    # Mapping depends on the specific model's labels (usually 1=Real, 0=Fake)
    return "Real News" if predicted_class == 1 else "Fake News"

# --- 4. Testing ---
print("-" * 30)
text1 = "Aliens landed in India yesterday night"
print(f"Headline: {text1}")
print(f"Prediction: {predict(text1)}")

print("-" * 30)
text2 = "Government launches new digital education initiative across India"
print(f"Headline: {text2}")
print(f"Prediction: {predict(text2)}")

print("-" * 30)
user_input = input("\nEnter a custom news headline to check:\n")
if user_input.strip():
    print(f"\nPrediction: {predict(user_input)}")
