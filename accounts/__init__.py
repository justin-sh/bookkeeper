from flask import Blueprint, request, jsonify, session

from db import db

bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.route('/')
def list_accounts():
    res = db.execute("SELECT name FROM accounts where user_id=?", (session['user_id'],))
    return jsonify({'ok': True, 'data': [{'name': u['name']} for u in res.fetchmany(size=100)]})


@bp.route('/add', methods=['POST'])
def add_account():
    data = request.get_json()
    #     app.logger.info(data)
    data['currency'] = data['currency'] or 'USD'
    data['balance'] = data['balance'] or 0  # cent
    sql_insert = 'insert into accounts(user_id,currency,name,note,balance) values(?,?,?,?,?)'
    params = (session['user_id'], data['currency'], data['name'], data['note'], data['balance'])
    db.execute(sql_insert, params)
    db.connection.commit()
    return jsonify({'ok': True, 'data': db.lastrowid})
