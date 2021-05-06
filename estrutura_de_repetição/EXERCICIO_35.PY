#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário. 
final_intervalo = int(input('valor primos existentes entre 1 à:'))
primos = []
contador = 0
for i in range(2,final_intervalo+1):
    contador = 0
    for m in range(2,i):
        divisao =  i % m 
        if divisao == 0:
            contador = contador + 1
        else: 
            pass 
    if contador > 0:
        pass
    else:
        primos.append(i)      
print(primos)
print(len(primos))
