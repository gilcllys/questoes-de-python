#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#    Dicas:
#    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#    Triângulo Equilátero: três lados iguais;
#    Triângulo Isósceles: quaisquer dois lados iguais;
#    Triângulo Escaleno: três lados diferentes; 

lado1 = float(input('lado 1 : '))
lado2 = float(input('lado 2 : '))
lado3 = float(input('lado 3 : '))
if lado1 == 0 or lado2 == 0 or lado3 == 0 :
    lados = [lado1,lado2,lado3]
    print(f'LADO NEGATIVO NÃO EXISTE -> {lados}')
elif lado1 < 0 or lado2 < 0 or lado3 < 0  :
    lados = [lado1,lado2,lado3]
    print(f'ERRO LADO NEGATIVO ->{lados}')
else:
    if lado1 == lado2 == lado3 :
        lados = [lado1,lado2,lado3]
        print(f'triângulo equilátero, lados {lados}')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
        lados = [lado1,lado2,lado3]
        print(f'triângulo isósceles, lados {lados}')
    else:
        lados = [lado1,lado2,lado3]
        print(f'triângulo escaleno, lados {lados}')
