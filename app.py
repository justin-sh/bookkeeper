from flask import Flask, jsonify, request
from flask_cors import CORS

import os

from dotenv import load_dotenv

load_dotenv()


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(__name__)

    _app.secret_key = os.getenv('SECRET_KEY')

    from auth import bp as auth_bp
    from accounts import bp as acc_bp
    _app.register_blueprint(auth_bp)
    _app.register_blueprint(acc_bp)

    # enable CORS
    CORS(_app,
         resources={r'/*': {'origins': '*', 'allow_headers': '*', "expose_headers": "*", "supports_credentials": True}})
    return _app


app = create_app()


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
