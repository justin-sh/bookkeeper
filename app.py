from flask import Flask, jsonify, request
from flask_cors import CORS

import os

from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    app.secret_key = os.getenv('SECRET_KEY')

    from auth import bp as auth_bp
    from accounts import bp as acc_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(acc_bp)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*','allow_headers':'*',"expose_headers": "*","supports_credentials":True}})
    return app

app = create_app()


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()
