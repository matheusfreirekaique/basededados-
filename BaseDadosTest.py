import pandas as pd

# Passo a passo de solução

# Abri os 6 arquivos de excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print(mes)
tabela_vendas_janeiro = pd.read_excel('janeiro.xlsx')


print(tabela_vendas)
# Para cada arquivo:

# Verificar se algum valor na coluna Vendas é maior que 55.000

# Se for maior do que 55.000 -> Enviar um SMS com o nome, mes e as vendas do vendedor

