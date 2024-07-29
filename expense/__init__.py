from flask import Blueprint, request, jsonify
from flask_login import current_user

import account
from db import db

bp = Blueprint('expenses', __name__, url_prefix='/expenses')


@bp.route('/')
def list_expenses():
    # t = request.args.get('type', '', type=str)

    # if 'account' == t:
    #     return account.list_accounts()

    sql = """SELECT exp.id,exp.user_id,exp.evt_date,exp.account_id,a.name as acc_name,
            exp.cat_id,op.name as cat_name,exp.subcat_id,op2.name as subcat_name,exp.amount,exp.currency_id,exp.note
             from expenses exp, accounts a, options op, options op2
            where exp.account_id = a.id
            and exp.cat_id = op.id
            and exp.subcat_id = op2.id
            and exp.user_id = ?
            order by evt_date desc"""
    sql_params = [current_user.id]
    # if 'subcategory' == t:
    #     sql += " and parent_id = ?"
    #     sql_params.append(request.args.get('parent', '', type=str))
    # sql += " order by evt_date desc"
    res = db.execute(sql, tuple(sql_params))
    return jsonify([{'id': u['id'], 'user_id': u['user_id'], 'date': u['evt_date'], 'account_id': u['account_id']} for u in res.fetchmany(size=100)])


# todo not complete
@bp.route('/create', methods=['POST'])
def create_expense():
    data = request.get_json()

    sql = 'insert into expenses(user_id,evt_date,account_id,cat_id,subcat_id,amount,currency_id,note)'
    sql += ' values(?,?,?,?,?,?,?,?)'
    sql_params = (current_user.id, data['date'], data['account']['id'],
                  data['category']['id'], data['subcategory']['id'],
                  data['amount'], data['currency']['id'], data['note'],)
    db.execute(sql, sql_params)
    db.connection.commit()
    return jsonify({'id': db.lastrowid})
