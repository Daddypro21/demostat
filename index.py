

# import requests
# from bs4 import BeautifulSoup

# # URL de la page d'accueil de FranceTV Info
# url = "https://www.francetvinfo.fr/"

# # Envoie de la requête HTTP
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # Récupération des liens vers les articles (structure propre au site)
# articles = soup.select("a.js-article-title")  # classe utilisée pour les liens d’articles

# for article in articles[:5]:  # Limité à 5 pour éviter de surcharger
#     lien = article.get("href")

#     if not lien.startswith("http"):
#         lien = "https://www.francetvinfo.fr" + lien

#     print(f"\n--- Article : {article.text.strip()} ---\n")
#     print(f"URL : {lien}")

#     try:
#         # Charger la page de l'article
#         article_response = requests.get(lien)
#         article_soup = BeautifulSoup(article_response.text, "html.parser")

#         # Récupération du contenu textuel de l’article
#         paragraphes = article_soup.select("div.article-body p")

#         for p in paragraphes:
#             texte = p.get_text(strip=True)
#             if texte:
#                 print(texte)
#     except Exception as e:
#         print("Erreur lors du chargement de l'article :", e)






import requests
from bs4 import BeautifulSoup


# URL cible
url = "https://www.wibegin.com/blog"

# Requête
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Scraping des titres d’actualités
titres = soup.find_all("p")
contents = soup.find_all("p")

for titre in titres:
    print(titre.text.strip())
    

# for content in contents:
#     print(content.text.strip())
