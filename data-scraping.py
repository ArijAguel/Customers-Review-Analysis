import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests

print ("testtttttt")

base_url = "https://cdn.judge.me/reviews/all_reviews_js_based"
params = {
    "url": "expressshop.tn",
    "shop_domain": "expressshop.tn",
    "platform": "woocommerce",
    "sort_by": "created_at",
    "sort_dir": "desc",
    "page": 1,
    "review_type": "product-reviews"
}

total_reviews = []

while True:
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch reviews: HTTP {response.status_code}")
        break

    data = response.json()
    html_content = data.get('html', '')
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    reviews = soup.find_all("div", class_="jdgm-rev")

    if not reviews:
        print("No more reviews to fetch.")
        break

    for review in reviews:
        # Extract reviewer name
        author = review.find("span", class_="jdgm-rev__author")
        author = author.text.strip() if author else "N/A"

        # Extract rating
        rating = review.find("span", class_="jdgm-rev__rating")
        rating = rating['data-score'] if rating else "N/A"

        # Extract review date
        date = review.find("span", class_="jdgm-rev__timestamp")
        date = date['data-content'] if date else "N/A"

        # Extract review text
        content = review.find("div", class_="jdgm-rev__body")
        content = content.text.strip() if content else "N/A"

        # Extract product title
        title = review.find("b", class_="jdgm-rev__title")
        title = title.text.strip() if title else "N/A"

        # Extract product link
        product_link = review.find("a", class_="jdgm-rev__prod-link")
        product_link = product_link['href'] if product_link else "N/A"

        # Add review details to the list
        total_reviews.append({
            "author": author,
            "rating": rating,
            "date": date,
            "content": content,
            "title": title,
            "product_link": product_link,
        })

    # Move to the next page
    params["page"] += 1

# Print the total reviews fetched
print(f"Total reviews fetched: {len(total_reviews)}")
for review in total_reviews:
    print(review)

# Save to a CSV file
csv_file = "reviews.csv"
with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["author", "rating", "date", "content", "title", "product_link"])
    writer.writeheader()
    writer.writerows(total_reviews)

print(f"Reviews saved to {csv_file}")

# Save to an Excel file
excel_file = "reviews.xlsx"
df = pd.DataFrame(total_reviews)
df.to_excel(excel_file, index=False)

print(f"Reviews also saved to {excel_file}")