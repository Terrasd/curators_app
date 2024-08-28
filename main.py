import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor

from src.styles.styles import (get_invalid_login_style,
                               font_style_for_QTableView,
                               style_QMenuBar)
from interface.interface import Ui_MainWindow
from db.db_manager import DBManager
from user_widgets.confirmation_window import ConfirmationDialog


class Window:
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.db = DBManager()

        self.hideMenuBar()

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
        self.ui.btn_quit_profile.triggered.connect(self.confirm_logout)

        # Инициализация ID куратора
        self.current_curator_id = None

        # Фиксация переключения вкладок с семестрами
        self.ui.group_tables_semesters.currentChanged.connect(
            self.update_students_table)

        # Фиксация переключения группы
        self.ui.choice_group.currentTextChanged.connect(
            self.update_students_table)

        # Установка стиля для QTableView
        self.set_common_table_view_style()

        # Установка стиля для строки меню
        self.ui.menuBar.setStyleSheet(style_QMenuBar)

    def show(self):
        """Отображение окна приложения."""
        self.window.show()

    def showMenuBar(self):
        """Показать строку меню."""
        self.ui.menuBar.setVisible(True)

    def hideMenuBar(self):
        """Скрыть строку меню."""
        self.ui.menuBar.setVisible(False)

    def set_common_table_view_style(self):
        """Установка общего стиля шрифта для всех QTableView."""
        for table_view in self.group_table_views:
            table_view.setStyleSheet(font_style_for_QTableView)

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
        self.showMenuBar()

        if self.current_curator_id is None:
            return

        selected_group = self.ui.choice_group.currentText()
        id_group = self.db.get_group_by_name(selected_group)

        if selected_group and id_group:
            id_group = id_group[0][0]
            group_info = self.db.get_group_by_id(id_group)
            group_semester = group_info[0][3]

            self.change_color_tab(group_semester)

            for i in range(5):
                semester = i + 1
                if semester == group_semester:
                    students = self.db.get_students_by_semester(
                        id_group, semester, archived=False)
                    is_archived = False
                elif semester < group_semester:
                    students = self.db.get_students_by_semester(
                        id_group, semester, archived=True)
                    is_archived = True
                else:
                    students = []
                    is_archived = False

                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(
                    ['Фамилия', 'Имя', 'Задолженности']
                )

                for student in students:
                    surname_item = QStandardItem(student[0])
                    name_item = QStandardItem(student[1])
                    debts_item = QStandardItem(str(student[2]))

                    # Если группа в архиве, запрещаем изменять колонки
                    if is_archived:
                        surname_item.setFlags(
                            surname_item.flags() & ~Qt.ItemIsEditable)
                        name_item.setFlags(
                            name_item.flags() & ~Qt.ItemIsEditable)
                        debts_item.setFlags(
                            debts_item.flags() & ~Qt.ItemIsEditable)
                    else:
                        # Разрешаем редактировать только задолженности
                        name_item.setFlags(
                            name_item.flags() & ~Qt.ItemIsEditable)
                        surname_item.setFlags(
                            surname_item.flags() & ~Qt.ItemIsEditable)

                    model.appendRow([surname_item, name_item, debts_item])

                self.group_table_views[i].setModel(model)

                # Подключаем сигнал для отслеживания изменений данных в таблице
                model.itemChanged.connect(
                    lambda item, archived=is_archived:
                    self.on_item_changed(item, id_group, archived)
                )

    def change_color_tab(self, semester):
        """Окрашивает вкладку в зависимости от текущего семестра."""
        # Предварительная очистка от цветов
        for i in range(self.ui.group_tables_semesters.count()):
            self.ui.group_tables_semesters.tabBar().setTabTextColor(
                i, QColor(0, 0, 0))

        for i in range(self.ui.group_tables_semesters.count()):
            if i + 1 == semester:
                self.ui.group_tables_semesters.tabBar().setTabTextColor(
                    i, QColor(90, 213, 62))
            else:
                ...

    def on_item_changed(self, item, id_group, is_archived):
        """Обработка изменений в таблице и обновление базы данных."""
        # Обновляем только если изменена колонка "Задолженности"
        # и не архивные данные
        if item.column() == 2 and not is_archived:
            row = item.row()
            student_surname = item.model().item(row, 0).text()
            student_name = item.model().item(row, 1).text()
            new_debt = item.text()
            self.db.update_student_debt(
                id_group, student_surname, student_name, new_debt
            )

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
            self.hideMenuBar()

    def closeEvent(self, event):
        self.db.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
