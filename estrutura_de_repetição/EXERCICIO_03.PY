#Faça um programa que leia e valide as seguintes informações:

#    Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#    Salário: maior que zero;
#    Sexo: 'f' ou 'm';
#    Estado Civil: 's', 'c', 'v', 'd'; 

print('Sistema de cadastro do usuário')
print()
nome = input('Digite o nome do usuário: ')
idade = int(input("Digite sua idade: "))
salario = float(input('Digite seu salário: '))
sexo = input('Digite o sexo ([f] feminino ou [m] masculino):')
print()

while len(nome) < 3:
    print('nome do usuário deve ser maior que 3 caracteres')
    nome = input('Digite o nome do usuário: ')
while not   0 < idade < 150:
    print('Idade incorreta')
    idade = int(input("Digite sua idade: "))
while  salario < 0:
    print('salário incorreto, não aceitamos valores negativos')
    salario = float(input('Digite seu salário: '))
while sexo != 'f' and sexo != 'm':
    print('sexo incorreto')
    sexo = input('Digite o sexo ([f] feminino ou [m] masculino):')

print(f"""
---------------------------------
Cadastro finalizado com sucesso !
---------------------------------
Nome: {nome}
Idade: {idade} anos 
Salário : R$ {salario}
Sexo : {sexo}""")

