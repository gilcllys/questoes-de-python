#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
#"Qual o melhor Sistema Operacional para uso em servidores?"

#As possíveis respostas são:

#1- Windows Server
#2- Unix
#3- Linux
#4- Netware
#5- Mac OS
#6- Outro

#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

#Sistema Operacional     Votos   %
#-------------------     -----   ---
#Windows Server           1500   17%
#Unix                     3500   40%
#Linux                    3000   34%
#Netware                   500    5%
#Mac OS                    150    2%
#Outro                     150    2%
#-------------------     -----
#Total                    8800

#O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
from random import*
votos_dos_SI = [[],[],[],[],[],[]]
sistemas_operacionais = ["Windows Server","Unix","Linux","Netware","Mac OS","Outro" ]

contador_de_votos = 0
for votos in range(8800):
    voto = randint(1,6)
    if voto >=1 and voto <=6:
        contador_de_votos = contador_de_votos + 1 
        cod_voto = voto - 1
        votos_dos_SI[cod_voto].append(voto)
    else:
        continue  

def porcentagem (valor):
    p = (valor / contador_de_votos) * 100
    return round(p,2)


print(f"""
Sistema Operacional     Votos   %
-------------------     -----   ---
{sistemas_operacionais[0]}           {len(votos_dos_SI[0])}   {porcentagem(len(votos_dos_SI[0]))}
{sistemas_operacionais[1]}                     {len(votos_dos_SI[1])}   {porcentagem(len(votos_dos_SI[1]))}
{sistemas_operacionais[2]}                    {len(votos_dos_SI[2])}   {porcentagem(len(votos_dos_SI[2]))}
{sistemas_operacionais[3]}                  {len(votos_dos_SI[3])}   {porcentagem(len(votos_dos_SI[3]))}
{sistemas_operacionais[4]}                   {len(votos_dos_SI[4])}   {porcentagem(len(votos_dos_SI[4]))}
{sistemas_operacionais[5]}                    {len(votos_dos_SI[5])}   {porcentagem(len(votos_dos_SI[5]))}
#-------------------     -----
#Total                    {contador_de_votos} """)

