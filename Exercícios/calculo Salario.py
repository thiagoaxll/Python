"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Calculo salario                  |
|   Data : 06/04/2018                            |
|________________________________________________|
"""

horasTrabalhadas = float(input('Quantas horas você trabalhou esse mês: '))
valorHora = float(input('Qual o valor da sua hora trabalhada: '))
desconto = float(input('Qual o percentual de desconto: '))

salariobruto = horasTrabalhadas * valorHora

print('Salário bruto: {:.2f}\nTotal descontado: {:.2f}\nSalário liquido: {:.2f}'.format(salariobruto, (desconto * salariobruto)/100,salariobruto - (desconto * salariobruto)/100))


