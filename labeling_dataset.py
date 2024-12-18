import pandas as pd
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf

# === Étape 1 : Charger les données ===
df = pd.read_csv('cleaned_reviews.csv')

# Vérifiez que la colonne 'cleaned_content' existe
if 'cleaned_content' not in df.columns:
    raise ValueError("Le fichier CSV doit contenir une colonne 'cleaned_content' avec les textes prétraités.")

# === Étape 2 : Charger le modèle et le tokenizer ===
model_name = "khaledsoudy/arabic-sentiment-bert-model"

# Charger le tokenizer
print("Chargement du tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Charger le modèle TensorFlow
print("Chargement du modèle...")
model = TFAutoModelForSequenceClassification.from_pretrained(model_name)

# === Étape 3 : Tokenisation et mise en lot ===
print("Tokenisation des textes...")
# Convertir les textes en tokens
encoded_texts = tokenizer(
    df['cleaned_content'].tolist(),
    max_length=128,  # Limite de longueur des séquences
    truncation=True,  # Tronquer les séquences trop longues
    padding=True,  # Ajouter du padding
    return_tensors="tf"  # Format TensorFlow
)

# === Étape 4 : Prédire les sentiments ===
print("Prédiction des sentiments...")
# Effectuer les prédictions
predictions = model(encoded_texts["input_ids"]).logits

# Convertir les logits en probabilités avec la fonction softmax
probabilities = tf.nn.softmax(predictions, axis=1)

# Identifier les labels de sentiment : 0 (négatif) ou 1 (positif)
labels = tf.argmax(probabilities, axis=1).numpy()

# Ajouter les résultats au DataFrame
df['sentiment'] = ['positive' if label == 1 else 'negative' for label in labels]

# === Étape 5 : Sauvegarder les résultats ===
output_file = 'classified_reviews.csv'
df.to_csv(output_file, index=False)
# === Étape 5 : Sauvegarder les résultats dans un fichier Excel ===
output_file1 = 'classified_reviews.xlsx'

# Utiliser pandas pour sauvegarder dans un fichier Excel
df.to_excel(output_file1, index=False, engine='openpyxl')  # Spécifiez openpyxl comme moteur pour écrire au format xlsx

print(f"Analyse de sentiment terminée. Les résultats sont enregistrés dans '{output_file}'.")