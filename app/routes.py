```python
from flask import Blueprint, request, jsonify
from app import db
from app.models import Photo, Photographer
from app.schemas import PhotoSchema, PhotographerSchema

main = Blueprint('main', __name__)

# Get all photos
@main.route('/photos', methods=['GET'])
def get_photos():
    photos = Photo.query.all()
    photo_schema = PhotoSchema(many=True)
    return jsonify(photo_schema.dump(photos))

# Get a photo by id
@main.route('/photos/<int:photo_id>', methods=['GET'])
def get_photo(photo_id):
    photo = Photo.query.get(photo_id)
    if photo is None:
        return jsonify({'message': 'Photo not found'}), 404
    photo_schema = PhotoSchema()
    return jsonify(photo_schema.dump(photo))

# Create a new photo
@main.route('/photos', methods=['POST'])
def create_photo():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    photo_schema = PhotoSchema()
    errors = photo_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    photo = Photo(title=data['title'], description=data['description'], image_url=data['image_url'])
    db.session.add(photo)
    db.session.commit()
    return jsonify(photo_schema.dump(photo)), 201

# Update a photo
@main.route('/photos/<int:photo_id>', methods=['PUT'])
def update_photo(photo_id):
    photo = Photo.query.get(photo_id)
    if photo is None:
        return jsonify({'message': 'Photo not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    photo_schema = PhotoSchema()
    errors = photo_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    photo.title = data['title']
    photo.description = data['description']
    photo.image_url = data['image_url']
    db.session.commit()
    return jsonify(photo_schema.dump(photo))

# Delete a photo
@main.route('/photos/<int:photo_id>', methods=['DELETE'])
def delete_photo(photo_id):
    photo = Photo.query.get(photo_id)
    if photo is None:
        return jsonify({'message': 'Photo not found'}), 404
    db.session.delete(photo)
    db.session.commit()
    return jsonify({'message': 'Photo deleted'})

# Get all photographers
@main.route('/photographers', methods=['GET'])
def get_photographers():
    photographers = Photographer.query.all()
    photographer_schema = PhotographerSchema(many=True)
    return jsonify(photographer_schema.dump(photographers))

# Get a photographer by id
@main.route('/photographers/<int:photographer_id>', methods=['GET'])
def get_photographer(photographer_id):
    photographer = Photographer.query.get(photographer_id)
    if photographer is None:
        return jsonify({'message': 'Photographer not found'}), 404
    photographer_schema = PhotographerSchema()
    return jsonify(photographer_schema.dump(photographer))

# Create a new photographer
@main.route('/photographers', methods=['POST'])
def create_photographer():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    photographer_schema = PhotographerSchema()
    errors = photographer_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    photographer = Photographer(name=data['name'], bio=data['bio'], profile_picture_url=data['profile_picture_url'])
    db.session.add(photographer)
    db.session.commit()
    return jsonify(photographer_schema.dump(photographer)), 201

# Update a photographer
@main.route('/photographers/<int:photographer_id>', methods=['PUT'])
def update_photographer(photographer_id):
    photographer = Photographer.query.get(photographer_id)
    if photographer is None:
        return jsonify({'message': 'Photographer not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    photographer_schema = PhotographerSchema()
    errors = photographer_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    photographer.name = data['name']
    photographer.bio = data['bio']
    photographer.profile_picture_url = data['profile_picture_url']
    db.session.commit()
    return jsonify(photographer_schema.dump(photographer))

# Delete a photographer
@main.route('/photographers/<int:photographer_id>', methods=['DELETE'])
def delete_photographer(photographer_id):
    photographer = Photographer.query.get(photographer_id)
    if photographer is None:
        return jsonify({'message': 'Photographer not found'}), 404
    db.session.delete(photographer)
    db.session.commit()
    return jsonify({'message': 'Photographer deleted'})
```

###