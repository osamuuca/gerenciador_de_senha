import sqlite3

Senha_Login = 'Wfcs86638699'
senha = input('Insira sua senha de Login: ')
if senha != Senha_Login:
    print('Senha invalida')
    exit()

conn = sqlite3.connect('senhas.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
service TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL
);
''')

def menu():
    print('_¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨_')
    print('_* i : inserir nova senha ~~~~*_')
    print('_* l : listar serviços salvss *_')
    print('_* r : mostrar suassenhas ~~~~*_')
    print('_* s : sair ~~~~~~~~~~~~~~~~~~*_')
    print('________________________________')

def get_password(service):
    cursor.execute(f'''
    SELECT username, password FROM users
    WHERE service = '{service}'
    ''')
    if cursor.rowcount ==0:
        print('Serviço não cadastrado, use a opçãp i para verificar os serviços')
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
    INSERT INTO users (service, username, password)
    VALUES ('{service}','{username}','{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute(f'''
    SELECT services FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input('O que deseja fazer? ')
    if op not in ['i','r','l','s']:
        print('Serviço invalido tente novamente')
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Qual o nome do serviço?')
        username = input('Qual o nome do usuario?')
        password = input('Qual a senha?')
        insert_password(service, username, password)
    if op == 'l':
        show_services()

    if op == 'r':
        service = input('Qual o serviço que voce deseja inserir?')
        get_password(service)
conn.close()
