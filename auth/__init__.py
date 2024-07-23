from http import HTTPStatus

from flask import Blueprint, request, jsonify, current_app as app, session, abort
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user


from db import db
from .user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    user_row = db.execute('SELECT * FROM users where id=?', (int(user_id),)).fetchone()
    if user_row:
        return User(user_row)

    return None


@login_manager.unauthorized_handler
def unauthorized():
    abort(HTTPStatus.UNAUTHORIZED)


@bp.route('/login', methods=['POST'])
def login():
    bcrypt = Bcrypt(app)
    data = request.get_json()
    #     app.logger.info(data)
    #     app.logger.info(data['username'])
    #     app.logger.info('passwd=' + data['passwd'])
    #     app.logger.info(bcrypt.generate_password_hash(data['passwd']).decode('utf-8'))
    r = db.execute("SELECT * FROM users where name=?", (data['name'],)).fetchone()
    # app.logger.info(user)
    if r is None or not bcrypt.check_password_hash(r['passwd'], data['passwd']):
        return jsonify({'ok': True, 'errorMsg': "login failed!"})

    session.clear()

    u = User(r['id'], r['name'], r['passwd'], r['sec_tip'], r['sec_ans'])
    login_user(u, remember=True)

    # session['user_id'] = r['id']
    return jsonify({'ok': True, 'data': {'name': r['name']}})


@bp.route('/logout')
def logout():
    logout_user()
    return jsonify({'ok': True})


@bp.route('/register', methods=['POST'])
def register():
    bcrypt = Bcrypt(app)
    data = request.get_json()
    hashed_pwd = bcrypt.generate_password_hash(data['passwd']).decode('utf-8')
    #     app.logger.info(data)
    sql_insert = 'insert into users(name,passwd,sec_tip,sec_ans) values(?,?,?,?)'
    db.execute(sql_insert, (data['name'], hashed_pwd, data['sec_tip'], data['sec_ans']))
    db.connection.commit()

    # session.clear()
    # session['user_id'] = db.lastrowid
    #     app.logger.info(db.lastrowid)
    # return jsonify({'ok':True, 'data': {'name':data['name']}})
    return jsonify({'ok': True})

# @bp.route('/')
# def users():
#     res = db.execute("SELECT * FROM users")
# #     app.logger.info(res.fetchmany())
#     return jsonify([ { 'name': u['name'] } for u in res.fetchmany(size=100) ])
