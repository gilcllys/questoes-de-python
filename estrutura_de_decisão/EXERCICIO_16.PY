#calculadora do raízes de funções do segundo grau 
from math import*
import random
print(100*"-")
print(' calculadora para encontrar as raízes')
# variáveis da função 
a = random.uniform(0,10)
b = random.uniform(0,10)
c = random.uniform(0,10)
#delta da função 
delta = b**2 - (4*a*c)
#condições para encontrar as raízes 
if delta >= 0 :
    if delta == 0 :
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + delta)/(2*a)
        print('possui somente uma raíz  x1 ={}, x2 ={}'.format(x1,x2))
    elif delta >0 :
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        print('possui duas raizes distintas x1 ={} , x2 ={}'.format(x1,x2))
else :
    print("não possui raízes")
