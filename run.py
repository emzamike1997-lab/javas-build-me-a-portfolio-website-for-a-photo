```python
from app import create_app
from app.utils import setup_logging, create_database

app = create_app()

if __name__ == '__main__':
    setup_logging()
    create_database()
    app.run(debug=True)
```

###