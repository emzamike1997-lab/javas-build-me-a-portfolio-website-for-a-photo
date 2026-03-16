```python
from marshmallow import Schema, fields

class PhotoSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    image_url = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)

class PhotographerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    bio = fields.Str(required=True)
    profile_picture_url = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
```

###