import psycopg2
import pandas as pd

db_params = {
    'host': 'localhost',        
    'port': '5432',
    'dbname': 'prolinux',
    'user': 'usuario',          
    'password': 'contraseña'    
}
#queries to extract data 
querys = {
    'CuentasDDS': "SELECT * FROM estcta.Cuentas_dds;",
    'comision': "SELECT * FROM estcta.Comision;",
    'Clientes5k': "SELECT * FROM estcta.clientes WHERE saldo >= 5000;",
    'SaldoPromedio': """
        SELECT cliente_id, AVG(saldo) AS saldo_promedio
        FROM estcta.movimientos
        GROUP BY cliente_id;
    """
}


try:
    conn = psycopg2.connect(**db_params)
    with pd.ExcelWriter('reporte unificadoFISSA appian.xlsx', engine='openpyxl') as writer:
        for nombre_tabla, query in queries.items():
            df = pd.read_sql_query(query, conn)
            df.to_excel(writer, sheet_name=nombre_tabla, index=False)
    print("Archivo 'reporte unificadoFISSA appian.xlsx' generado exitosamente.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()