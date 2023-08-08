'''5) Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.'''

a = int(input("digite um numero"))
b = int(input("digite outro numero"))

soma = a + b
sub = a - b
sub2 = b - a
mult = a * b
div = a / b
res = a % b

print(f"Soma: { soma }")
print(f"Subtração: { sub }")
print(f"Subtração: { sub2 }")
print(f"Multiplicação: { mult }")
print(f"resta da divisao {res}")

