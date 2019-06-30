documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(people_by_doc):
    inp_num = input('Введите номер документа: ')
    for cell in people_by_doc:
        num = cell['number']
        person = cell['name']
        if inp_num == num:
            print(person)
            return
    print('Нет такого человека')



def listo(list_of_doc):
    for cell in list_of_doc:
        doc_id = cell['type']
        num = cell['number']
        person = cell['name']
        print(doc_id, person, num)



def shelf(people_by_doc, shelf_of_doc):
    inp_num = input('Введите номер документа: ')
    for cell in people_by_doc:
        num = cell['number']
        if inp_num == num:
            for k, v in shelf_of_doc.items():
                if inp_num in v:
                    print('Документ находится на полке №', k)
                    return
    print('Документа с таким номером не существует')



def add(people_by_doc, shelf_of_doc):
    inp_num = input('Введите номер документа: ')
    inp_doc_id = input('Введите тип документа: ')
    inp_person = input('Введите имя владельца: ')
    inp_shelf = input('Введите номер полки для хранения: ')
    new_dict = {"type": inp_doc_id, "number": inp_num, "name": inp_person}
    people_by_doc.append(new_dict)
    for k, v in shelf_of_doc.items():
        if inp_shelf in k:
            shelf_of_doc[k].append(inp_num)
            print(shelf_of_doc)
            return
    inp_num_list = list()
    shelf_of_doc.update({inp_shelf: inp_num_list})
    shelf_of_doc[inp_shelf].append(inp_num)
    print(shelf_of_doc)



def user_command():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            people(documents)
        elif user_input == 'l':
            listo(documents)
        elif user_input == 's':
            shelf(documents, directories)
        elif user_input == 'a':
            add(documents, directories)
        else:
            print('Такой команды не существует')
        break


from datetime import datetime

class Timer:
    def __init__(self, description):
        self.description = description

    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.now()
        print(f'{self.description}')
        print(f'Время запуска кода: {self.start}')
        print(f'Время окончания работы кода: {self.end}')
        print(f'Продолжительность работы кода: {self.end - self.start}')

with Timer('Параметры выполнения кода: '):
    user_command()




