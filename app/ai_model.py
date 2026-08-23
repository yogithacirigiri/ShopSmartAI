from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .database import get_products


def recommend_products(product_name, limit=5):

    products = get_products()

    if products.empty:
        return []

    # Make sure text columns do not contain null values
    products["ProductName"] = products["ProductName"].fillna("").astype(str)
    products["CategoryName"] = products["CategoryName"].fillna("").astype(str)

    # Combine product name and category
    products["description"] = (
        products["ProductName"] + " " +
        products["CategoryName"]
    )

    # Convert product information into TF-IDF vectors
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2)
    )

    vectors = vectorizer.fit_transform(products["description"])

    # Calculate cosine similarity
    similarity = cosine_similarity(vectors)

    # Find selected product
    product_name_clean = product_name.strip().lower()

    matches = products[
        products["ProductName"].str.strip().str.lower()
        == product_name_clean
    ]

    if matches.empty:
        return []

    product_index = matches.index[0]

    # Get similarity scores
    scores = list(enumerate(similarity[product_index]))

    # Sort from highest to lowest similarity
    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in scores:

        # Don't recommend the selected product itself
        if index == product_index:
            continue

        product = products.iloc[index]

        recommendations.append({
            "ProductID": int(product["ProductID"]),
            "ProductName": product["ProductName"],
            "Category": product["CategoryName"],
            "similarity": round(float(score), 2)
        })

        if len(recommendations) >= limit:
            break

    return recommendations