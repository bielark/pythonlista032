'''3) Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros'''

a = float(input("digite seu peso em quilo:"))
b = float(input("digite sua altura"))

c = a * 1000
d = b * 100

print(f"vocé tem {c}em grama {b} em centimetros")


