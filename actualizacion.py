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
# crear sentencia sql
    sql='UPDATE datos SET nombre=%s,descripcion=%s WHERE iddato=%s'

# consulta de datos a usuario
    iddato=input('ingrese id de la iddato a editar: ')
    nombre=input('ingrese nombre: ')
    descripcion=input('ingrese descripcion: ')

#recoleccion de datos
    datos=(nombre,descripcion,iddato)

# utilizar el metodo execute
    cursor.execute(sql,datos)

# guardar modificacion
    connection.commit()

#contar el numero de cambios
    actualizacion=cursor.rowcount

# mostrar mensaje al usuraio
    print(f'registro actualizado: {actualizacion}')
    row=cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)