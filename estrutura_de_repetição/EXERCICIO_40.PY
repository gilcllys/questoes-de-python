#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
#----------------------------------------------------------

codigo_cidade = []
numero_veiculos = []
numero_acidentes = []
cidade = 1
#laço para organizar os dados dentras das listas
for i in range(5):
    print(f"cidade número {cidade}")
    codigo = int(input('Digite o cógido da cidade: '))
    if codigo == 0:
        break
    else:
        veiculos = int(input('Informe a quantidade de veículos de passeio em 1999: '))
        acidentes = int(input('Informe o número de acidentes de trânsito com vitímas :'))
        print(12*"-")
        numero_veiculos.append(veiculos)
        numero_acidentes.append(acidentes)
        codigo_cidade.append(codigo)
        cidade = cidade + 1
##Qual o maior e menor índice de acidentes de transito e a que cidade pertence
cidade_altos_acidentes = numero_acidentes.index(max(numero_acidentes))
cidade_baixos_acidentes = numero_acidentes.index(min(numero_acidentes))
print(70*"-")

print(f"Cidade {codigo_cidade[cidade_altos_acidentes]} possui o maior índice de acidentes: {max(numero_acidentes)} acidentes")
print(f"Cidade {codigo_cidade[cidade_baixos_acidentes]} possui o maior índice de acidentes: {min(numero_acidentes)} acidentes")

#Qual a média de veículos nas cinco cidades juntas;

media_veiculos = sum(numero_veiculos)/len(numero_veiculos)
print(f"Média de veículos nas 5 cidades: {media_veiculos}")

#Qual a média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio.
acidentes_selecionados = []
for i in range(len(numero_veiculos)):
    if numero_veiculos[i] < 2000:
        codigo_acidente = numero_acidentes.index(numero_veiculos[i])
        acidentes_selecionados.append(numero_acidentes[codigo_acidente])
    else:
        continue
media_acidentes = sum(acidentes_selecionados)/len(acidentes_selecionados)

print(f"A média de acidentes nas cidades com menos de 2000 veículos de passeio é {media_acidentes}")