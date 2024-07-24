import sqlite3
from os.path import join
from pathlib import Path

basedir = Path(__file__).parent.parent.absolute()

con = sqlite3.connect(join(basedir, "bp.db"), check_same_thread=False)
con.row_factory = sqlite3.Row

db = con.cursor()
