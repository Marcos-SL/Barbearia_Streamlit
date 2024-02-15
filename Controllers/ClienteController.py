import services.database as db;

def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO Cliente (cliNome, cliIdade, cliProfissao, cliSenha) 
    VALUES (?,?,?,?)""",
    cliente.nome, cliente.idade, cliente.profissao, cliente.senha).rowcount
    db.cnxn.commit()
