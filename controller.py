import model
import view
import text_fields


def search_contact():
    print('Поиск контакта')
    request = view.get_search_request()
    result = model.find_contact(request)
    if len(result):
        return result
    else:
        print(text_fields.not_found)
        return False


def contact_choose_confirm(action:str):
    pass

def start():
    model.open_file()
    while True:
        phonebook = model.get_phonebook()
        view.show_menu(text_fields.main_menu)
        command = view.get_menu_command(text_fields.main_menu)
        match command:
            case 1:
                view.show_contacts(phonebook)                       #1. Отобразить все контакты
            case 2:
                index = model.create_contact()
                view.edit_contact('добавлен', phonebook, index)        #2. Добавить новый контакт
            case 3:

                view.show_contacts(search_contact())                          #3. Найти контакт

            case 4:                                                             #4. Изменить контакт

                action = "изменить"
                whats_found = search_contact()                 # Тут надо сделать функцию, но уже не успеваю, поэтому лапша, сорри
                if whats_found:
                    index = view.choose_contact(whats_found)
                    view.del_edit_confirm_message(action, whats_found, index)
                    decision = view.get_menu_command(text_fields.contact_action_menu)
                    confirm = model.is_confirmed(decision)
                    if confirm:
                        view.edit_contact(action, whats_found, index)
                        name = whats_found[index]["ФИО"]
                        view.del_edit_message(action, name)

            case 5:                                                  #5. Удалить контакт
                action = "удалить"
                whats_found = search_contact()
                if whats_found:
                    view.show_contacts(whats_found)
                    index = view.choose_contact(whats_found)
                    view.del_edit_confirm_message(action, whats_found, index)
                    decision = view.get_menu_command(text_fields.contact_action_menu)
                    confirm = model.is_confirmed(decision)
                if confirm:
                    name = model.del_contact(index, whats_found)
                    view.del_edit_message(action, name)
            case 6:
                model.save_in_file()                                #6. Сохранить изменения
                print("Данные успешно сохранены в файл")
