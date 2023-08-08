''') A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.'''

a = float(input("diga o valor do produto pra ver as parcelas"))

b = a / 10

print(f"o produto fica {a} sem juros por 10 parcelas")

c = float(input("que mudar o numeros de parcelamebto"))

d = a / c
print(f"fica {d}")