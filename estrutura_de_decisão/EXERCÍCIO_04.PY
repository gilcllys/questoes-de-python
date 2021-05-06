#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
while True:
    print(90*'*-')
    letra = input("Digite uma letra para verificar se é uma vogal ou consoante: ")
    vogal = 'aeiouAEIOU'
    if letra in vogal:
        print(f'{letra} é uma vogal')
    else:
        print(f'{letra} é uma consoante')
