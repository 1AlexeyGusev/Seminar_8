from logger import *

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    command = '-1' #инициализация 
    while command != '4':
        print(
            'Возможные варианты взаимодействия:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Скопировать контакт\n'
            '5. Выход из программы'
        )

        command = input('Выберите команду: ')

        while command not in ('1', '2', '3', '4'):    # проверка на корректность ввода 
            print('Некорректный ввод...')
        # command = input('Введите номер действия: ')

        match command:  #по сути аналог if/elif/else
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                copy_contact()
            case '5':
                print('Всего хорошего!')