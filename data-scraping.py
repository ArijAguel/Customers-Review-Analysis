import requests
from bs4 import BeautifulSoup

# URL cible
url = "https://expressshop.tn/reviews/"

# Envoyer une requête pour récupérer le contenu HTML
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

# Vérifier si la requête est réussie
if response.status_code == 200:
    print("Connexion réussie au site !")
else:
    print(f"Échec de la connexion. Code d'état : {response.status_code}")
    exit()

# Analyser le contenu HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Trouver tous les conteneurs d'avis
reviews = soup.find_all('div', class_='jdgm-rev')  # Adapter la classe en fonction de votre HTML

# Vérifier s'il y a des avis
if not reviews:
    print("Aucun avis trouvé sur la page.")
    exit()

i=0
# Extraire les informations de chaque avis
for review in reviews:
    i=i+1
    print (i)
    # Nom de l'auteur
    author = review.find('span', class_='jdgm-rev__author')
    author = author.text.strip() if author else "NA"

    # Date de l'avis
    date = review.find('span', class_='jdgm-rev__timestamp')
    date = date['data-content'] if date else "NA"

    # Note (score)
    rating = review.find('span', class_='jdgm-rev__rating')
    rating = rating['data-score'] if rating else "NA"

    # Titre de l'avis
    title = review.find('b', class_='jdgm-rev__title')
    title = title.text.strip() if title else "NA"

    # Contenu de l'avis
    content = review.find('div', class_='jdgm-rev__body')
    content = content.text.strip() if content else "NA"

    # Lien vers le produit
    product_link_tag = review.find('a', class_='jdgm-rev__prod-link')
    product_link = product_link_tag['href'] if product_link_tag else "NA"

    # Afficher les résultats
    print(f"Auteur : {author}")
    print(f"Date : {date}")
    print(f"Note : {rating} étoiles")
    print(f"Titre : {title}")
    print(f"Contenu : {content}")
    print(f"Lien du produit : {product_link}")
    print("-" * 50)
