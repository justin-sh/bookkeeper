from flask import Flask, jsonify, request
from flask_cors import CORS

import sqlite3

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

con = sqlite3.connect("bp.db", check_same_thread=False)
db = con.cursor()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
#     res = db.execute("SELECT name FROM sqlite_master")
#     app.logger.info(res.fetchone())
    return jsonify('pong!')


@app.route('/users')
def users():
    res = db.execute("SELECT name FROM users")
#     app.logger.info(res.fetchmany())
    return jsonify(res.fetchmany(size=100))

@app.route('/users/add', methods=['POST'])
def userAdd():
    data =  request.get_json()
#     app.logger.info(data)
    sqlInsert = 'insert into users(name,passwd,sec_tip,sec_ans) values(?,?,?,?)'
    db.execute(sqlInsert,(data['name'],data['passwd'],data['sec_tip'],data['sec_ans']))
    con.commit()
#     app.logger.info(db.lastrowid)
    return jsonify(db.lastrowid)

if __name__ == '__main__':
    app.run()
