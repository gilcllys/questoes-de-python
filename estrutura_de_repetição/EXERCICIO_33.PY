#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. 

loop = True
valores = []
while loop:
    temperatura = float(input('Informe as temperaturas (°C) :'))
    if temperatura != 0:
        valores.append(temperatura)
    else:
        loop = False

media = sum(valores)/len(valores)

print(f"""
Temperatura máxima : {max(valores)}
Temperatura mínima : {min(valores)}
Temperatura média : {media} """)

