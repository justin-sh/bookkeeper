from flask import Flask, jsonify, request
from flask_cors import CORS

import os

from dotenv import load_dotenv
load_dotenv()

# @app.route('/users')
# def users():
#     res = db.execute("SELECT name FROM users")
# #     app.logger.info(res.fetchmany())
#     return jsonify(res.fetchmany(size=100))
#
# @app.route('/users/add', methods=['POST'])
# def userAdd():
#     data =  request.get_json()
# #     app.logger.info(data)
#     sqlInsert = 'insert into users(name,passwd,sec_tip,sec_ans) values(?,?,?,?)'
#     db.execute(sqlInsert,(data['name'],data['passwd'],data['sec_tip'],data['sec_ans']))
#     con.commit()
# #     app.logger.info(db.lastrowid)
#     return jsonify(db.lastrowid)

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    app.secret_key = os.getenv('SECRET_KEY')

    from auth import bp as auth_bp
    from users import bp as user_bp
    from accounts import bp as acc_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(acc_bp)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    return app

app = create_app()


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
#     res = db.execute("SELECT name FROM sqlite_master")
#     app.logger.info(res.fetchone())
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()
