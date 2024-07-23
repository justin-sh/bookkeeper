from flask import Blueprint, request, jsonify, current_app as app, session
from flask_bcrypt import Bcrypt

from db import db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['POST'])
def login():
    bcrypt = Bcrypt(app)
    data = request.get_json()
    #     app.logger.info(data)
    #     app.logger.info(data['username'])
    #     app.logger.info('passwd=' + data['passwd'])
    #     app.logger.info(bcrypt.generate_password_hash(data['passwd']).decode('utf-8'))
    user = db.execute("SELECT * FROM users where name=?", (data['name'],)).fetchone()
    app.logger.info(user)
    if user is None or not bcrypt.check_password_hash(user['passwd'], data['passwd']):
        return jsonify({'ok': True, 'errorMsg': "login failed!"})

    session.clear()
    session['user_id'] = user['id']
    return jsonify({'ok': True, 'data': {'name': user['name']}})


@bp.route('/register', methods=['POST'])
def register():
    bcrypt = Bcrypt(app)
    data = request.get_json()
    #     app.logger.info(data)
    sqlInsert = 'insert into users(name,passwd,sec_tip,sec_ans) values(?,?,?,?)'
    db.execute(sqlInsert, (
    data['name'], bcrypt.generate_password_hash(data['passwd']).decode('utf-8'), data['sec_tip'], data['sec_ans']))
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
