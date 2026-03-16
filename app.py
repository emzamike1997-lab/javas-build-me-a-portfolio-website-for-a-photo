```python
from flask import Flask, jsonify
from flask_cors import CORS
from routes import main_routes
from utils import configure_logger

app = Flask(__name__)
CORS(app)

# Configure logging
configure_logger(app)

# Register routes
app.register_blueprint(main_routes)

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

###