import services.database as db;

def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO Agenda (nome, corte, telefone, horario, data) 
    VALUES (?,?,?,?,?)""",
    cliente.nome, cliente.corte, cliente.telefone, cliente.horario, cliente.data).rowcount
    db.cnxn.commit()
