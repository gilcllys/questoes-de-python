#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

nome_usuario = input('Digite seu usuário :')
senha = input('digite sua senha :')

while nome_usuario == senha:
    print('Não aceitamos senha igual ao usuário ')
    print()
    senha = input('Digite sua senha :')
    print()
print('! Cadastro válido !')
print(f"""
Usuário : {nome_usuario}
senha : {senha} """)