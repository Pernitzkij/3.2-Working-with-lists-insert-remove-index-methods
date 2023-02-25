people = int(input('Кол-во сотрудников? '))
list_people = []
for i in range(people):
    cost = int(input(f'Введите зарплату {i + 1} сотрудника? '))
    if cost > 0:
        list_people.append(cost)
    else:
        pass
print()
print(f'Осталось сотрудников: {len(list_people)}')
print(f'Зарплаты: {list_people}')
print()
print(f'Максимальная зп: {max(list_people)}')
print(f'Минимальная зп: {min(list_people)}')
