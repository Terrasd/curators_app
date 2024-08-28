import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from src.styles.styles import get_invalid_login_style
from interface.interface import Ui_MainWindow
from db.db_manager import DBManager
from user_widgets.confirmation_window import ConfirmationDialog


class Window:
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.db = DBManager()

        # Список со всеми вкладками семестров
        self.group_table_views = [
            self.ui.group_table_view_1,
            self.ui.group_table_view_2,
            self.ui.group_table_view_3,
            self.ui.group_table_view_4,
            self.ui.group_table_view_5
        ]

        # Установка активным окно входа
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)

        # Кнопки
        self.ui.btn_enter_account.clicked.connect(self.auth_page)
        self.ui.btn_logout.clicked.connect(self.confirm_logout)

        # Инициализация ID куратора
        self.current_curator_id = None

        # Фиксация переключения вкладок с семестрами
        self.ui.group_tables_semesters.currentChanged.connect(
            self.update_students_table)

        # Фиксация переключения группы
        self.ui.choice_group.currentTextChanged.connect(
            self.update_students_table)

    def show(self):
        """Отображение окна приложения."""
        self.window.show()

    def auth_page(self):
        """Авторизация пользователя."""
        login = self.ui.login_enter.text()
        password = self.ui.password_enter.text()

        curator = self.db.verify_curator(login, password)

        if curator:
            self.ui.text_invalid_log_or_pass.clear()

            # Сохраняем ID текущего куратора
            self.current_curator_id = curator[0]
            self.ui.stackedWidget.setCurrentWidget(self.ui.students_page)

            # Загружаем группы куратора в comboBox
            sql_groups = self.db.get_groups_by_curator_id(
                self.current_curator_id)
            groups_list = [row[0] for row in sql_groups]
            self.ui.choice_group.clear()
            self.ui.choice_group.addItems(groups_list)

            # Обновляем таблицу для выбранной по умолчанию группы
            self.update_students_table()
        else:
            self.ui.text_invalid_log_or_pass.clear()
            shadow_effect, style, text = get_invalid_login_style()
            self.ui.text_invalid_log_or_pass.setText(text)
            self.ui.text_invalid_log_or_pass.setStyleSheet(style)
            self.ui.text_invalid_log_or_pass.setGraphicsEffect(shadow_effect)

    def update_students_table(self):
        """Обновление таблицы на основе выбранной группы и активной вкладки."""
        if self.current_curator_id is None:
            return

        # Получаем выбранную группу из списка групп
        selected_group = self.ui.choice_group.currentText()
        id_group = self.db.get_group_by_name(selected_group)

        # Проверяем, что группа выбрана
        if selected_group and id_group:
            id_group = id_group[0][0]

            # Получаем информацию о группе
            group_info = self.db.get_group_by_id(id_group)
            group_semester = group_info[0][3]  # Семестр группы

            # Обновляем данные для каждой вкладки
            for i in range(5):
                semester = i + 1
                if semester == group_semester:
                    # Текущий семестр (текущие данные)
                    students = self.db.get_students_by_semester(
                        id_group, semester, archived=False
                    )
                elif semester < group_semester:
                    # Архивные данные для семестров до текущего
                    students = self.db.get_students_by_semester(
                        id_group, semester, archived=True
                    )
                else:
                    # Пустая таблица для будущих семестров
                    students = []

                # Заполняем таблицу данными студентов
                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(
                    ['Фамилия', 'Имя', 'Задолженности']
                )
                for student in students:
                    surname_item = QStandardItem(student[0])
                    name_item = QStandardItem(student[1])
                    debts_item = QStandardItem(str(student[2]))
                    model.appendRow([surname_item, name_item, debts_item])

                # Устанавливаем модель в таблицу на соответствующей вкладке
                self.group_table_views[i].setModel(model)

    def confirm_logout(self):
        dialog = ConfirmationDialog(self.window)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            self.ui.login_enter.clear()
            self.ui.password_enter.clear()
            self.current_curator_id = None
            self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
            self.ui.choice_group.clear()
            # Очистка всех таблиц
            for view in self.group_table_views:
                view.setModel(QStandardItemModel())

    def closeEvent(self, event):
        self.db.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
