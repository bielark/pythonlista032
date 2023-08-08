''' Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.'''

no =  input("insira o nome")
sa = float(input("diga seu salario"))
ve = float(input("diga quanta vendas"))

co = 0.15

total = sa +(ve * co )

print(f"entao senho(a) {no} vocé vai ganha no total desse mes e {total}")


