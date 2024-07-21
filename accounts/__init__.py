from flask import Blueprint, request, jsonify, current_app as app

from db import db

bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@bp.route('/')
def users():
    res = db.execute("SELECT name FROM accounts")
#     app.logger.info(res.fetchmany())
    return jsonify(res.fetchmany(size=100))

@bp.route('/add', methods=['POST'])
def userAdd():
    data =  request.get_json()
#     app.logger.info(data)
    sqlInsert = 'insert into accounts(name,passwd,sec_tip,sec_ans) values(?,?,?,?)'
    db.execute(sqlInsert,(data['name'],data['passwd'],data['sec_tip'],data['sec_ans']))
    con.commit()
#     app.logger.info(db.lastrowid)
    return jsonify(db.lastrowid)