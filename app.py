from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

products = []
orders = []

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Mini E-Commerce</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        input, button { padding: 8px; margin: 5px; }
        .card { border: 1px solid #ccc; padding: 10px; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>🛒 Mini E-Commerce Dashboard</h1>

    <h2>Add Product</h2>
    <input id="name" placeholder="Product Name">
    <input id="price" placeholder="Price">
    <button onclick="addProduct()">Add</button>

    <h2>Products</h2>
    <div id="products"></div>

    <script>
        async function loadProducts(){
            const res = await fetch('/products');
            const data = await res.json();
            const div = document.getElementById('products');
            div.innerHTML = '';
            data.forEach(p=>{
                div.innerHTML += `<div class="card">${p.name} - ₹${p.price}</div>`;
            });
        }

        async function addProduct(){
            const name = document.getElementById('name').value;
            const price = document.getElementById('price').value;

            await fetch('/products', {
                method: 'POST',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify({name, price})
            });

            loadProducts();
        }

        loadProducts();
    </script>
</body>
</html>
"""


@app.route("/")
def dashboard():
    return render_template_string(HTML_PAGE)


@app.route("/products", methods=["POST"])
def add_product():
    data = request.json

    product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price"),
        "created_at": datetime.utcnow().isoformat()
    }

    products.append(product)
    return jsonify(product), 201


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

