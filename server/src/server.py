from flask import Flask
from flask_cors import CORS
import os

from api import routes
from rate_limit import limiter

app = Flask(__name__)
app.register_blueprint(routes.api, url_prefix='/api')
app.config.update(
    SECRET_KEY = 'devkey'
)

limiter.init_app(app)
CORS(app)

# @app.route("/")
# def client():
#   return "This route will be used to serve the client"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)