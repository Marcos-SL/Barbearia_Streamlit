import pyodbc

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=exemplo;DATABASE=exemplo;UID=UserExemplo;PWD=SenhaExemplo')
cursor = cnxn.cursor()
