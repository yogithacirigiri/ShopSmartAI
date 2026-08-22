const API = "";


async function loadProducts() {

    const response = await fetch(`${API}/products`);

    const products = await response.json();

    const productList =
        document.getElementById("product-list");

    const select =
        document.getElementById("productSelect");

    productList.innerHTML = "";

    products.forEach(product => {

        const card = document.createElement("div");

        card.className = "product-card";

        card.innerHTML = `
            <h3>${product.ProductName}</h3>
            <p>Category: ${product.CategoryName}</p>
        `;

        productList.appendChild(card);


        const option = document.createElement("option");

        option.value = product.ProductName;

        option.textContent = product.ProductName;

        select.appendChild(option);

    });
}


async function getRecommendations() {

    const product =
        document.getElementById("productSelect").value;

    if (!product) {

        alert("Please select a product.");

        return;
    }


    const response =
        await fetch(
            `/recommend/${encodeURIComponent(product)}`
        );


    const data = await response.json();


    const container =
        document.getElementById("recommendations");

    container.innerHTML = "";


    if (data.recommendations.length === 0) {

        container.innerHTML =
            "<p>No recommendations found.</p>";

        return;
    }


    data.recommendations.forEach(item => {

        const card =
            document.createElement("div");

        card.className = "product-card";

        card.innerHTML = `
            <h3>${item.ProductName}</h3>
            <p>Category: ${item.Category}</p>
            <p>AI Similarity: ${item.similarity}</p>
        `;

        container.appendChild(card);

    });
}


async function loadAnalytics() {

    const response =
        await fetch("/analytics");

    const data =
        await response.json();


    document.getElementById("revenue").textContent =
        "₹" + data.total_revenue.toLocaleString("en-IN");


    document.getElementById("orders").textContent =
        data.total_orders;


    document.getElementById("average").textContent =
        "₹" + data.average_order_value.toLocaleString("en-IN", {
            maximumFractionDigits: 2
        });
}


loadProducts();

loadAnalytics();