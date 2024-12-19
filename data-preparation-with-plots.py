#### This File prepares the data but with plots
#### It modifies the csv file !!! 
#### To run only 1 time to see the plots 
#### And then rerun data-preparation.py to save the csv file that we're gonna use for the model training

import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud

# Charger les données
data = pd.read_csv('reviews.csv')  # Ou  pd.read_excel('reviews.xlsx')
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

# Word count before cleaning
data['word_count_before'] = data['content'].apply(lambda x: len(str(x).split()))

# Appliquer la fonction de nettoyage
data['cleaned_content'] = data['content'].apply(clean_text)

# Word count after cleaning
data['word_count_after'] = data['cleaned_content'].apply(lambda x: len(str(x).split()))

# Visualisation: Distribution des comptes de mots avant et après nettoyage
plt.figure(figsize=(10, 6))
plt.hist(data['word_count_before'], bins=30, alpha=0.5, label='Before Cleaning')
plt.hist(data['word_count_after'], bins=30, alpha=0.5, label='After Cleaning')
plt.legend()
plt.title('Word Count Distribution Before and After Cleaning')
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.show()

# Visualisation: Word Cloud avant nettoyage
wordcloud_before = WordCloud(stopwords=set(stopwords.words('english')), width=800, height=400).generate(' '.join(data['content']))
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud_before, interpolation='bilinear')
plt.title('Word Cloud Before Cleaning')
plt.axis('off')
plt.show()

# Visualisation: Word Cloud après nettoyage
wordcloud_after = WordCloud(stopwords=set(stopwords.words('english')), width=800, height=400).generate(' '.join(data['cleaned_content']))
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud_after, interpolation='bilinear')
plt.title('Word Cloud After Cleaning')
plt.axis('off')
plt.show()

# Exporter le fichier nettoyé au format CSV
data.to_csv('cleaned_reviews.csv', index=False, encoding='utf-8')
print("Les données nettoyées ont été exportées dans 'cleaned_reviews.csv'")

# Save to an Excel file
excel_file = "cleaned_reviews.xlsx"
data = pd.DataFrame(data)
data.to_excel(excel_file, index=False)

print(f"Reviews also saved to {excel_file}")
