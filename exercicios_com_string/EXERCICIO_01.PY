string_1 = "Brasil Hexa 2006"
string_2 = "Brasil! Hexa 2006!"

tamanho_1 = len(string_1)
tamanho_2 = len(string_2)

print(f"Tamanho da string: {string_1} ({tamanho_1} caracteres)")
print(f"Tamanho da string: {string_2} ({tamanho_2} caracteres)")

if tamanho_1 != tamanho_2:
    print("As duas strings sao de tamanhos diferentes")
else:
    print("As duas strings sao de tamanhos iguais")

if string_1 == string_2:
    print("As duas strings possuem conteúdos iguais")
else:
    print("As duas strings possuem conteúdos diferentes")