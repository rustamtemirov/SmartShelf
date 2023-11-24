from flask import request, jsonify
from app import app, db
from models import User

# Create a new user
@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = User(
        username=data['username'],
        password_hash=data['password_hash'],
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

# Get all users
@app.route('/api/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify({'users': user_list})

# Get a specific user by ID
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    user_data = {'id': user.id, 'username': user.username, 'email': user.email}
    return jsonify({'user': user_data})

# Update a user by ID
@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    user.username = data['username']
    user.email = data['email']
    user.first_name = data['first_name']
    user.last_name = data['last_name']

    db.session.commit()

    return jsonify({'message': 'User updated successfully'})

# Delete a user by ID
@app.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'})
