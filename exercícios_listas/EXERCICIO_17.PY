#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
 
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m
import os

ordem_saltos = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
Atleta = input("Nome do atleta: ")

def saltos (distancia):
    for i in ordem_saltos:
        distancia_marcada = float(input(f"{distancia} Salto(metros): "))
        return distancia_marcada
#lista com todos os saltos armazenados
distancia_saltos = [ saltos(i) for i in ordem_saltos]
os.system("cls")
#média dos saltos
media_dos_saltos = round((sum(distancia_saltos)/len(distancia_saltos)),2)

for i in range (len(ordem_saltos)):
    print(f"{ordem_saltos[i]} Salto: {distancia_saltos[i]} m")

print(f"""
\n\nResultado final:
Atleta: {Atleta}""")
print("Saltos:",end=" ")
for i in distancia_saltos:
    print(i,end=" - ")

print(f"\nMédia dos saltos: {media_dos_saltos} m")
