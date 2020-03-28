#--- Imports --------------------------------------------------------------------------------------------------------
import sqlite3

#--- Funções ------------------------------------------------------------------------------------------------------

def menu():
    print('\n')
    print('#'*28)
    print('#  1 : Inserir nova senha         #')
    print('#  2 : Listar servios salvos       #')
    print('#  3 : Recuperar senha            #')
    print('#  0 : Sair                                #')
    print('#'*28,'\n')

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}','{username}','{password}')
    ''')
    conn.commit()
    
def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    print('--- Serviços ----------')
    x = 0
    for service in cursor.fetchall():
        print(x,' - ',service[0])
        x += 1
        
def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
        ''')

    if cursor.rowcount == 0:
        print("Serviço não cadastrado (user '2' para verificar os serviços).")
    else:
        print('-'*50)
        for user in cursor.fetchall():
            print('Usuario: ',user[0],'Senha: ',user[1])
            print('-'*50)


        
#--- Execução -----------------------------------------------------------------------------------------------------

MASTER_PASSWORD ='1'

#--------------------------------------------------------------------------

senha =  input('Insira a sua senha master: ')
if senha != MASTER_PASSWORD:
    print('\nSenha invalida Encerrando!')
    print('\n')
    exit()
    
#--------------------------------------------------------------------------    

conn = sqlite3.connect('password.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    );
    ''')

#--- loop para o menu ------------------------------------------

while True:
    menu()
    op = input('O que deseja fazer? ')
    if op not in ['1','2','3','0']:
        print('\nOpção invalida!\n')
        continue

    if op == '0':
        print('\nBye Bye!')
        print('\n')        
        break

    if op == '1':
        print('\n')
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usuario? ')
        password = input('Qual a senha? ')
        insert_password(service, username, password)        
        
    if op == '2':
        print('\n')
        show_services()


    if op == '3':
        print('\n')
        show_services()
        print('\n')
        service = input('Qual o nome do serviço para o qual quer a senha? ')
        get_password(service)    
        
#--- Fechar a conexão --------------------------------------------    
conn.close()
