path = 'phonebook.txt'
phonebook = []

def open_file():

    with open(path, 'r', encoding='UTF-8') as file:
        txt_strings = file.readlines()
        contact = ''
    for line in txt_strings:
        contact = line.strip().split('|')
        phonebook.append({'ФИО': contact[0],
                         'Номер телефона': contact[1],
                         'Комментарий': contact[2]})


def save_in_file():
    txt_strings = []
    for contact in phonebook:
        txt_strings.append('|'.join(contact.values()))
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(txt_strings))


def get_phonebook():
    return phonebook


def create_contact():
    phonebook.append({'ФИО': '',
                      'Номер телефона': '',
                      'Комментарий': ''})
    return len(phonebook)-1


def del_contact(index, contact_list: list[dict]):
    for i in range(len(phonebook)):
        delete = True
        for field in phonebook[i].keys():
            if contact_list[index][field] != phonebook[i][field]:
                delete = False
        if delete:
            removed = phonebook.pop(i)
            return removed['ФИО']


def find_contact(request: str):
    search_result = []
    for contact in phonebook:
        for data in contact.values():
            if request.lower() in data.lower():
                search_result.append(contact)
                break
    return search_result


def is_confirmed(command):
    if command == 1:
        return True
    else:
        return False





