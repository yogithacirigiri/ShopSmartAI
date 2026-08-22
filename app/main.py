from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .database import (
    get_products,
    get_sales,
    get_customer_orders
)

from .ai_model import recommend_products


app = FastAPI(
    title="ShopSmart AI",
    description="AI-powered e-commerce recommendation system",
    version="1.0"
)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/products")
def products():

    df = get_products()

    return df.to_dict(orient="records")


@app.get("/recommend/{product_name}")
def recommend(product_name: str):

    recommendations = recommend_products(product_name)

    return {
        "product": product_name,
        "recommendations": recommendations
    }


@app.get("/customer/{customer_id}")
def customer(customer_id: int):

    df = get_customer_orders(customer_id)

    return {
        "customer_id": customer_id,
        "orders": df.to_dict(orient="records")
    }


@app.get("/analytics")
def analytics():

    df = get_sales()

    total_revenue = float(df["TotalAmount"].sum())
    total_orders = int(len(df))
    average_order = float(df["TotalAmount"].mean())

    best_order = df.loc[df["TotalAmount"].idxmax()]

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "average_order_value": average_order,
        "highest_order": float(best_order["TotalAmount"])
    }