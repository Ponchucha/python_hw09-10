import text_fields


def show_menu(menu_type):
    print(menu_type)


def get_menu_command(menu_type: str):
    menu_len = len(menu_type.split('\n'))-1
    while True:
        command = input(f'Введите число от 1 до {menu_len}: ')
        if command.isdigit() and int(command) <= menu_len:
            return int(command)
        else:
            print(f'Введено неверное значение. Введите число от 1 до {menu_len}: ')


def choose_contact(contact_list: list[dict]):
    if len(contact_list) == 1:
        return 0
    else:
        show_contacts(contact_list)
        return int(input("Введите номер контакта из списка"))-1


def del_edit_message(action: str, name):
    if action == "удалить".lower():
        action = 'удалён'
    if action == 'изменить'.lower():
        action = 'изменён'
    if action == 'добавить'.lower():
        action = 'добавлен'
    print(f"Контакт {name} успешно {action}.")


def edit_contact(action: str, contact_list, index):
    for field_name in contact_list[index].keys():
        contact_list[index][field_name] = input(f'Введите {field_name}: ')


def get_search_request():
    return input("Введите ФИО, номер телефона или комментарий: ")


def show_contacts(contact_list: list[dict]):
    for contact in enumerate(contact_list, 1):
        print(contact)


def del_edit_confirm_message(action: str, contact_list, index):
    print(f'Вы собираетесь {action} контакт: \n {contact_list[index-1]}.\n Продолжить?')
    print(text_fields.contact_action_menu)







