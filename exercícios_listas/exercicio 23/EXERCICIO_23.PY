#A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
#alexandre       456123789
#anderson        1245698456
#antonio         123456456
#carlos          91257581
#cesar           987458
#rosemary        789456125
#Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
#ACME Inc.               Uso do espaço em disco pelos usuários
#------------------------------------------------------------------------
#Nr.  Usuário        Espaço utilizado     % do uso

#1    alexandre       434,99 MB             16,85%
#2    anderson       1187,99 MB             46,02%
#3    antonio         117,73 MB              4,56%
#4    carlos           87,03 MB              3,37%
#5    cesar             0,94 MB              0,04%
#6    rosemary        752,88 MB             29,16%

#Espaço total ocupado: 2581,57 MB
#Espaço médio ocupado: 430,26 MB
#O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

from conversor_bytes import conversor

usuarios = open('usuarios.txt') #abrindo o arquivo
users = usuarios.readlines() #convertendo cada linha em uma string e armazenando todas ela e uma lista

dados = [] # lista com dados brutos
pessoas = [] # somente os nomes dos usuários 
espaco_utilizado = [] # somentes o espaço utilizado de cada um

#loop para retirar o quebra linha e traformar os dados em um matriz
for linhas in users:
    linhas = linhas.rstrip("\n")
    dados.append(linhas.split())

# separando  os dados para as lista pessoas[] e espaco_utilizado[]
for linha in range(len(dados)):
    for coluna in range(len(dados[linha])):
        if coluna == 0:
            pessoas.append(dados[linha][coluna])
        else:
            espaco_utilizado.append(dados[linha][coluna])

#convertendo de bytes para Megabytes
espaco_convertido = conversor(espaco_utilizado)

# porcentagens
pctg = []
for valores in espaco_convertido:
    valores = (valores / sum(espaco_convertido))*100
    pctg.append(round(valores,2))

# espaço médio
espaco_medio = sum(espaco_convertido)/len(espaco_convertido)

# criando relatório

relatorio = open("relatório.txt","w")
conteudo = []

conteudo.append("""
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário            Espaço utilizado     % do uso
\n""")
count = 1
for index,valor in enumerate(espaco_convertido):
    conteudo.append(f"{count}     {pessoas[index]}  ")
    conteudo.append(f"        {valor} MB              {pctg[index]}\n")
    count += 1

conteudo.append(f"""
Espaço total ocupado: {round(sum(espaco_convertido),2)} MB
Espaço médio ocupado: {espaco_medio} MB""")


#escrevendo cada elemento da lista conteúdo linha por linha do arquivo txt.
relatorio.writelines(conteudo)

#fechando arquivos após o uso
usuarios.close()
relatorio.close()