#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. 
contador1 = 0
contador2 = 0
contador3 = 0

loop = True

while loop:
    votos = int(input("""
Urna eletrônica:
     - Digite o número do seu candidato
     (1) candidato 1 
     (2) candidato 2
     (3) candidato 3
     
     (0) encerrar votação total
     voto: """))

    if votos == 1:
        contador1 = contador1 + 1
    elif votos == 2:
        contador2 = contador2 + 1
    elif votos == 3:
        contador3 = contador3 + 1 
    elif votos == 0:
        loop = False

print(f"""
--------------------------------------------------------
             RESULTADO DA VOTAÇÃO
--------------------------------------------------------
CANDIDATO 1 : {contador1} VOTOS
CANDIDATO 2 : {contador2} VOTOS
CANDIDATO 3 : {contador3} VOTOS  """)



