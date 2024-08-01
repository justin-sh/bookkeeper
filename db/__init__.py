import sqlite3
from os.path import join
from os import getenv
from pathlib import Path

from sqlmodel import Field, Session, SQLModel, create_engine

from .models import *


basedir = Path(__file__).parent.parent.absolute()

con = sqlite3.connect(join(basedir, "bp.db"), check_same_thread=False)
con.row_factory = sqlite3.Row

db = con.cursor()


engine = create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db_name}".format(user=getenv('DB_USER'),passwd=getenv('DB_PASSWD'),host=getenv('DB_URL'),port=getenv('DB_PORT'),db_name=getenv('DB_NAME')))

# print(engine)