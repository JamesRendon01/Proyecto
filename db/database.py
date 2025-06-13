from sqlalchemy import create_engine

MARIADB_URL = 'mysql+pymysql://root:admin@localhost:3315/escapade-parfaite'

#crear el objeto de la conexion
engine = create_engine(MARIADB_URL)