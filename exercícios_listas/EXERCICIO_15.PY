#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

from random import*
# função de criadora de elementos aleatória do tipo float entre 1 à 10 arrendados para 2 casas decimais
def gerador_de_valores (valor):
    return round(uniform(1,10),2)

#vetor gerador de 50 elementos em loop
vetor_de_valores = [gerador_de_valores(i) for i in range(5)]

#Mostre a quantidade de valores que foram lidos;
print (f"Quantidade de valores que foram lidos: {len(vetor_de_valores)}\n")
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print("valores na ordem em que foram informados, um ao lado do outro:")
for valores in vetor_de_valores:
    print(valores,end=" ")
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
vetor_de_valores.reverse()
print("\n\nExiba todos os valores na ordem inversa à que foram informados, um abaixo do outro")
for valores in vetor_de_valores:
    print(valores)
#Calcule e mostre a soma dos valores;
print(f"\nsoma dos valores: {round(sum(vetor_de_valores),2)}")
#Calcule e mostre a média dos valores;
media = sum(vetor_de_valores)/len(vetor_de_valores)
print(f"\nmédia dos valores: {round(media,2)}")
#Calcule e mostre a quantidade de valores acima da média calculada;
count = 0
for valores in vetor_de_valores:
    if valores > media:
        count = count + 1
    else:
        continue
print(f"\nQuantidade de valores acima da média: {count}")

#Calcule e mostre a quantidade de valores abaixo de sete;
cont = 0
for valores in vetor_de_valores:
    if valores < 7:
        cont = cont + 1
    else:
        continue
print(f"\nquantidade de valores abaixo de sete: {cont}")

print("\n\nPrograma finalizado!")
