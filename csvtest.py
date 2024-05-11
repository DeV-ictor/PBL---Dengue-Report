import csv
import time
import module

#Inicialização das variáveis

opt_1 = ''

#Leitura do arquivo

with open ('dados.csv', 'r') as archive:
    relatorio = csv.reader(archive, delimiter = ",")
    for i in relatorio:
        print(i)

while opt_1 != '3':

    print('==== DENGUE ====')

    module.menu(['Sobre a Dengue', 'Relatório de Dados', 'Sair'])

    opt_1 = str(input('Insira uma opção: '))

    if opt_1 == '1':
        