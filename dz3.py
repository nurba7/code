x = int(input('Введите число x:'))
y = int(input('Введите число y:'))

if x > 0 and y > 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 1 ')
elif x < 0 and y > 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 2 ')
elif x < 0 and y < 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 3 ')
elif x > 0 and y < 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 4 ')