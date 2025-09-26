try:
    import sqlite3 as sql
    from core import config 
except ImportError as e:
    print("error al importar el modulo  ",e)
# establecer la conexion a la base de datos y su creacion
conn= sql.connect(config.full_path_file_db)
# ejecutar comandos sql en la base datos
print(conn) 
cr= conn.cursor()
# crear la tabla students si no existe
cr.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL 
    )
''') 
# INGRESA VARIOS ESYUDIANTES  
# CONSULTA PARA INGRESAR 
name = "jhon"
insert_query = "INSERT INTO students (name) VALUES ( ? )",name
# DATOS A INSERTAR
val=[
    'jhon dean',
    'jane smiht',
    'Alice jhonson',
    'bob brown'
]
# insertar daros en la tabla students
# cr.executemany(insert_query,val)
cr.execute("INSERT INTO students(name) VALUES ('jhon')")

#mostrar los datos que se encuentran en la base de datos
rows = cr.execute("SELECT  id, name FROM students").fetchall()
print (rows)  

#guardar los cambioos en la base de datos 
conn.commit()
#mostrar el numero de registros insertados
print (f"{cr.rowcount}registros insertados.")
#cerrar la conexion a la base de datos 
conn. close()