#Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:

# a-O total de votos computados;
# b-Os númeos e respectivos votos de todos os jogadores que receberam votos;
# c-O percentual de votos de cada um destes jogadores;
# d-O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
        #Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.

#Enquete: Quem foi o melhor jogador?

#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 11
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 50
#Informe um valor entre 1 e 23 ou 0 para sair!
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 0

#Resultado da votação:

#Foram computados 8 votos.

#Jogador        Votos              %
#9               4               50,0%
#10              3               37,5%
#11              1               12,5%
#O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

jogadores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
votos = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

print("Enquete: Quem foi o melhor jogador?")
while True:
        num_player = int(input("Número do jogador (0=fim): "))
        if num_player in jogadores:
                position = num_player - 1
                votos[position].append(num_player)
        else:
                if num_player == 0:
                        break
                else:
                    print("Informe um valor entre 1 e 23 ou 0 para sair!")

#Somando todos os votos contabilizados
contador = 0
for votos_dos_jogadores in range(len(votos)):
        contador = contador + len(votos[votos_dos_jogadores])

print(f"""
Resultado da votação:
Foram computados {contador} votos.\n""")

# Porcentagem do somatório de cada voto para cada jogador
lista_de_porcentagens = []
# Somatória de votos para cada jogador
quantidade_de_votos = []
for local, votes in enumerate(votos, start=1):
        # Porcentagem de votos
        porcentagem = (len(votes)/contador) * 100
        # Quantidade de cadas votos 
        quantidade_de_votos.append(len(votes))
        if porcentagem > 0:
                lista_de_porcentagens.append(porcentagem)
                print(f"""  Jogador         votos         %   
        {local}         {len(votes)}         {round(porcentagem,2)}""")
        else:
                lista_de_porcentagens.append(porcentagem)
                continue
maior_qtd_de_votos = max(quantidade_de_votos)
maior_pocentagem = round(max(lista_de_porcentagens),2)
cod_index = lista_de_porcentagens.index(maior_pocentagem)
cod_maior_porcentagem = cod_index + 1

print(f"\nO melhor jogador foi o número {cod_maior_porcentagem}, com {maior_qtd_de_votos} votos, correspondendo a {maior_pocentagem}% do total de votos.\n")





