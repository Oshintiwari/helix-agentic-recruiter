from flask import Flask
from flask_cors import CORS

from routes.chat_routes import chat_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(chat_bp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
