```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Photographer(db.Model):
    """Photographer model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Photographer('{self.name}', '{self.bio}')"

class Photo(db.Model):
    """Photo model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(200), nullable=False)
    photographer_id = db.Column(db.Integer, db.ForeignKey('photographer.id'), nullable=False)

    def __repr__(self):
        return f"Photo('{self.title}', '{self.description}', '{self.url}')"
```

###