import random
def victory():
    print('Начинаем Викторину!!!')
    data = [
        '12.04.1961',  # Гагарин
        '06.06.1799',  # Пушкин
        '14.01.1948',  # Харламов
        '17.01.1962',  # Кэрри
        '07.04.1954',  # Джекки Чан
        '17.04.1949',  # Пугачёва
        '06.01.1938',  # Челентано
        '22.06.1941',  # В.О.В
        '07.10.1952',  # Путин
        '18.12.1921'  # Никулин
    ]
    data_dict = {'Первый полёт Гагарина?': '12 апреля 1961 года',
                 'День рождения Пушкина А.С? ': 'Шестое июня 1799 года',
                 'День рождения Валерия Харламова? ': '14 января 1948 года',
                 'День рождения Джима Кэрри? ': '17 января 1962 года',
                 'День рождения Джекки Чана? ': '7 апреля 1954 года',
                 'День рождения Аллы Пугачевой? ': '15 апреля 1949 года',
                 'День рождения Адриано Челентано? ': '6 января 1938 года',
                 'Начало В.О.В? ': '22 июня 1941 года',
                 'День рождения Путина В.В? ': '7 октября 1952 года',
                 'День рождения Юрия Никулина? ': '18 декабря 1921 года'}

    user = ['Первый полёт Гагарина?', 'День рождения Валерия Харламова? ', 'День рождения Джима Кэрри? ',
            'День рождения Пушкина А.С? ', 'День рождения Джекки Чана? ', 'День рождения Аллы Пугачевой? ',
            'День рождения Адриано Челентано? ', 'Начало В.О.В? ', 'День рождения Путина В.В? ',
            'День рождения Юрия Никулина? ']

    game = ['да', 'Да', 'ДА']
    over = ['нет', 'Нет', 'НЕТ']
    question = ''

    while not question in over:
        correct_answer = 0
        wrong_answer = 0
        result = random.sample(user, 5)
        for i in result:
            if input(i) in data:
                print('Правильно,\nИдём дальше! ')
                correct_answer += 1
                print('-' * 50)
            else:
                print('Неверный ответ или ввод!')
                print('Правильный ответ: ', data_dict.get(i))
                wrong_answer += 1
                print('-' * 50)

        print('Верно:', correct_answer, '\nОшибки:', wrong_answer)
        question = input('Хотите начать сначала? ')
        if question in game:
            print('Продолжаем!')
            print('-' * 50)
        elif question in over:
            print('Всего Вам доброго!')
        else:
            print('Не правильный ввод\nПрограмма закрыта!')
            break