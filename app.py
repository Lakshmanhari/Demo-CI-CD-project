from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage
products = []
orders = []


@app.route("/")
def home():
    return jsonify({"message": "Mini E-Commerce Service Running"})


# ---------------- PRODUCTS ----------------

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


# ---------------- ORDERS ----------------

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json

    order = {
        "id": len(orders) + 1,
        "product_id": data.get("product_id"),
        "quantity": data.get("quantity"),
        "created_at": datetime.utcnow().isoformat()
    }

    orders.append(order)
    return jsonify(order), 201


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


# ---------------- HEALTH ----------------

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

