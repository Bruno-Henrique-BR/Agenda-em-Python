import sqlite3
conn = sqlite3.connect('C:/Users/Robson/Desktop/Agenda.db')
cursor = conn.cursor()

def insere_codigo():
     return(input("Codigo: "))

def insere_nome():
     return(input("Nome: "))

def insere_telefone():
     return(input("Telefone: "))

def insere_email():
     return(input("E-mail: "))

def insere_dt_nascimento():
     return(input("Data de Nascimento: "))

def insere_endereco():
    return(input("Endereço: "))

def insere():
     nome = insere_nome()
     telefone = insere_telefone()
     email = insere_email()
     dt_ascimento = insere_dt_nascimento()
     endereco = insere_endereco()
     cursor.execute("INSERT INTO contatos VALUES (NULL, ?, ?, ?, ?, ?)", (nome, telefone, email, dt_ascimento, endereco))
     conn.commit()
     print("Contato inserido com sucesso!")

def consulta():
    codigo = insere_codigo()
    cursor.execute("SELECT * FROM contatos WHERE id_codigo = ?", (codigo))
    pessoa = cursor.fetchall()
    print(pessoa)

def alterar():
    codigo = insere_codigo()

    print("""
O QUE DESEJA ALTERAR?
    1 - Nome
    2 - Telefone
    3 - E-mail
    4 - Data de Nascimento
    5 - Endereço
""")
    opcao = validar_opcao("Escolha uma opção: ",1,5)

    if opcao == 1:
        alter_nome = insere_nome()
        cursor.execute("UPDATE contatos SET nome = ? where id_codigo = ?", (alter_nome, codigo))
        conn.commit()
        print("Nome alterado com sucesso!")

    elif opcao == 2:
        alter_telefone = insere_telefone()
        cursor.execute("UPDATE contatos SET telefone = ? where id_codigo = ?", (alter_telefone, codigo))
        conn.commit()
        print("Telefone alterado com sucesso!")
        
    elif opcao == 3:
        alter_email = insere_email()
        cursor.execute("UPDATE contatos SET email = ? where id_codigo = ?", (alter_email, codigo))
        conn.commit()
        print("E-mail alterado com sucesso!")
        
    elif opcao == 4:
        alter_data_nascimento = insere_dt_nascimento()
        cursor.execute("UPDATE contatos SET data_nascimento = ? where id_codigo = ?", (alter_data_nascimento, codigo))
        conn.commit()
        print("Data de Nascimento alterada com sucesso!")
        
    elif opcao == 5:
        alter_endereço = insere_endereco()
        cursor.execute("UPDATE contatos SET endereco = ? where id_codigo = ?", (alter_endereço, codigo))
        conn.commit()
        print("Endereço alterado com sucesso!")

def remove_cod():
    codigo = insere_codigo()
    try:
        cursor.execute("DELETE FROM contatos WHERE id_codigo = ?", (codigo))
        conn.commit()
        print("Contato excluído com sucesso!")
    except conn.Error as erro:
        print(erro)

def listar():
     cursor.execute("SELECT * FROM contatos")
     for contato in cursor.fetchall():
        print(contato)



def validar_opcao(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))


def menu():
     print("""
   1 - Cadastrar
   2 - Consultar
   3 - Alterar
   4 - Apagar
   5 - Listar

   0 - Sair
""")
     return validar_opcao("Escolha uma opção: ",0,5)

while True:
     opcao = menu()
     if opcao == 0:
         break
     elif opcao == 1:
         insere()
     elif opcao == 2:
        consulta()
     elif opcao == 3:
        alterar()
     elif opcao == 4:
        remove_cod()
     elif opcao == 5:
        listar()