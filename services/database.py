import pyodbc

server = 'servidor'
database = 'nome do database'
username = 'login'
password = 'senha'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
