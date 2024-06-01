import csv
import os

#MENU

def menu(list):

    enum = 1
    print('\n')
    for item in list:   
        print(f'{enum}. {item}')
        enum += 1
    print('\n')

    try:
        option = int(input('Insira uma opção: '))
        return option
    except:
        print('\nOpção inválida!')
        return menu(list)
    
#VISUALIZAÇÃO COMPLETA

def getFullData(data):
    
    date = 'Data'
    district = 'Bairro'
    population = 'Habitantes'
    suspects = 'Casos Suspeitos'
    negatives = 'Casos Negativos'
    confirmeds = 'Casos Confirmados'

    print(f'| {date.center(10)} | | {district.center(20)} | | {population.center(10)} | | {suspects.center(15)} | | {negatives.center(15)} | | {confirmeds.center(17)} |')
    print('--------------------------------------------------------------------------------------------------------------------\n')

    for item in data:
        data_date = item.get('Data')
        data_district = item.get('Bairro')
        data_population = item.get('Habitantes')
        data_suspects = item.get('Casos Suspeitos')
        data_negatives = item.get('Casos Negativos')
        data_confirmeds = item.get('Casos Confirmados')

        print(f'| {data_date.center(10)} | | {data_district.center(20)} | | {data_population.center(10)} | | {data_suspects.center(15)} | | {data_negatives.center(15)} | | {data_confirmeds.center(17)} |')
        print('--------------------------------------------------------------------------------------------------------------------')

#PERCENTUAL DE CASOS TOTAIS

def getFullPercent(data):

    data_suspect = 0
    data_negative = 0
    data_confirmed = 0

    data_population = 0

    for item in data:
        data_suspect += int(item.get('Casos Suspeitos'))
        data_negative += int(item.get('Casos Negativos'))
        data_confirmed += int(item.get('Casos Confirmados'))

        data_population += int(item.get('Habitantes'))
        
    percent_data_suspect = 100 * data_suspect / data_population
    percent_data_negative = 100 * data_negative / data_population
    percent_data_confirmed =  100 * data_confirmed / data_population

    print(f'\nHabitantes: {data_population}\n \nPercentual de casos suspeitos: {percent_data_suspect:.2f}% \nPercentual de casos negativos: {percent_data_negative:.2f}% \nPercentual de casos confirmados: {percent_data_confirmed:.2f}%\n')

#COLETAR AS INFORMAÇÕES POR DATA SOLICITADA

def getDataByDate(data):

    try:
        date = str(input('\nInsira a data de visualização: '))

    except:
        print('\nData inválida!')
        return getDataByDate(data)

    count = 0

    for item in data:
        if date in item.values():
            print(f' \n=== {item.get('Bairro')} ===\n Habitantes: {item.get('Habitantes')}\n Casos Suspeitos: {item.get('Casos Suspeitos')}\n Casos Negativos: {item.get('Casos Negativos')}\n Casos Confirmados: {item.get('Casos Confirmados')}\n')
            count += 1
        
    if count == 0:
        print('Data inválida!')
        return getDataByDate(data)
    
#COLETAR AS INFORMAÇÕES POR BAIRRO SOLICITADO

def getDataByDistrict(data):

    try:
        district = str(input('\nInsira o bairro para visualização: '))
        district = district.title()

    except:
        print('\nBairro inválido!')
        return getDataByDistrict(data)

    count = 0

    for item in data:
        if district in item.values():
            info = (f' \n=== {item.get('Bairro')} === \n Data: {item.get('Data')} \n Habitantes: {item.get('Habitantes')}\n Casos Suspeitos: {item.get('Casos Suspeitos')}\n Casos Negativos: {item.get('Casos Negativos')}\n Casos Confirmados: {item.get('Casos Confirmados')}\n')
            print(info.ljust(20))
            count += 1

    if count == 0:
        print('Bairro inválido!')
        return getDataByDistrict(data)
        
#COMPARAÇÃO DE CASOS POSITIVOS E NEGATIVOS PARA DUAS DATAS

def getDataDateByDate(data):

    try:
        ref_date = str(input('\nInsira a data inicial: '))
        comp_date = str(input('\nInsira a data final: '))

    except:
        print('Valores inválidos!')
        return getDataDateByDate(data)
    

    count = 0 #Verificar se possui os itens

    ref_data_pos = 0 #Acumulador de casos positivos na data referencial
    ref_data_neg = 0 #Acumulador de casos negativos na data referencial

    comp_data_pos = 0 #Acumulador de casos positivos na data comparativa
    comp_data_neg = 0 #Acumulador de casos negativos na data comparativa
    
    for item in data:
        if item.get('Data') == ref_date:
            ref_data_pos += int(item.get('Casos Confirmados'))
            ref_data_neg += int(item.get('Casos Negativos'))
            count += 1

        elif item.get('Data') == comp_date:
            comp_data_pos += int(item.get('Casos Confirmados'))
            comp_data_neg += int(item.get('Casos Negativos'))
            count += 1
        
    if count < 50:
        print('\nDatas inválidas ou ainda não atualizadas! Selecione uma outra data!')
        return getDataDateByDate(data)
        
    data_pos = comp_data_pos - ref_data_pos 
    data_neg = comp_data_neg - ref_data_neg 

    percent_pos = 100 * comp_data_pos / ref_data_pos
    percent_neg = 100 * comp_data_neg / ref_data_neg

    if data_pos > 0:
        print(f'Houve um aumento na quantidade de casos confirmados, com um aumento de {data_pos} casos confirmados e aumento percentual de {percent_pos:.1f}%.')

    elif data_pos < 0:
        print(f'Houve uma redução na quantidade de casos confirmados, com uma redução de {data_pos} casos confirmados e redução percentual de {percent_pos:.1f}%.')
    elif data_pos == 0:
        print(f'Não houve variação na quantidade de casos confirmados. A variação foi de 0 casos.')    

    if data_neg > 0:
        print(f'Houve um aumento na quantidade de casos negativos, com um aumento de {data_neg} casos negativos e aumento percentual de {percent_neg:.1f}%.')
    elif data_neg < 0:
        print(f'Houve uma redução na quantidade de casos negativos, com uma redução de {data_pos} casos negativos e redução percentual de {percent_neg:.1f}%.')
    elif data_neg == 0:
        print(f'Não houve variação na quantidade de casos negativos. A variação foi de 0 casos.')

