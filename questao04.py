''' Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros.'''


peso = float(input("digite seu peso em quilo"))
altura = float(input("digite sua altura"))
IMC = peso / altura

print(f"sua massa corporal e {IMC}")


