import os
from datetime import timedelta

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

load_dotenv()


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(__name__)

    _app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    _app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=float(os.getenv('REMEMBER_COOKIE_DURATION_DAYS')))
    _app.config['REMEMBER_COOKIE_REFRESH_EACH_REQUEST'] = True

    from auth import bp as auth_bp, login_manager
    from accounts import bp as acc_bp
    from item_options import bp as ip_bp
    _app.register_blueprint(auth_bp)
    _app.register_blueprint(acc_bp)
    _app.register_blueprint(ip_bp)

    login_manager.init_app(_app)

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
