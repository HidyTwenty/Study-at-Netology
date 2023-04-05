documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}


def search_for_a_person_by_number():
    document_number = input('Введите номер документа: ')
    for document in documents:
        if document['number'] == document_number:
            name_by_number = document['name']
            return (name_by_number)
# использовал return, только для того, чтобы закрепить лекцию


def shelf_search_by_number():
    document_number = input('Введите номер документа: ')
    for directory_key, directory_value in directories.items():
        if document_number in directory_value:
            shelf_by_number = directory_key
            return shelf_by_number
# использовал return, только для того, чтобы закрепить лекцию

def list_of_documents():
    for document in documents:
        list = document['type'], document['number'], document['name']
        print(list)


def add_new_document():
    new_type = input('Введите тип документа: ')
    new_number = input('Введите номер документа: ')
    new_name = input('Введите имя: ')
    new_shelf = int(input('Введите номер полки: '))
    if new_shelf == 1 or new_shelf == 2 or new_shelf == 3:
        documents.append({
            'type': new_type,
            'number': new_number,
            'name': new_name
        })
        new_shelf = str(new_shelf)
        directories[new_shelf].append(new_number)
    else:
        print('Введен некорректный номер')

def main():
    while True:
        comand = input('Введите команду: ')
        if comand == 'p':
            res = search_for_a_person_by_number()
            print(res)
        elif comand == 's':
            res = shelf_search_by_number()
            print(res)
        elif comand == 'l':
            list_of_documents()
        elif comand == 'a':
            add_new_document()
        else:
            print('Вы ввели несуществующую команду')

main()
