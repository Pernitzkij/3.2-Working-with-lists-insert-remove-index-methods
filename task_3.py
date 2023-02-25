films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

def new_film():
    user_film = input(f'Название фильма: ')
    if films.count(user_film) > 0:

        print("Команды: добавить, вставить, удалить")
        comand = input('Введите команду: ')
        if comand == 'добавить':
            if user_list.count(user_film) > 0:
                print("Такой фильм уже есть")
            else:
                user_list.append(user_film)
        if comand == 'удалить':
            if films.count(user_film) > 0:
                user_list.remove(user_film)
            else:
                print('Такого фильма у вас нет')
        if comand == 'вставить':
            posishin = int(input('Выберите позицию для вставки фильма: '))
            user_list.insert(posishin - 1, user_film)
    else:
        print("Такого фильма в кинотеатре нет, повторите ввод")
        new_film()




user_list = []
user_list_bag = []

while True:
    print(f'Ваш текущий топ фильмов: {user_list}')
    new_film()

