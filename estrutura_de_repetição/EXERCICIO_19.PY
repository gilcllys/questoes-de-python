#Altere o programa anterior (EXERCICIO_18.PY) para que ele aceite apenas números entre 0 e 1000. 
print('Digite os valores e para terminar o programa digite -1')
lista = []
while True:
    valores = float(input('Digite os valores ou "-1" para sair : '))
    if valores > 0:
        if   0 <= valores <= 1000:
            lista.append(valores)
        else:
            print('valor incorreto')
    elif valores == -1  :
        break
    
print(f"""
Soma: {sum(lista)}
Maior valor : {max(lista)}
Menor valor : {min(lista)}""")
