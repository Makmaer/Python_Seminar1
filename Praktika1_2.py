# 2. Найти максимальное из пяти чисел.
# mas = []
# for i in range(5):
#     x = float(input('input number  '))
#     mas.append(x)
# number = max(mas)
# print(number)
list = [1, 2, 4, 3 ,6]
max = list[0]
for i in list:
    if i >= max: 
        max = i
print(max) 
