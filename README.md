# ShopSmart AI 🛍️🤖

ShopSmart AI is a full-stack AI-powered e-commerce application that combines Machine Learning, FastAPI REST APIs, Microsoft SQL Server, Python data analytics, and a responsive web frontend.

The application provides AI-based product recommendations and sales insights through an interactive web application and Power BI dashboard.

---

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

---

## 🧠 AI Recommendation System

ShopSmart AI uses a **content-based product recommendation system**.

The recommendation engine uses:

- TF-IDF Vectorization
- Cosine Similarity
- Product names
- Product categories

When a user selects a product, the system analyzes product similarity and recommends similar products.

### Recommendation Process

```text
Product Selection
       ↓
Product Name + Category
       ↓
TF-IDF Vectorization
       ↓
Cosine Similarity
       ↓
Similar Products
       ↓
AI Recommendations
````

---

## 🏗️ System Architecture

```text
                    ShopSmart AI
                         │
                         ▼
              HTML + CSS + JavaScript
                         │
                         ▼
                  FastAPI REST API
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Python AI/ML Model     SQL Server Database
              │                     │
              ▼                     ▼
      TF-IDF + Cosine       Products / Customers
         Similarity          Orders / Categories
              │
              └──────────┬──────────┘
                         ▼
                  Application Results


             SQL Server Database
                       │
                       ▼
                   Power BI
                       │
                       ▼
              Sales Dashboard
```

---

## 🛠️ Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### AI / Machine Learning

* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity

### Database

* Microsoft SQL Server
* SQL Server Express
* pyodbc

### Data Analytics

* Pandas
* Power BI

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 📁 Project Structure

```text
ShopSmartAI/
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
├── ss/
│   ├── shop smart ai.png
│   ├── shop smart ai 2 .png
│   └── shopsmart dashboad.png
│
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🗄️ Database

The application uses **Microsoft SQL Server**.

### Database

```text
ShopSmartDB
```

### SQL Server Instance

```text
localhost\SQLEXPRESS
```

### Tables

* Customers
* Categories
* Products
* Orders
* OrderDetails

### Database Relationships

```text
Customers
    ↓
Orders
    ↓
OrderDetails
    ↓
Products
    ↓
Categories
```

---

## 📊 Business Insights

The current dataset contains **15 orders**.

Key findings from the dataset:

| Business Metric       |          Result |
| --------------------- | --------------: |
| Best Performing Month |         January |
| January Revenue       |         ₹95,996 |
| Top Customer          |      Customer 1 |
| Top Customer Revenue  |         ₹89,997 |
| Top Product           | Apple iPhone 15 |
| Top Product Revenue   |        ₹159,998 |
| Top Category          |     Electronics |
| Electronics Revenue   |        ₹395,991 |
| Average Order Value   |      ₹23,685.53 |

These insights were generated using **Python and Pandas** and visualized using **Power BI**.

---

## 📈 Power BI Dashboard

The project includes an interactive Power BI sales dashboard containing:

* Total Revenue
* Total Orders
* Average Order Value
* Monthly Revenue
* Revenue by Category
* Top Products by Revenue
* Top Customers by Revenue
* Category filter
* Order Date filter

---

## 📸 Project Screenshots

### 🛍️ ShopSmart AI Website

[![ShopSmart AI Website](ss/shop%20smart%20ai.png)](ss/shop%20smart%20ai.png)

**Click the image to view the full-size screenshot.**

---

### 🤖 AI Product Recommendation

[![AI Product Recommendation](ss/shop%20smart%20ai%202%20.png)](ss/shop%20smart%20ai%202%20.png)

**Click the image to view the full-size screenshot.**

---

### 📊 Power BI Sales Dashboard

[![Power BI Sales Dashboard](ss/shopsmart%20dashboad.png)](ss/shopsmart%20dashboad.png)

**Click the image to view the full-size screenshot.**

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yogithacirigiri/ShopSmartAI.git
```

### 2. Open the project

```bash
cd ShopSmartAI
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment on Windows

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔌 Database Configuration

The application currently connects to SQL Server using:

```text
localhost\SQLEXPRESS
```

Database:

```text
ShopSmartDB
```

Make sure:

1. SQL Server Express is installed.
2. SQL Server is running.
3. The `ShopSmartDB` database exists.
4. The required tables are available.
5. Windows Authentication is configured.

> Note: This project is currently configured for local SQL Server development.

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
python -m uvicorn app.main:app
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

FastAPI API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

| Endpoint                    | Description                    |
| --------------------------- | ------------------------------ |
| `/`                         | Web application                |
| `/products`                 | Get available products         |
| `/recommend/{product_name}` | Get AI product recommendations |
| `/customer/{customer_id}`   | Get customer orders            |
| `/analytics`                | Get sales analytics            |

---

## 🔮 Future Improvements

* 📈 Sales prediction using Machine Learning
* 👥 Customer segmentation
* 🎯 Personalized recommendations
* 🤖 AI chatbot
* 🔐 User authentication
* 🛒 Shopping cart and checkout
* ⚡ Real-time recommendation updates
* ☁️ Cloud deployment

---

## 👩‍💻 Author

**Yogitha Cirigiri**

B.Tech – Computer Science & Engineering (AI & ML)

---

## ⭐ Project Goal

The goal of ShopSmart AI is to demonstrate the integration of:

**AI + Machine Learning + Full-Stack Development + SQL + Data Analytics**

in a practical e-commerce application.

````
