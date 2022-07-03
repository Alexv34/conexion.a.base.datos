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


# sentencia sql
    sql='DELETE FROM personas WHERE iddato=%s'

# solicitar dato al usuraio
    iddato=input('ingrese el id del registro a eliminar: ')

# metodo execute
    cursor.execute(sql,iddato)

# guardar cambios
    connection.commit()

# conteo de registro eliminado
    registro_eliminado=cursor.rowcount

# mensaje al usuario
    print(f'registros eliminados: {registro_eliminado}')


    row=cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)