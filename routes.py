```python
from flask import Blueprint, jsonify, request
from models import db, Photographer, Photo

main_routes = Blueprint('main_routes', __name__)

# Get all photographers
@main_routes.route('/photographers', methods=['GET'])
def get_photographers():
    """Get all photographers"""
    photographers = Photographer.query.all()
    return jsonify([{"id": p.id, "name": p.name, "bio": p.bio} for p in photographers])

# Get photographer by id
@main_routes.route('/photographers/<int:photographer_id>', methods=['GET'])
def get_photographer(photographer_id):
    """Get photographer by id"""
    photographer = Photographer.query.get(photographer_id)
    if photographer is None:
        return jsonify({"error": "Photographer not found"}), 404
    return jsonify({"id": photographer.id, "name": photographer.name, "bio": photographer.bio})

# Get all photos
@main_routes.route('/photos', methods=['GET'])
def get_photos():
    """Get all photos"""
    photos = Photo.query.all()
    return jsonify([{"id": p.id, "title": p.title, "description": p.description, "url": p.url} for p in photos])

# Get photo by id
@main_routes.route('/photos/<int:photo_id>', methods=['GET'])
def get_photo(photo_id):
    """Get photo by id"""
    photo = Photo.query.get(photo_id)
    if photo is None:
        return jsonify({"error": "Photo not found"}), 404
    return jsonify({"id": photo.id, "title": photo.title, "description": photo.description, "url": photo.url})

# Create new photographer
@main_routes.route('/photographers', methods=['POST'])
def create_photographer():
    """Create new photographer"""
    data = request.get_json()
    if 'name' not in data or 'bio' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    photographer = Photographer(name=data['name'], bio=data['bio'])
    db.session.add(photographer)
    db.session.commit()
    return jsonify({"id": photographer.id, "name": photographer.name, "bio": photographer.bio}), 201

# Create new photo
@main_routes.route('/photos', methods=['POST'])
def create_photo():
    """Create new photo"""
    data = request.get_json()
    if 'title' not in data or 'description' not in data or 'url' not in data or 'photographer_id' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    photo = Photo(title=data['title'], description=data['description'], url=data['url'], photographer_id=data['photographer_id'])
    db.session.add(photo)
    db.session.commit()
    return jsonify({"id": photo.id, "title": photo.title, "description": photo.description, "url": photo.url}), 201
```

###