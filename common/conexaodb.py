from sqlite3 import connect

conexao = connect('/home/fefeto/git/Banco/base-dados')
conexao_curs = conexao.cursor()

def executar(comando):
    conexao_curs.execute(comando)
    conexao.commit()

    rows = conexao_curs.fetchall()

    return 
