#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

from random import*

valores_altura = []
valores_idade = []

#loop para gerar as 30 alturas e idades
for dados in range(30):
    #gerador de alturas aleatórias (flutuante) 
    alturas = round(uniform(1,2),2)
    #gerador de idades aleatórias (inteiro)
    idades = randint(10,70)
    #adicionado o valor da variável "alturas" na lista valores_alturas
    valores_altura.append(alturas)
    #adicionado o valor da variável "idades" na lista valores_idade
    valores_idade.append(idades)

# MEDIA DAS ALTURAS
media_alturas = sum(valores_altura) / len(valores_altura)
print(f"\nMédia das alturas: {round(media_alturas,2)} \n")
cont = 0
for position in range(len(valores_altura)):
    if valores_altura[position] < media_alturas:
        cod_rastreamento =  valores_altura.index(valores_altura[position])
        if valores_idade[cod_rastreamento] > 13:
            print(f"Idade {valores_idade[cod_rastreamento]} , altura {valores_altura[position]}")
            cont = cont + 1
        else:
            continue
    else:
        continue

print(f"\nTotal de alunos abaixo da média: {cont}")


