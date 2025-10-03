try: 
    import os
    from core import config 
    from pathlib import Path
    import pandas as pd 
except IndexError as e:
    print('error al importar la libreria ', e)

def create_excel(data,columns ):
    if not os.path.exists(config.directory_folder_excel):
        os.makedirs(config.directory_folder_excel)

    excel_file = pd.DataFrame(data,columns=columns)

    excel_file.to_excel(config.paht_file_excel, engine= 'openpyxl')
