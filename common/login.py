from common.conexaodb import executar

def cadastro():
    nome_completo = str(input("Digite seu nome completo:"))
    telefone = int(input("Digite seu número de telefone:"))
    endereco = str(input("Digite seu endereço:"))
    email = str(input("Digite seu e-mail:")) 
    senha = int(input("Crie uma senha:"))
    
    informacoes = "INSERT INTO USUARIO (NOME, TELEFONE, EMAIL, ENDERECO) VALUES ('" + nome_completo + "'," + str(telefone) + ",'" + email + "','" + endereco +"')"
    executar(informacoes)

    informacoes = "SELECT ID FROM USUARIO WHERE NOME = '" + nome_completo + "'"
    identificacao = executar(informacoes)
    
    informacoes = "INSERT INTO LOGIN (ID,SENHA) VALUES ("+ str(identificacao) + "," + str(senha) + ")"
    

def login():
    
    senha = int(input("Digite sua senha:"))
    verificacao = "SELECT U.NOME FROM LOGIN L INNER JOIN USUARIO U ON U.ID = L.ID WHERE L.SENHA = " + str(senha)
    executar(verificacao)
    
if(__name__ == "__main__"):  
    cadastro()   
    login()