import sqlite3

con = sqlite3.connect("bp.db", check_same_thread=False)
con.row_factory = sqlite3.Row

db = con.cursor()
