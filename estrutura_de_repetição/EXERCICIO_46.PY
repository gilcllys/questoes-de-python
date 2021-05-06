#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo

#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Melhor salto:  6.5 m
#Pior salto: 5.3 m
#Média dos demais saltos: 5.9 m

#Resultado final:
#Rodrigo Curvêllo: 5.9 m


ordem_saltos = ["Primeiro", "segundo", "Terceiro", "Quarto", "Quinto"]
valores_saltos = []
nome_atleta = input("Digite o nome do Atleta: ")

#loop para armazenar os saltos na lista valores_saltos
for saltos in range(len(ordem_saltos)):
    medida_salto = float(input(f"Distância do {ordem_saltos[saltos]} salto: "))
    valores_saltos.append(medida_salto)

#média do saltos
media_saltos = (sum(valores_saltos) - max(valores_saltos) - min(valores_saltos)) /3

print(f"""
Atleta: {nome_atleta}

Primeiro Salto: {valores_saltos[0]} m
Segundo Salto: {valores_saltos[1]} m
Terceiro Salto: {valores_saltos[2]} m
Quarto Salto: {valores_saltos[3]} m
Quinto Salto: {valores_saltos[4]} m

Melhor salto:  {max(valores_saltos)} m
Pior salto: {min(valores_saltos)} m

Resultado final:
{nome_atleta}: {round(media_saltos,2)} m""")


