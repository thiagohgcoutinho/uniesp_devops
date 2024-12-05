from flask import Flask, request, jsonify
import psycopg2


conn = psycopg2.connect(
    host="db", 
    database="product_db", 
    user="postgres", 
    password="postgres"
)

app = Flask(__name__)


@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    try:
        name = data.get("name")
        price = round(float(data.get("price", 0)), 2)  

        if not name or price <= 0:
            return jsonify({"message": "Nome inválido ou preço deve ser positivo."}), 400

        cur = conn.cursor()
        cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
        conn.commit()

        return jsonify({"message": "Produto adicionado com sucesso!"}), 201

    except (ValueError, KeyError):
        return jsonify({"message": "Erro ao processar os dados."}), 400


@app.route("/products", methods=["GET"])
def get_products():
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name, price FROM products ORDER BY id ASC")
        products = cur.fetchall()

        
        result = [
            {"id": prod[0], "name": prod[1], "price": float(prod[2])} for prod in products
        ]
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"message": "Erro ao buscar produtos.", "error": str(e)}), 500


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()

    try:
        name = data.get("name")
        price = round(float(data.get("price", 0)), 2)

        if not name or price <= 0:
            return jsonify({"message": "Nome inválido ou preço deve ser positivo."}), 400

        cur = conn.cursor()
        cur.execute(
            "UPDATE products SET name = %s, price = %s WHERE id = %s",
            (name, price, product_id)
        )
        conn.commit()

        if cur.rowcount == 0:
            return jsonify({"message": "Produto não encontrado."}), 404

        return jsonify({"message": "Produto atualizado com sucesso!"}), 200

    except (ValueError, KeyError):
        return jsonify({"message": "Erro ao processar os dados."}), 400


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()

        if cur.rowcount == 0:
            return jsonify({"message": "Produto não encontrado."}), 404

        return jsonify({"message": "Produto excluído com sucesso!"}), 200

    except Exception as e:
        return jsonify({"message": "Erro ao excluir o produto.", "error": str(e)}), 500


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name, price FROM products WHERE id = %s", (product_id,))
        product = cur.fetchone()

        if not product:
            return jsonify({"message": "Produto não encontrado."}), 404

        result = {"id": product[0], "name": product[1], "price": float(product[2])}
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"message": "Erro ao buscar o produto.", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)