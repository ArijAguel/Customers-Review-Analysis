import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# === Step 1: Load Prepared Data ===
# Replace 'your_reviews_file.csv' with the path to your cleaned dataset
df = pd.read_csv('your_reviews_file.csv')

# Ensure there's a 'cleaned_content' column for the text data
if 'cleaned_content' not in df.columns:
    raise ValueError("The dataset must contain a 'cleaned_content' column with preprocessed text.")

# === Step 2: Load Pretrained Model and Tokenizer ===
# Replace with the path to your saved model and tokenizer
model_path = 'arabizi_sentiment_model.h5'
tokenizer_path = 'tokenizer.json'

# Load the trained model
model = load_model(model_path)

# Load the tokenizer
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json

with open(tokenizer_path, 'r') as f:
    tokenizer_json = json.load(f)
tokenizer = tokenizer_from_json(tokenizer_json)

# === Step 3: Tokenize and Pad Text ===
# Convert text to sequences using the tokenizer
sequences = tokenizer.texts_to_sequences(df['cleaned_content'])

# Pad sequences to the maximum length used during training
max_length = 100  # Use the same max length as during training
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

# === Step 4: Predict Sentiment ===
# Predict sentiment (output is typically a score between 0 and 1)
predictions = model.predict(padded_sequences)

# Assign sentiment labels based on prediction scores
df['sentiment'] = ['positive' if score >= 0.5 else 'negative' for score in predictions]

# === Step 5: Save Results ===
# Save the results to a new CSV file
df.to_csv('classified_reviews.csv', index=False)

print("Sentiment detection completed. Results saved to 'classified_reviews.csv'.")
