import module
import csv


def editData():
    
    opt_edit = module.menu(['Data', 'Bairro', 'Habitantes', 'Casos Suspeitos', 'Casos Negativos', 'Casos Confirmados'])

    with open('./PBL_2/dados.csv', 'r', encoding='utf-8', newline='') as archive:
        report = csv.reader(archive)
        headers = next(report) #Cabeçalho
        data = [{header: value for header, value in zip(headers, row)} for row in report]

    column = headers[(opt_edit - 1)]

    all = []

    try:
        line = int(input('Insira a linha que deseja alterar: '))
        value = str(input('Insira o dado atualizado: '))

    except:
        print('Valor inválido!')
        return editData()

    match opt_edit:

        case 1, 2, 3, 4:
            
            for pos, item in enumerate(data):
                if pos == line:
                    toRep = item.update({column:value})
                    data[pos] = toRep

        case 5:
            
            for pos, item in enumerate(data):
                if pos == line:
                    district = item.get('Bairro')
                    negatives = item.get('Casos Negativos')

                    for pos, item in enumerate(data):
                        if item.get('Bairro') == district:
                            all.append(pos)

            sumPosNeg = int(negatives) + int(value)

            all.pop()
            line_to_update = max(all)

            num_suspects = data[line_to_update].get('Casos Suspeitos')

            if sumPosNeg > int(num_suspects):
                print('Número de casos confirmados e negativos é maior que o número de casos suspeitos da data anterior!')
                return editData()

            else:
                upd_suspects = int(num_suspects) - sumPosNeg
                toRep.update({'Casos Suspeitos': upd_suspects})
                data[line_to_update] = toRep

        case 6:

            for pos, item in enumerate(data):
                if pos == line:
                    district = item.get('Bairro')
                    confirmeds = item.get('Casos Confirmados')

                    for pos, item in enumerate(data):
                        if item.get('Bairro') == district:
                            all.append(pos)

            sumPosNeg = int(confirmeds) + int(value)

            all.pop()
            line_to_update = max(all)

            num_suspects = data[line_to_update].get('Casos Suspeitos')

            if sumPosNeg > int(num_suspects):
                print('Número de casos confirmados e negativos é maior que o número de casos suspeitos da data anterior!')
                return editData()

            else:
                upd_suspects = int(num_suspects) - sumPosNeg
                toRep.update({'Casos Suspeitos': upd_suspects})
                data[line_to_update] = toRep

    archive.close()

    with open('./PBL_2/dados.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

        f.close()

editData()


with open('./PBL_2/dados.csv', 'r', encoding='utf-8', newline='') as archive:
        report = csv.reader(archive)
        headers = next(report) #Cabeçalho
        data = [{header: value for header, value in zip(headers, row)} for row in report]

        all = []

        for pos, row in enumerate(data):
            if row.get('Bairro') == district:

                all.append(pos)

                num_suspects = row.get('Casos Suspeitos')
                toRep = row
                
            toRep.update({'Casos Suspeitos': upd_suspects})
            data[max(all)] = toRep

        archive.close()

        with open('./PBL_2/dados.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        f.close()

#QUESTÃO: COMO DEVE SER REFLETIDA OS CASOS SUSPEITOS NA DATA ANTERIOR

for pos, item in enumerate(data):
    if pos + 2 == line:
        district = item.get('Bairro')
        confirmeds = item.get('Casos Confirmados')
        toRep_1 = item #Vai pegar a linha em que será alterada o valor de casos negativos

        for pos, item in enumerate(data):
            if item.get('Bairro') == district:
                all.append(pos)
        break

sumPosNeg = int(confirmeds) + int(value)

all.pop()
line_to_update = max(all)

num_suspects = data[line_to_update].get('Casos Suspeitos')

if sumPosNeg > int(num_suspects):
    print('Número de casos confirmados e negativos é maior que o número de casos suspeitos da data anterior!')
    return editData()

else:
    upd_suspects = int(num_suspects) - sumPosNeg

    toRep_2 = data[line_to_update]

    toRep_2.update({'Casos Suspeitos': upd_suspects})
    toRep_1.update({'Casos Negativos': value})
    data[line_to_update] = toRep #Casos Suspeitos da data anterior
    data[line] = toRep_1 #Casos negativos