preco_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_bruto = preco_hora * horas_trabalhadas
IR = salario_bruto * (11 / 100)
INSS = salario_bruto * (8 / 100)
sindicato = salario_bruto * (5 / 100)
salario_liquido = salario_bruto - IR - INSS - sindicato
print("+ Salário Bruto : R${}.\n"
    "- IR (11%) : R${}\n"
    "- INSS (8%) : R${}\n"
    "- Sindicato (5%) : R${}\n"
    "= Salário Liquido : R${}" .format(IR,INSS,sindicato,salario_liquido))