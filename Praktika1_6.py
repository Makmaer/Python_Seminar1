#6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
a=0
dniNedeli = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ' ,'СБ' ,'ВС']
if 1<=a<=7:
    print(dniNedeli[a-1])
    if a>5: 
        print('vihodnoy')
    else: 
        print('rabochiy')
else: 
    print('oshibka')
