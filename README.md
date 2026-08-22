Your README content is good, but there is **one important problem**: the screenshot paths are pointing to your **Windows computer paths**. Those will not work for people viewing your GitHub repository.

You currently have:

```markdown
![ShopSmart AI Website]("C:\Users\C.Yogitha\OneDrive\Documents\ShopSmartDB\ss\shop smart ai.png")
```

GitHub needs the **repository-relative path** instead:

```markdown
![ShopSmart AI Website](ss/shop%20smart%20ai.png)
```

Also, your Markdown has a lot of unnecessary `**` and escaped characters because it looks like it was copied from formatted text.

### I recommend replacing your entire README with this clean version

````markdown
# ShopSmart AI 🛍️🤖

ShopSmart AI is a full-stack AI-powered e-commerce application that combines machine learning, REST APIs, SQL Server, and a web-based frontend to provide intelligent product recommendations and sales insights.

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

When a user selects a product, the system analyzes product similarity and recommends similar products.

## 🏗️ System Architecture

```text
Frontend
HTML + CSS + JavaScript
        ↓
FastAPI REST API
        ↓
Python AI/ML Model
        ↓
Microsoft SQL Server
````

Power BI is also connected to the database for sales analytics.

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
* TF-IDF
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

## 🗄️ Database

The application uses the following SQL Server tables:

* Customers
* Categories
* Products
* Orders
* OrderDetails

### Main relationships

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

## 📊 Business Insights

The current dataset contains 15 orders.

Key findings include:

* January is the best-performing month with ₹95,996 revenue.
* Customer 1 generated ₹89,997 revenue.
* Apple iPhone 15 generated ₹159,998 revenue.
* Electronics is the highest-revenue category with ₹395,991.
* Average order value is approximately ₹23,685.53.

## ⚙️ Installation

### Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Move into the project

```bash
cd ShopSmartDB
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it on Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## 🔌 Database Configuration

The application currently connects to SQL Server using:

```text
localhost\SQLEXPRESS
```

Database:

```text
ShopSmartDB
```

Make sure SQL Server Express is running and the required database and tables are available.

## ▶️ Run the Application

Start the FastAPI server:

```bash
python -m uvicorn app.main:app
```

Open the application:

```text
http://127.0.0.1:8000
```

FastAPI API documentation:

```text
http://127.0.0.1:8000/docs
```

## 🔗 API Endpoints

| Endpoint                    | Description            |
| --------------------------- | ---------------------- |
| `/`                         | Web application        |
| `/products`                 | Get products           |
| `/recommend/{product_name}` | Get AI recommendations |
| `/customer/{customer_id}`   | Get customer orders    |
| `/analytics`                | Get sales analytics    |

## 📈 Power BI Dashboard

The project also includes a Power BI sales dashboard containing:

* Total Revenue
* Total Orders
* Average Order Value
* Monthly Revenue
* Revenue by Category
* Top Products by Revenue
* Top Customers by Revenue
* Category filter
* Order Date filter

## 📸 Project Screenshots

### ShopSmart AI Website

![ShopSmart AI Website](ss/shop%20smart%20ai.png)

### AI Product Recommendation

![AI Recommendation](ss/shop%20smart%20ai%202%20.png)

### Power BI Sales Dashboard

![Power BI Dashboard](ss/shopsmart%20dashboad.png)

## 🔮 Future Improvements

* Sales prediction using machine learning
* Customer segmentation
* Personalized recommendations
* AI chatbot
* User authentication
* Shopping cart and checkout
* Cloud deployment
* Real-time recommendation updates

## 👩‍💻 Author

**Yogitha Cirigiri**

B.Tech – Computer Science & Engineering (AI & ML)

## ⭐ Project Goal

The goal of ShopSmart AI is to demonstrate the integration of:

**AI + Machine Learning + Full-Stack Development + SQL + Data Analytics**

in a practical e-commerce application.

````

