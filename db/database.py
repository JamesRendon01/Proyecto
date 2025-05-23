from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:admin@localhost:3315/escapade-parfaite'

conn = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()