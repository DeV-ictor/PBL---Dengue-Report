def menu(list):
    enum = 1
    print('\n')
    for item in list:   
        print(f'{enum}. {item}')
        enum += 1
    print('\n')