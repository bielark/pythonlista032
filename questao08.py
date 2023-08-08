'''8) Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.'''


a = float(input("diga o valor do custo R$"))
b = float(input("diga  a taxa que ira paga "))

c = b / 100
total = a + (a * c )

print(f"valor total com as taxa{total}")

