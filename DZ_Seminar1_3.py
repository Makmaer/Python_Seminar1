# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x=0
y=1
if x>0 and y>0:
    print('первая четверть')
elif x>0 and y<0:
    print('четвертая четверть')
elif x<0 and y>0:
    print('вторая четверть')    
elif x<0 and y<0:
    print('третья четверть')
elif x==0 and y==0:
    print('точка в начале координат')
elif x==0 and y!=0:
    print('точка на оси y')
elif y==0 and x!=0:
    print('точка на оси x')   