#Percentual de casos confirmados e suspeitos por bairro:

def getPercentByDistrict(data):
    
    try:
        district = str(input('\nInsira o bairro para visualização: '))
        district.capitalize()

    except:
        print('\nBairro inválido!')
        return getDataByDistrict(data)
    
    data_suspect = 0
    data_negative = 0
    data_confirmed = 0

    count = 0

    for item in data:
        if item.get('Bairro') == district:
            data_suspect += int(item.get('Casos Suspeitos'))
            data_negative += int(item.get('Casos Negativos'))
            data_confirmed += int(item.get('Casos Confirmados'))

            data_population = int(item.get('Habitantes'))

            count += 1

    if count == 0:
        print('\nBairro inválido!')
        return getPercentByDistrict(data)
        
    percent_data_suspect = 100 * data_suspect / data_population
    percent_data_negative = 100 * data_negative / data_population
    percent_data_confirmed =  100 * data_confirmed / data_population

    print(f'\nBairro selecionado: {district} \nHabitantes: {data_population} \nPercentual de casos suspeitos: {percent_data_suspect:.2f}% \nPercentual de casos negativos: {percent_data_negative:.2f}% \nPercentual de casos confirmados: {percent_data_confirmed:.2f}%')

#GRAVAÇÃO DE NOVOS DADOS

def dataUpdate():

    #PRECISAMOS MANTER O MÓDULO RODANDO ATÉ O USUÁRIO DECIDIR PARAR

    with open('./PBL_2/dados.csv', 'r', encoding='utf-8', newline='') as archive:
        report = csv.reader(archive)
        headers = next(report) #Cabeçalho
        data = [{header: value for header, value in zip(headers, row)} for row in report]

    all_districts = ['Tomba', 'Campo Limpo', 'Muchila', 'Conceição', 'Brasília', 'Mangabeira', 'Calumbi', 'Queimadinha', 'Gabriela', 'Parque Ipê', 'Jardim Cruzeiro', 'Rua Nova', 'Lagoa Grande', 'Aviário', 'Santa Mônica', 'Centro', 'Pedra de Descanso', 'Caseb', 'São João', 'Cidade Nova', 'Jardim Acácia', 'Serraria Brasil', 'Baraúna', 'Cis', 'Ponto Central']

    for i in all_districts:

        print(f'\nAtualizando: {i}\n')

        district = i

        try:
            date = str(input('Data: '))
            population = str(input('Habitantes: '))
            suspects = int(input('Casos Suspeitos: '))
            confirmeds = int(input('Casos Negativos: '))
            negatives = int(input('Casos Confirmados: '))

        except:
            print('Valor inválido!')
            return dataUpdate()
        
        #ATUALIZAÇÃO DO NÚMERO DE SUSPEITOS

        #ATUALIZAR NOVOS DADOS

        with open('./PBL_2/dados.csv', 'a', encoding='utf-8', newline='') as dataAppend:
            newData = csv.DictWriter(dataAppend, fieldnames=headers)
            newData.writerow({'Data': date, 'Bairro': district, 'Habitantes': population, 'Casos Suspeitos':suspects, 'Casos Confirmados': confirmeds, 'Casos Negativos': negatives})

def editData():
    opt_edit = menu(['Data', 'Bairro', 'Habitantes', 'Casos Suspeitos', 'Casos Negativos', 'Casos Confirmados'])

    with open('./PBL_2/dados.csv', 'r', encoding='utf-8', newline='') as archive:
        report = csv.reader(archive)
        headers = next(report) #Cabeçalho
        data = [{header: value for header, value in zip(headers, row)} for row in report]

    column = headers[(opt_edit - 1)]

    try:
        line = int(input('Insira a linha que deseja alterar: '))
        value = str(input('Insira o dado atualizado: '))

    except:
        print('Valor inválido!')
        return editData()

    match opt_edit:

        case 1 | 2 | 3 | 4 | 5 :
            
            for pos, item in enumerate(data):
                if pos + 2 == line:
                    toRep = item
                    break
            
            toRep.update({column:value})
            data[pos] = toRep

    archive.close()

    with open('./PBL_2/dados.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

        f.close()