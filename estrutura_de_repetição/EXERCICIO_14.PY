#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares
print('Digite 10 números inteiros')
pares = []
impares = []
for i in range(1,11):
    numero = int(input(f'valor {i}: ')) 
    if numero % 2 == 0 :
        pares.append(numero)
    else:
        impares.append(numero)

print(f"""
- Quantidade de valores pares: {len(pares)}
    -> valores pares: {pares} 
- Quantidade de valores impares: {len(impares)}
    -> valores impares: {impares}
""")

   