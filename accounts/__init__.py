from flask import Blueprint, request, jsonify, session

from flask_login import current_user

from db import db

bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.route('/')
def list_accounts():
    res = db.execute("SELECT id,name FROM accounts where user_id=?", (current_user.id,))
    return jsonify([{'name': u['name'], 'id': u['id']} for u in res.fetchmany(size=100)])


@bp.route('/add', methods=['POST'])
def add_account(data):
    data = data if data is not None else request.get_json()
    #     app.logger.info(data)
    data['currency'] = data['currency'] or 'USD'
    data['balance'] = data['balance'] or 0  # cent
    sql_insert = 'insert into accounts(user_id,currency,name,note,balance) values(?,?,?,?,?)'
    params = (current_user.id, data['currency'], data['name'], data['note'], data['balance'])
    db.execute(sql_insert, params)
    db.connection.commit()
    return jsonify({'id': db.lastrowid})
