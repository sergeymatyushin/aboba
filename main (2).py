allow_numbs = []
k=0
while True:
    k+=1
    num = int(input('Введите число'))
    if (num != 0) and (num < 1001) and (num > -1001):
        allow_numbs.append(num)
    else:
        break
if k>=2:
    a = max(allow_numbs)
    print('Максимальное число: ', a)
    z = min(allow_numbs)
    print('Минимальное число: ', z)
else:
    print("Введеное число не подходит по условиям")
    
