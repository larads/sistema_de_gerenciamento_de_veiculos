import pymysql.cursors
from contextlib import contextmanager
from pymysql import Error

@contextmanager
def database_connection():
    connection = None

    try:
        connection = pymysql.connect(
            host='127.0.0.1',  
            port=3306,         
            user='root',     
            password='root',  
            db='locar',       
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Conexão com o banco de dados estabelecida.")
    except Error as ex:
        print("Erro ao conectar ao banco de dados:", ex)
    yield connection
    if connection:
        connection.close()
        print("Conexão com o banco de dados encerrada.")

def dql(query):
    with database_connection() as conect:
        try:
            c = conect.cursor()
            c.execute(query)
            resultado = c.fetchall()
            return resultado
        except Error as ex:
            print("Erro ao executar consulta SELECT:", ex)

def dml(query):
    with database_connection() as conect:
        try:
            c = conect.cursor()
            c.execute(query)
            conect.commit()
            print("Consulta DML executada com sucesso.")
        except Error as ex:
            print("Erro ao executar consulta DML:", ex)
