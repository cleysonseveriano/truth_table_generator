import ttg 
variables_list = []
operacoes_list = []

print('-'*15,'CALCULADORA LÓGICA','-'*15)
print('Variáveis: [p] [q] [r]')
print('Operações: [or] [and] [=>] [=]\n')

print('ex.:')
print('Variáveis: [p,q]')
print('Operações: [p => q, p = q]\n')

variables = input('Digite as variáveis: ')
for i in variables:
    variables_list.append(i)

operacoes = input('Digite a operação: ')
operacoes_list.append(operacoes)

table = ttg.Truths(variables_list, operacoes_list, ints=False)

print('\nTABELA VERDADE')
print(table)
if table.valuation()=='Tautology':
    print('A tabela é tautológica')