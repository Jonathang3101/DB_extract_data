import pymysql
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from datetime import datetime

db_config = {
    'host': 'localhost',
    'user': 'usuario',
    'password': 'password',
    'database': 'basedatos',
    'port': 3306,
    'charset': 'utf8mb4'
}


def conectar_db():
    """ conexión con MariaDB"""
    try:
        conn = pymysql.connect(**db_config)
        print(" Conexión exitosa a la base de datos")
        return conn
    except pymysql.Error as e:
        print(f" Error al conectar: {e}")
        return None
    
