zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
print(f'Зоопарк: {zoo}')

i_lion = zoo.index('lion')
print(f'Лев сидит в клетке номер {i_lion + 1}')
zoo.insert(i_lion + 1, 'bear')

zoo.remove('elephant')
print(f"Обезьяна сидит в клетке номер {zoo.index('monkey') + 1}")
