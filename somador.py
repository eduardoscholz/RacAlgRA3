import cardapio as cd
bill_list=[]
add_item=''
quit=''
while quit!='y':
    while add_item!='n':
        order=input('Itens pedidos: ')
        if order in cd.user_dict:
            bill_list.append(cd.user_dict[order])
        else:
            print('Item nao existente')
        add_item=input('Gostaria de adicionar outro item no pedido? [Y/N]\n')
    tip=int(input('Qual a gorjeta dada pelo cliente (porcentagem)\n'))
    finalbill=sum(bill_list)*((tip+100)/100)
    print(f'A conta e de R$ {round(finalbill, 2)}')
    quit=input('Gostaria de sair do programa? [Y/N]\n')
    add_item=''
    bill_list=[]
