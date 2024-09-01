import sqlite3


class DBManager:
    def __init__(self, db_name='curators.db'):
        """
        Инициализация менеджера базы данных.

        :param db_name: Имя файла базы данных. По умолчанию 'curators.db'.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Создание таблиц в базе данных, если они не существуют.
        """
        # Таблица кураторов
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS curators (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                surname TEXT NOT NULL,
                name TEXT NOT NULL,
                login TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                is_superuser INTEGER DEFAULT 0
            )
        ''')

        # Таблица групп
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curator_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                semester INTEGER NOT NULL,
                institute_id INTEGER NOT NULL,
                FOREIGN KEY (curator_id) REFERENCES curators (id) ON DELETE CASCADE,
                FOREIGN KEY (institute_id) REFERENCES institutes (id) ON DELETE CASCADE
            )
        ''')

        # Таблица студентов
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_id INTEGER NOT NULL,
                surname TEXT NOT NULL,
                name TEXT NOT NULL,
                debts INTEGER NOT NULL,
                FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE CASCADE
            )
        ''')

        # Таблица институтов
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS institutes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')

        # Таблица с информацией о группах за прошлые семестры
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS archived_groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curator_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                semester TEXT NOT NULL,
                institute_id INTEGER NOT NULL,
                FOREIGN KEY (curator_id) REFERENCES curators (id) ON DELETE CASCADE,
                FOREIGN KEY (institute_id) REFERENCES institutes (id) ON DELETE CASCADE
            )
        ''')

        # Таблица с информацией о студентах за прошлые семестры
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS archived_students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_id INTEGER NOT NULL,
                surname TEXT NOT NULL,
                name TEXT NOT NULL,
                debts INTEGER,
                semester INTEGER,
                FOREIGN KEY (group_id) REFERENCES archived_groups (id) ON DELETE CASCADE
            )
        ''')

        self.connection.commit()

    # Методы для работы с кураторами
    def add_curator(self, surname, name, login, password):
        """
        Добавление нового куратора.

        :param surname: Фамилия куратора.
        :param name: Имя куратора.
        :param login: Логин куратора.
        :param password: Пароль куратора.
        """
        try:
            self.cursor.execute('''
                INSERT INTO curators (surname, name, login, password)
                VALUES (?, ?, ?, ?)
            ''', (surname, name, login, password))
            self.connection.commit()
            print(f'Куратор "{login}" успешно добавлен.')
        except sqlite3.IntegrityError:
            print(f'Куратор с логином "{login}" уже существует.')

    def add_curator_superuser(self, surname, name, login, password):
        """
        Добавление нового суперпользователя-куратора.

        :param surname: Фамилия куратора.
        :param name: Имя куратора.
        :param login: Логин куратора.
        :param password: Пароль куратора.
        """
        try:
            self.cursor.execute('''
                INSERT INTO curators (surname, name, login, password, is_superuser)
                VALUES (?, ?, ?, ?, 1)
            ''', (surname, name, login, password))
            self.connection.commit()
            print(f'Куратор-superuser "{login}" успешно добавлен.')
        except sqlite3.IntegrityError:
            print(f'Куратор с логином "{login}" уже существует.')

    def verify_curator(self, login, password):
        """
        Проверка существования куратора с указанным логином и паролем.

        :param login: Логин куратора.
        :param password: Пароль куратора.
        :return: Кортеж с id, логином и статусом суперпользователя, если куратор найден; иначе None.
        """
        self.cursor.execute('''
            SELECT id, login, is_superuser
            FROM curators
            WHERE login = ? AND password = ?
        ''', (login, password))
        return self.cursor.fetchone()

    # Методы для работы с группами
    def add_group(self, curator_id, name, semester, institute_id):
        """
        Добавление новой группы.

        :param curator_id: ID куратора, ответственного за группу.
        :param name: Название группы.
        :param semester: Номер семестра.
        :param institute_id: ID института.
        """
        self.cursor.execute('''
            INSERT INTO groups (curator_id, name, semester, institute_id)
            VALUES (?, ?, ?, ?)
        ''', (curator_id, name, semester, institute_id))
        self.connection.commit()

    def update_semester_group(self, group_id):
        """
        Обновление семестра группы.

        :param group_id: ID группы.
        """
        self.cursor.execute('''
            UPDATE groups
            SET semester = semester + 1
            WHERE id = ?
        ''', (group_id,))
        self.connection.commit()

    def get_group_by_id(self, group_id):
        """
        Получение информации о группе по её ID.

        :param group_id: ID группы.
        :return: Список кортежей с данными о группе.
        """
        self.cursor.execute('''
            SELECT * FROM groups
            WHERE id = ?
        ''', (group_id,))
        return self.cursor.fetchall()

    def get_groups_by_curator_id(self, curator_id):
        """
        Получение списка групп по ID куратора.

        :param curator_id: ID куратора.
        :return: Список названий групп.
        """
        self.cursor.execute('''
            SELECT name FROM groups
            WHERE curator_id = ?
        ''', (curator_id,))
        return self.cursor.fetchall()

    def get_group_by_name(self, name):
        """
        Получение информации о группе по её названию.

        :param name: Название группы.
        :return: Список ID групп.
        """
        self.cursor.execute('''
            SELECT id FROM groups
            WHERE name = ?
        ''', (name,))
        return self.cursor.fetchall()

    def get_group_id_by_semester(self, group_id, semester):
        """
        Получение ID группы по названию и семестру из архива.

        :param group_id: ID группы.
        :param semester: Номер семестра.
        :return: ID группы из архива или None, если группа не найдена.
        """
        self.cursor.execute('''
            SELECT id FROM archived_groups
            WHERE name = (SELECT name FROM groups WHERE id = ?) AND semester = ?
        ''', (group_id, semester))
        result = self.cursor.fetchone()
        return result[0] if result else None

    # Методы для работы со студентами
    def add_student(self, group_id, surname, name, debts):
        """
        Добавление нового студента в группу.

        :param group_id: ID группы.
        :param surname: Фамилия студента.
        :param name: Имя студента.
        :param debts: Задолженность студента.
        """
        debts = 0 if debts == '' else debts
        self.cursor.execute('''
            INSERT INTO students (group_id, surname, name, debts)
            VALUES (?, ?, ?, ?)
        ''', (group_id, surname, name, debts))
        self.connection.commit()

    def delete_student(self, student_id):
        """
        Удаление студента по его ID.

        :param student_id: ID студента.
        """
        self.cursor.execute('''
            DELETE FROM students
            WHERE id = ?
        ''', (student_id,))
        self.connection.commit()

    def get_students_by_group(self, group_id, archived=False):
        """
        Получение списка студентов по ID группы.

        :param group_id: ID группы.
        :param archived: Флаг, указывающий, нужно ли получить студентов из архива.
        :return: Список кортежей с данными о студентах.
        """
        if archived:
            self.cursor.execute('''
                SELECT surname, name, debts FROM archived_students
                WHERE group_id = ?
            ''', (group_id,))
        else:
            self.cursor.execute('''
                SELECT surname, name, debts FROM students
                WHERE group_id = ?
            ''', (group_id,))
        return self.cursor.fetchall()

    def get_students_by_semester(self, group_id, semester, archived=False):
        """
        Получение списка студентов по ID группы и семестру.

        :param group_id: ID группы.
        :param semester: Номер семестра.
        :param archived: Флаг, указывающий, нужно ли получить студентов из архива.
        :return: Список кортежей с данными о студентах.
        """
        if archived:
            self.cursor.execute('''
                SELECT surname, name, debts
                FROM archived_students
                WHERE group_id = ? AND semester = ?
            ''', (group_id, semester))
        else:
            # Для текущих студентов не нужно учитывать семестр в запросе
            self.cursor.execute('''
                SELECT surname, name, debts
                FROM students
                WHERE group_id = ?
            ''', (group_id,))
        return self.cursor.fetchall()

    def update_student_debt(self, group_id, surname, name, new_debt):
        """
        Обновление задолженности студента в базе данных.

        :param group_id: ID группы.
        :param surname: Фамилия студента.
        :param name: Имя студента.
        :param new_debt: Новая задолженность.
        """
        new_debt = 0 if new_debt == '' else new_debt
        self.cursor.execute('''
            UPDATE students
            SET debts = ?
            WHERE group_id = ? AND surname = ? AND name = ?
        ''', (new_debt, group_id, surname, name))
        self.connection.commit()

    # Методы для работы с институтами
    def add_institute(self, name):
        """
        Добавление нового института.

        :param name: Название института.
        """
        self.cursor.execute('''
            INSERT INTO institutes (name)
            VALUES (?)
        ''', (name,))
        self.connection.commit()

    def get_groups_by_institute(self, institute_id):
        """
        Получение списка групп по ID института.

        :param institute_id: ID института.
        :return: Список названий групп.
        """
        self.cursor.execute('''
            SELECT name FROM groups
            WHERE institute_id = ?
        ''', (institute_id,))
        return self.cursor.fetchall()

    def get_all_institutes(self):
        """
        Получение списка всех институтов.

        :return: Список кортежей с ID и названиями институтов.
        """
        self.cursor.execute('''
            SELECT id, name FROM institutes
        ''')
        return self.cursor.fetchall()

    def get_institute_by_name(self, name):
        """
        Получение ID института по его названию.

        :param name: Название института.
        :return: Список ID институтов.
        """
        self.cursor.execute('''
            SELECT id FROM institutes
            WHERE name = ?
        ''', (name,))
        return self.cursor.fetchall()

    # Методы для работы с архивом
    def archive_group_and_students(self, group_id):
        """
        Архивирование группы и её студентов.

        :param group_id: ID группы, которую нужно архивировать.
        """
        # Получаем текущий семестр группы
        self.cursor.execute('''
            SELECT semester FROM groups WHERE id = ?
        ''', (group_id,))
        semester = self.cursor.fetchone()[0]

        # Копируем группу в архив
        self.cursor.execute('''
            INSERT INTO archived_groups (curator_id, name, semester, institute_id)
            SELECT curator_id, name, ?, institute_id
            FROM groups
            WHERE id = ?
        ''', (semester, group_id))

        # Копируем всех студентов группы в архив с указанием семестра
        self.cursor.execute('''
            INSERT INTO archived_students (group_id, surname, name, debts, semester)
            SELECT ?, surname, name, debts, ?
            FROM students
            WHERE group_id = ?
        ''', (group_id, semester, group_id))

        # Сохраняем изменения в базе данных
        self.connection.commit()

    # Закрытие базы данных
    def close(self):
        """
        Закрытие соединения с базой данных.
        """
        self.connection.close()
