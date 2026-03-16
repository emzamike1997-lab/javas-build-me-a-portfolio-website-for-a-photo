```python
import os
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logging.info('Logging setup')

def create_database():
    from app import db
    db.create_all()
    logging.info('Database created')
```

###