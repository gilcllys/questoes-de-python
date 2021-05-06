#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
#Quantidade de mouses: 100

#Situação                        Quantidade              Percentual
#1- necessita da esfera                  40                     40%
#2- necessita de limpeza                 30                     30%
#3- necessita troca do cabo ou conector  15                     15%
#4- quebrado ou inutilizado              15                     15%
import os
# lista das situações possiveis do mouse
esfera = []
limpeza = []
troca_cabo = []
quebrado = []
# metódo para apresentar o menu com as opções para o usuário
def menu ():
    print("""
    ********************************
    SISTEMA DE D CADASTRO DE SUCATAS
    *********************************
    Selecione o código para indicar a situação do mouse
    
    1 - Necessita de esfera
    2 - Necessita de limpeza 
    3 - Necessita troca de cabo ou conector
    4 - Quebrado ou inutilizado
    0 - Encerrar o programa
    """)
    entrada = int(input("Código: "))
    return entrada
# método para exibir um menu de encerramento 
def encerrar ():
    print(" Tem certeza que deseja encerrar o programa ?")
    print("s (encerrar o programar completamente)")
    print("n (para voltar o menu principal)\n")
    comando = input("comando (s/n)")
    comando = comando.lower()
    return comando

def incorreto():
   print("""
            *******************
            *ENTRADA INCORRETA*
            *******************
            O programa somente aceita os valores: 0,1,2,3 e 4
            
            Tente novamente 
            Por favor """)
# loop para armazenar as respostas do usuário
while True:
    resposta = menu()
    os.system("cls")
    if resposta == 1:
        esfera.append(resposta)
    elif resposta == 2:
        limpeza.append(resposta)
    elif resposta == 3:
        troca_cabo.append(resposta)
    elif resposta == 4:
        quebrado.append(resposta)
    elif resposta == 0:
        comando = encerrar()
        os.system("cls")
        if comando == "s":
            print("""
            ********************
            *Programa encerrado*
            ********************
            """)
            break
        else:
            menu()
    else:
        incorreto()

# total de mouses cadastrados
TOTAL = len(esfera) + len(limpeza) + len(troca_cabo) + len(quebrado)

# porcentagens 
pctg_eseferas = round((len(esfera)/TOTAL)*100,2)
pctg_limpeza = round((len(limpeza)/TOTAL)*100,2)
pctg_trocaCabo = round((len(troca_cabo)/TOTAL)*100,2)
pctg_quebrado = round((len(quebrado)/TOTAL)*100,2)

#Display 
print(f"""
relatório:
Quantidade de mouses: {TOTAL}

Situação                        Quantidade              Percentual
1- necessita da esfera                  {len(esfera)}                     {pctg_eseferas} %
2- necessita de limpeza                 {len(limpeza)}                     {pctg_limpeza} %
3- necessita troca do cabo ou conector  {len(troca_cabo)}                     {pctg_trocaCabo} %
4- quebrado ou inutilizado              {len(quebrado)}                     {pctg_quebrado} %
""")