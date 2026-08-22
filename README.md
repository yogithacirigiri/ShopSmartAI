# ShopSmart AI 🛍️🤖

ShopSmart AI is a full-stack AI-powered e-commerce application that combines
machine learning, REST APIs, SQL Server, and a web-based frontend to provide
intelligent product recommendations and sales insights.

## 🚀 Features

- 🛍️ Product catalog
- 🤖 AI-based product recommendations
- 📊 Sales analytics
- 👤 Customer order information
- 💰 Revenue and order statistics
- 🔌 REST APIs using FastAPI
- 🗄️ Microsoft SQL Server database
- 📈 Power BI sales dashboard
- 💻 Responsive web interface

## 🧠 AI Recommendation System

ShopSmart AI uses a content-based recommendation approach.

The recommendation engine uses:

- TF-IDF Vectorization
- Cosine Similarity
- Product names
- Product categories

When a user selects a product, the system analyzes product similarity
and recommends similar products.

## 🏗️ System Architecture

Frontend
↓
HTML + CSS + JavaScript
↓
FastAPI REST API
↓
Python AI/ML Model
↓
Microsoft SQL Server

Power BI is also connected to the database for sales analytics.

## 🛠️ Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### AI / Machine Learning
- Scikit-learn
- TF-IDF
- Cosine Similarity

### Database
- Microsoft SQL Server
- SQL Server Express
- pyodbc

### Data Analytics
- Pandas
- Power BI

### Development Tools
- Visual Studio Code
- Git
- GitHub

## 📁 Project Structure

```text
ShopSmartDB/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── ai_model.py
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── database.py
├── requirements.txt
├── README.md
└── .gitignore

#### 🗄️ Database

The application uses the following SQL Server tables:

Customers
Categories
Products
Orders
OrderDetails

Main relationships:

Customers
    ↓
Orders
    ↓
OrderDetails
    ↓
Products
    ↓
Categories

#### 📊 Business Insights

The current dataset contains 15 orders.

Key findings include:

January is the best-performing month with ₹95,996 revenue.
Customer 1 generated ₹89,997 revenue.
Apple iPhone 15 generated ₹159,998 revenue.
Electronics is the highest-revenue category with ₹395,991.
Average order value is approximately ₹23,685.53.
#### ⚙️ Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project:

cd ShopSmartDB

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

#### 🔌 Database Configuration

The application currently connects to SQL Server using:

localhost\SQLEXPRESS

and the database:

ShopSmartDB

Make sure SQL Server Express is running and the required database and
tables are available.

#### ▶️ Run the Application

Start the FastAPI server:

python -m uvicorn app.main:app

Open the application in your browser:

http://127.0.0.1:8000

FastAPI API documentation is available at:

http://127.0.0.1:8000/docs

#### 🔗 API Endpoints
Endpoint	                        Description
/	                                Web application
/products	                         Get products
/recommend/{product_name}	        Get AI recommendations
/customer/{customer_id}         	Get customer orders
/analytics	                        Get sales analytics

#### 
📈 Power BI Dashboard

The project also includes a Power BI sales dashboard containing:

Total Revenue
Total Orders
Average Order Value
Monthly Revenue
Revenue by Category
Top Products by Revenue
Top Customers by Revenue
Category filter
Order Date filter
**
#### 🔮 Future Improvements**
Sales prediction using machine learning
Customer segmentation
Personalized recommendations
AI chatbot
User authentication
Shopping cart and checkout
Cloud deployment
Real-time recommendation updates
**
👩‍💻 Author**
**Yogitha Cirigiri**

B.Tech – Computer Science & Engineering (AI & ML)

⭐** Project Goal**

The goal of ShopSmart AI is to demonstrate the integration of:

**AI + Machine Learning + Full-Stack Development + SQL + Data Analytics **

in a practical e-commerce application.