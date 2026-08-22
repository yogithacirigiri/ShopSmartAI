from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .database import get_products


def recommend_products(product_name, limit=5):

    products = get_products()

    if products.empty:
        return []

    products["description"] = (
        products["ProductName"].fillna("")
        + " "
        + products["CategoryName"].fillna("")
    )

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(products["description"])

    similarity = cosine_similarity(vectors)

    matches = products[
        products["ProductName"].str.lower() == product_name.lower()
    ]

    if matches.empty:
        return []

    product_index = matches.index[0]

    scores = list(enumerate(similarity[product_index]))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in scores[1:limit + 1]:

        product = products.iloc[index]

        recommendations.append({
            "ProductID": int(product["ProductID"]),
            "ProductName": product["ProductName"],
            "Category": product["CategoryName"],
            "similarity": round(float(score), 2)
        })

    return recommendations