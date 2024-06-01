#Autor: Adson Victor de Souza Alves
#Componente Curricular: Algoritmos e Programação I
#Concluido em: 01/06/2024

#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

#Importação de bibliotecas

import csv
import os
import module

#Leitura do arquivo

def main():

    opt_1 = 0 #Variável pra inicialização

    with open('./PBL_2/dados.csv', 'r', encoding='utf-8', newline='') as archive:
        report = csv.reader(archive)
        headers = next(report) #Cabeçalho
        data = [{header: value for header, value in zip(headers, row)} for row in report]

    while opt_1 != 3:

        print('======= DENGUE =======')

        opt_1 = module.menu(['Sobre a Dengue', 'Dados', 'Sair'])

        match opt_1:

            case 1:

                txt_1 = 'A dengue é uma doença viral transmitida'
                txt_2 = 'principalmente pelos mosquitos Aedes aegypti'
                txt_3 = 'e Aedes albopictus. É uma doença endêmica em'
                txt_4 = 'muitas partes do mundo, incluindo o Brasil,'
                txt_5 = 'e representa um grande desafio de saúde pública'
                txt_6 = 'devido à sua disseminação rápida e aos surtos sazonais.'

                texts = [txt_1, txt_2, txt_3, txt_4, txt_5, txt_6]

                for txt in texts:
                    txt.center(50)
                    print(txt)

            case 2:
                opt_2 = module.menu(['Visualizar Dados', 'Atualizar Dados', 'Voltar'])
                
                match opt_2:

                    case 1:
                        opt_3 = module.menu(['Visualização completa', 'Visualização por data', 'Visualização por bairro', 'Voltar'])

                        match opt_3:

                            case 1:
                                opt_fullview = module.menu(['Visualizar Todos os Dados', 'Percentual de Casos'])

                                match opt_fullview:

                                    case 1:
                                        os.system('cls||clear')
                                        module.getFullData(data)
                                    
                                    case 2:
                                        module.getFullPercent(data)
                                        return 
                            
                            case 2:
                                opt_dateview = module.menu(['Visualizar Única Data', 'Comparar Datas'])

                                match opt_dateview:

                                    case 1:
                                        module.getDataByDate(data)

                                    case 2:
                                        module.getDataDateByDate(data)
                            
                            case 3:
                                opt_districtview = module.menu(['Visualizar Único Bairro', 'Percentual de Casos'])

                                match opt_districtview:

                                    case 1:
                                        module.getDataByDistrict(data)

                                    case 2:
                                        module.getPercentByDistrict(data)

                            case 4:
                                print('\n')
                                return main()

                    case 2:
                        opt_dataupd = module.menu(['Registrar nova data', 'Editar'])

                        match opt_dataupd:

                            case 1:
                                module.dataUpdate()

                            case 2:
                                module.editData()

                    case 3:
                        print('\n')
                        return main()

            case 3:
                print('\n')
                print('Sistema encerrado.')

if __name__ == "__main__":
    main()