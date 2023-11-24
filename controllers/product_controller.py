from flask import request, jsonify
from app import app, db
from models import Product

# Create a new product
@app.route('/api/product', methods=['POST'])
def create_product():
    data = request.get_json()

    new_product = Product(
        name=data['name'],
        shelf_id=data['shelf_id'],
        expiration_date=data['expiration_date']
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product created successfully'}), 201

# Get all products
@app.route('/api/product', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    product_list = [{'id': product.id, 'name': product.name, 'shelf_id': product.shelf_id, 'expiration_date': product.expiration_date} for product in products]
    return jsonify({'products': product_list})

# Get a specific product by ID
@app.route('/api/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    product_data = {'id': product.id, 'name': product.name, 'shelf_id': product.shelf_id, 'expiration_date': product.expiration_date}
    return jsonify({'product': product_data})

# Update a product by ID
@app.route('/api/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()

    product.name = data['name']
    product.shelf_id = data['shelf_id']
    product.expiration_date = data['expiration_date']

    db.session.commit()

    return jsonify({'message': 'Product updated successfully'})

# Delete a product by ID
@app.route('/api/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully'})
