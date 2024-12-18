import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



# Charger les données
data = pd.read_csv('reviews.csv')  # Ou  pd.read_excel('reviews.xlsx)
print(data.head())

# Supprimer les lignes vides
data.dropna(inplace=True)
print(data.info())


data = data[['title', 'rating', 'content']]


# Télécharger les stopwords
nltk.download('stopwords')
nltk.download('wordnet')

# Initialiser lemmatizer
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()  # Convertir en minuscules
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Supprimer les URL
    text = re.sub(r'\d+', '', text)  # Supprimer les chiffres
    text = re.sub(r'[^\w\s]', '', text)  # Supprimer les caractères spéciaux
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()
                     if word not in stopwords.words('english')])  # Retirer les stopwords
    return text

data['cleaned_content'] = data['content'].apply(clean_text)
print(data.head())


# Exporter le fichier nettoyé au format CSV
data.to_csv('cleaned_reviews.csv', index=False, encoding='utf-8')
print("Les données nettoyées ont été exportées dans 'cleaned_reviews.csv'")

# Save to an Excel file
excel_file = "cleaned_reviews.xlsx"
data = pd.DataFrame(data)
data.to_excel(excel_file, index=False)

print(f"Reviews also saved to {excel_file}")

