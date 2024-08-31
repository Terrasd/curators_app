import sqlite3


class DBManager:
    def __init__(self, db_name='curators.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
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

    # Кураторы
    def add_curator(self, surname, name, login, password):
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
        self.cursor.execute('''
            SELECT id, login, is_superuser
            FROM curators
            WHERE login = ? AND password = ?
        ''', (login, password))
        return self.cursor.fetchone()

    # Группы
    def add_group(self, curator_id, name, semester, institute_id):
        self.cursor.execute('''
            INSERT INTO groups (curator_id, name, semester, institute_id)
            VALUES (?, ?, ?, ?)
        ''', (curator_id, name, semester, institute_id))
        self.connection.commit()

    def update_semester_group(self, group_id):
        self.cursor.execute('''
            UPDATE groups
            SET semester = semester + 1
            WHERE id = ?
        ''', (group_id,))
        self.connection.commit()

    def get_group_by_id(self, group_id):
        self.cursor.execute('''
            SELECT * FROM groups
            WHERE id = ?
        ''', (group_id,))
        return self.cursor.fetchall()

    def get_groups_by_curator_id(self, curator_id):
        self.cursor.execute('''
            SELECT name FROM groups
            WHERE curator_id = ?
        ''', (curator_id,))
        return self.cursor.fetchall()

    def get_group_by_name(self, name):
        self.cursor.execute('''
            SELECT id FROM groups
            WHERE name = ?
        ''', (name,))
        return self.cursor.fetchall()

    def get_group_id_by_semester(self, group_id, semester):
        self.cursor.execute('''
            SELECT id FROM archived_groups
            WHERE name = (SELECT name FROM groups WHERE id = ?) AND semester = ?
        ''', (group_id, semester))
        result = self.cursor.fetchone()
        return result[0] if result else None

    # Студенты
    def add_student(self, group_id, surname, name, debts):
        debts = 0 if debts == '' else debts
        self.cursor.execute('''
            INSERT INTO students (group_id, surname, name, debts)
            VALUES (?, ?, ?, ?)
        ''', (group_id, surname, name, debts))
        self.connection.commit()

    def delete_student(self, student_id):
        self.cursor.execute('''
            DELETE FROM students
            WHERE id = ?
        ''', (student_id,))
        self.connection.commit()

    def get_students_by_group(self, group_id, archived=False):
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
        """Обновление задолженности студента в базе данных."""
        new_debt = 0 if new_debt == '' else new_debt
        self.cursor.execute('''
            UPDATE students
            SET debts = ?
            WHERE group_id = ? AND surname = ? AND name = ?
        ''', (new_debt, group_id, surname, name))
        self.connection.commit()

    # Институты
    def add_institute(self, name):
        self.cursor.execute('''
            INSERT INTO institutes (name)
            VALUES (?)
        ''', (name,))
        self.connection.commit()

    # Методы для отправки в архив
    def archive_group_and_students(self, group_id):
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

    # Метод для получения групп по выбранному институту
    def get_groups_by_institute(self, institute_id):
        self.cursor.execute('''
            SELECT name FROM groups
            WHERE institute_id = ?
        ''', (institute_id,))
        return self.cursor.fetchall()

    # Метод для получения всех институтов
    def get_all_institutes(self):
        self.cursor.execute('''
            SELECT id, name FROM institutes
        ''')
        return self.cursor.fetchall()

    def get_institute_by_name(self, name):
        self.cursor.execute('''
            SELECT id FROM institutes
            WHERE name = ?
        ''', (name,))
        return self.cursor.fetchall()

    # Закрытие базы данных
    def close(self):
        self.connection.close()
