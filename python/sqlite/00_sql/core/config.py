try:
    import os 
    from pathlib import Path
except ImportError as e:
    print("error al importar el modulo  ",e)
# obtener el directorio de trabajo actual 
cwd= os.getcwd()
path_current_db = cwd + "/python/sqlite/00_sql"
#nonbre de la carpeta donde almacernaremos el archivo.db o la base de datos 
directorio_carpeta_db = "db/folder_db"
#trabajando en una computadora local o en un espacio de codigop de github no hace falta agregar las siguientes variables
# con solo agregar full_path_db = os.path.join(cwd,directorio_carpeta_db)

full_path_db = os.path.join(path_current_db,directorio_carpeta_db)

if not os.path.exists(full_path_db):
    print (full_path_db) 
    os.makedirs(full_path_db)

#crear el archivo sqlite en la carpeta db /folder_db 

name_file_db = "test"
#comprobar que el archivo db cuente con el sufijo .db
name_file_db = str(Path(name_file_db).with_suffix(".db").stem + ".db")

full_path_file_db = os.path.join(full_path_db,name_file_db)