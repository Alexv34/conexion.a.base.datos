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


# crear sentencia sql
    sql='INSERT INTO datos (nombre,descripcion,fecha) VALUES(%s,%s,%s)'

# solicitud de datos al usuario
    nombre=input('ingrese el nombre: ')
    descripcion=input('ingrese el apellido: ')
    fecha=input('ingrese la edad: ')

# recoleccion de datos
    datos=(nombre,descripcion,fecha)

# hacer uso del metodo execute
    cursor.execute(sql,datos)

# guardar registro
    connection.commit()

# registro insertados
    registros=cursor.rowcount

# mostrar mensaje
    print(f'registro insertado: {registros}')

    row=cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)