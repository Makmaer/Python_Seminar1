# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
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