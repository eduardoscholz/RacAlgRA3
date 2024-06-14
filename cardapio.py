user_dict={'bebidas':'coca-cola, agua', 'alimentos':'coxinha, pizza fatia', 'coca-cola':6.00, 'agua':2.00, 'coxinha':5.50, 'pizza fatia':5.50}
while True:
    op=int(input(
    'Selecionar operacao\n'
    '1 Adicionar\n'
    '2 Excluir\n'
    '3 Alterar\n'
    '4 Buscar\n'
    '5 Listar\n'
    '6 Salvar\n'
    '99 Somador\n'))
    if op==1:   #Operação 1
        num_entries = int(input('Quantia de itens para adicionar: '))
        for i in range(num_entries):
            keytoadd = input('Key: ')
            valuetoadd = int(input('Value (deve ser um numero): '))
            user_dict[keytoadd] = valuetoadd

    elif op==2: #Operação 2
        delkey = input('Key do item para ser deletado: ')
        user_dict.pop(delkey)

    elif op==3: #Operação 3
        upkey=input('Key a ser alterada: ')
        if upkey in user_dict:
            upvalue=int(input(f'Novo valor da key {upkey} (deve ser um numero): '))
            user_dict[upkey] = upvalue
            print(f'O valor da key {upkey} agora é {upvalue}')
        else:
            print(f'{upkey} nao esta no dicionario')

    elif op==4: #Operação 4
        keytocheck = input('Key do item para ser mostrado: ')
        if keytocheck in user_dict:
            print(user_dict[keytocheck])
        else:
            print(f'A key {keytocheck} ainda nao foi registrada')

    elif op==5: #Operação 5
        print(user_dict)

    elif op==6: #Operação 6
        txtfilename=input('Insira o nome do arquivo: ') + '.txt'
        with open(txtfilename, 'w') as txt:
            for key, value in user_dict.items():
                txt.write('%s:%s\n' % (key, value))
        print(f'Salvo com exito como {txtfilename}')

    if op==99:
        break
