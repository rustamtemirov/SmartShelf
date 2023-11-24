from flask import request, jsonify
from app import app, db
from models import Shelf

# Create a new shelf
@app.route('/api/shelf', methods=['POST'])
def create_shelf():
    data = request.get_json()

    new_shelf = Shelf(
        name=data['name'],
        owner=data['owner']
    )

    db.session.add(new_shelf)
    db.session.commit()

    return jsonify({'message': 'Shelf created successfully'}), 201

# Get all shelves
@app.route('/api/shelf', methods=['GET'])
def get_all_shelves():
    shelves = Shelf.query.all()
    shelf_list = [{'id': shelf.id, 'name': shelf.name, 'owner': shelf.owner} for shelf in shelves]
    return jsonify({'shelves': shelf_list})

# Get a specific shelf by ID
@app.route('/api/shelf/<int:shelf_id>', methods=['GET'])
def get_shelf(shelf_id):
    shelf = Shelf.query.get_or_404(shelf_id)
    shelf_data = {'id': shelf.id, 'name': shelf.name, 'owner': shelf.owner}
    return jsonify({'shelf': shelf_data})

# Update a shelf by ID
@app.route('/api/shelf/<int:shelf_id>', methods=['PUT'])
def update_shelf(shelf_id):
    shelf = Shelf.query.get_or_404(shelf_id)
    data = request.get_json()

    shelf.name = data['name']
    shelf.owner = data['owner']

    db.session.commit()

    return jsonify({'message': 'Shelf updated successfully'})

# Delete a shelf by ID
@app.route('/api/shelf/<int:shelf_id>', methods=['DELETE'])
def delete_shelf(shelf_id):
    shelf = Shelf.query.get_or_404(shelf_id)
    db.session.delete(shelf)
    db.session.commit()

    return jsonify({'message': 'Shelf deleted successfully'})
