from date_create import *


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'
def add_contact(contact):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)


def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        # print(file.read().rstrip())
        for contact in enumerate(contacts_list,1):
            print(*contact)
            
            
            
def copy_contact():
   
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list, 1):
            print(nn,contact, '\n')
        num_copy = int(input('Выберите номер контакта, который хотите скопировать: '))
        index_contact = num_copy - 1
        
    with open('copy_phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{contacts_list[index_contact]}\n\n')
        
        
# def copy_line(source_file, destination_file, line_number):
#     with open('phonebook.txt', 'r', encoding='UTF-8') as file:
#         source_file = 'phonebook.txt'
#         destination_file = 'destination_file.txt'
#         lines = file.readlines()
#         if 1 <= line_number <= len(lines):
#             line_to_copy = lines[line_number - 1]
#             with open('destination_file.txt', 'a') as file2:
#                 file2.write(line_to_copy)
#         else:
#             print("Номер строки вне диапазона.")
        
#=============================================================================        

def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу\n'
    )
    var_search = input('Выберите вариант поиска: ')

    while var_search not in ('1', '2', '3', '4', '5'):
        print('Некорректные данные, нужно ввести число комманды')
        var_search = input('Введите вариант поиска: ')


    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)