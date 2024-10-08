from db_manager import DBManager


def print_menu():
    print('\nМеню:')
    print('1. Добавить куратора')
    print('2. Добавить группу')
    print('3. Добавить студента в группу')
    print('4. Добавить институт')
    print('5. Обновить семестр группы')
    print('6. Удалить студента')
    print('15. Добавить куратора суперюзера')
    print('0. Выход')


def main():
    db = DBManager()

    while True:
        print_menu()
        choice = input('Выберите действие: ')

        if choice == '1':
            surname = input('Введите фамилию куратора: ')
            name = input('Введите имя куратора: ')
            login = input('Введите логин куратора: ')
            password = input('Введите пароль куратора: ')
            db.add_curator(surname, name, login, password)

        elif choice == '2':
            curator_id = input('Введите ID куратора: ')
            name = input('Введите название группы: ')
            semester = input('Введите семестр группы: ')
            institute_id = input('Введите ID института: ')
            db.add_group(curator_id, name, semester, institute_id)

        elif choice == '3':
            group_id = input('Введите ID группы: ')
            surname = input('Введите фамилию студента: ')
            name = input('Введите имя студента: ')
            debts = input('Введите кол-во задолженностей: ')
            db.add_student(group_id, surname, name, debts)

        elif choice == '4':
            name = input('Введите название института: ')
            db.add_institute(name)

        elif choice == '5':
            group_id = input('Введите ID группы: ')
            db.archive_group_and_students(group_id)
            db.update_semester_group(group_id)

        elif choice == '6':
            student_id = input('Введите ID студента: ')
            db.delete_student(student_id)

        elif choice == '15':
            surname = input('Введите фамилию куратора: ')
            name = input('Введите имя куратора: ')
            login = input('Введите логин куратора: ')
            password = input('Введите пароль куратора: ')
            db.add_curator_superuser(surname, name, login, password)

        elif choice == '0':
            print('Выход...')
            db.close()
            break

        else:
            print('Неверный выбор. Попробуйте снова.')


if __name__ == '__main__':
    main()
