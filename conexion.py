from sqlite3 import Row
import psycopg2
try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='ejemplo'
        )
    print("conexion exitosa")
    
    cursor=connection.cursor()
    cursor.execute("Select version()")
# crear la sentencia sql
    sql='SELECT * FROM datos'

# uso del metodo execute
    cursor.execute(sql)

# mostrar resultado
    registro=cursor.fetchall()

# mostrar en consola o el usuario
    for fila in registro:
        print(fila)
    row=cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)