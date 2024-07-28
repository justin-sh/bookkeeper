from flask import Blueprint, request, jsonify, session, current_app as app, g
from flask_login import current_user
import accounts
from db import db

bp = Blueprint('options', __name__, url_prefix='/options')


@bp.route('/')
def list_options():
    t = request.args.get('type', '', type=str)

    if 'account' == t:
        return accounts.list_accounts()

    sql = "SELECT id,name FROM options where user_id in (0, ?) and type=?"
    sql_params = [current_user.id, t]
    if 'subcategory' == t:
        sql += " and parent_id = ?"
        sql_params.append(request.args.get('parent', '', type=str))
    sql += " order by name"
    res = db.execute(sql, tuple(sql_params))
    return jsonify([{'name': u['name'], 'id': u['id']} for u in res.fetchmany(size=100)])


@bp.route('/add')
def add_options():
    data = request.get_json()
    t = data['type']

    if 'account' == t:
        return accounts.add_account(data)

    res = db.execute("SELECT name, desc FROM options where user_id in (0, ?) and type=? order by name",
                     (current_user.id, t))
    return jsonify([{'name': u['name'], 'desc': u['desc']} for u in res.fetchmany(size=100)])
