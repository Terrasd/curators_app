import sys

from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRegExp
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
        """
        Инициализация главного окна приложения
        и установка начальных параметров.
        """
        # Создание основного окна и инициализация интерфейса
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        # Инициализация базы данных
        self.db = DBManager()

        # Скрытие строки меню по умолчанию
        self.hideMenuBar()

        # Списки с таблицами для различных семестров
        self.group_table_views = [
            self.ui.group_table_view_1,
            self.ui.group_table_view_2,
            self.ui.group_table_view_3,
            self.ui.group_table_view_4,
            self.ui.group_table_view_5
        ]

        self.group_table_views_superuser = [
            self.ui.group_table_view_1_superuser,
            self.ui.group_table_view_2_superuser,
            self.ui.group_table_view_3_superuser,
            self.ui.group_table_view_4_superuser,
            self.ui.group_table_view_5_superuser,
        ]

        # Установка страницы входа в качестве текущей
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)

        # Подключение сигналов кнопок
        self.ui.btn_enter_account.clicked.connect(self.auth_page)
        self.ui.btn_quit_profile.triggered.connect(self.confirm_logout)

        # Инициализация ID текущего куратора
        self.current_curator_id = None

        # Подключение сигналов для переключения вкладок и групп
        self.ui.group_tables_semesters.currentChanged.connect(
            self.update_students_table)
        self.ui.choice_group.currentTextChanged.connect(
            self.update_students_table)

        # Установка стиля для QTableView и строки меню
        self.set_common_table_view_style()
        self.ui.menuBar.setStyleSheet(style_QMenuBar)

        # Инициализация модели и прокси-модели
        # для списка групп суперпользователя
        self.group_list_model = QStandardItemModel()
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.group_list_model)
        self.proxy_model.setFilterKeyColumn(0)  # Фильтрация по первой колонке
        self.ui.group_list_superuser.setModel(self.proxy_model)

        # Подключение сигналов для отслеживания изменений данных в таблице
        self.ui.group_list_superuser.clicked.connect(self.on_group_selected)

        # Обновление модели при изменении текста поиска
        self.ui.find_group_by_name.textChanged.connect(self.filter_groups)

    def show(self):
        """Отображение главного окна приложения."""
        self.window.show()

    def showMenuBar(self):
        """Показать строку меню."""
        self.ui.menuBar.setVisible(True)

    def hideMenuBar(self):
        """Скрыть строку меню."""
        self.ui.menuBar.setVisible(False)

    def set_common_table_view_style(self):
        """Установка общего стиля шрифта для всех QTableView."""
        for table_view in (self.group_table_views +
                           self.group_table_views_superuser):
            table_view.setStyleSheet(font_style_for_QTableView)

    def setup_list_view_models(self):
        """
        Инициализация модели и прокси-модели
        для списка групп суперпользователя.
        """
        self.group_list_model = QStandardItemModel()
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.group_list_model)
        self.proxy_model.setFilterKeyColumn(0)  # Фильтрация по первой колонке
        self.ui.group_list_superuser.setModel(self.proxy_model)

    def auth_page(self):
        """Обработка авторизации пользователя."""
        login = self.ui.login_enter.text()
        password = self.ui.password_enter.text()

        curator = self.db.verify_curator(login, password)

        if curator:
            self.ui.text_invalid_log_or_pass.clear()
            self.current_curator_id = curator[0]

            if curator[2] == 1:
                # Суперпользователь
                self.ui.stackedWidget.setCurrentWidget(
                    self.ui.students_page_superuser)
                self.ui.find_group_by_name.clear()
                self.load_institutes_for_superuser()
                self.load_groups_for_superuser()
                self.update_students_table_for_superuser()
            else:
                # Обычный куратор
                self.ui.stackedWidget.setCurrentWidget(self.ui.students_page)
                sql_groups = self.db.get_groups_by_curator_id(
                    self.current_curator_id)
                groups_list = [row[0] for row in sql_groups]
                self.ui.choice_group.clear()
                self.ui.choice_group.addItems(groups_list)
                self.update_students_table()
        else:
            self.handle_invalid_login()

    def handle_invalid_login(self):
        """Обработка неверного логина или пароля."""
        shadow_effect, style, text = get_invalid_login_style()
        self.ui.text_invalid_log_or_pass.setText(text)
        self.ui.text_invalid_log_or_pass.setStyleSheet(style)
        self.ui.text_invalid_log_or_pass.setGraphicsEffect(shadow_effect)

    def update_students_table(self):
        """
        Обновление таблицы студентов на основе
        выбранной группы и активной вкладки.
        """
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
                    ['Фамилия', 'Имя', 'Задолженности'])

                for student in students:
                    surname_item = QStandardItem(student[0])
                    name_item = QStandardItem(student[1])
                    debts_item = QStandardItem(str(student[2]))

                    if is_archived:
                        surname_item.setFlags(
                            surname_item.flags() & ~Qt.ItemIsEditable)
                        name_item.setFlags(
                            name_item.flags() & ~Qt.ItemIsEditable)
                        debts_item.setFlags(
                            debts_item.flags() & ~Qt.ItemIsEditable)
                    else:
                        name_item.setFlags(
                            name_item.flags() & ~Qt.ItemIsEditable)
                        surname_item.setFlags(
                            surname_item.flags() & ~Qt.ItemIsEditable)

                    model.appendRow([surname_item, name_item, debts_item])

                self.group_table_views[i].setModel(model)

                # Подключение сигнала для отслеживания
                # изменений данных в таблице
                model.itemChanged.connect(
                    lambda item, archived=is_archived: self.on_item_changed(
                        item, id_group, archived))

    def load_institutes_for_superuser(self):
        """Загрузка всех институтов в comboBox для суперпользователя."""
        institutes = self.db.get_all_institutes()
        institute_names = [institute[1] for institute in institutes]
        self.ui.choice_institute_superuser.clear()
        self.ui.choice_institute_superuser.addItems(institute_names)
        self.ui.choice_institute_superuser.currentTextChanged.connect(
            self.load_groups_for_superuser)

    def load_groups_for_superuser(self):
        """
        Загрузка групп по выбранному институту в QListView
        и очистка таблицы студентов.
        """
        selected_institute = self.ui.choice_institute_superuser.currentText()
        institute_id = self.db.get_institute_by_name(selected_institute)

        if institute_id:
            institute_id = institute_id[0][0]
            groups = self.db.get_groups_by_institute(institute_id)
            group_names = [group[0] for group in groups]

            self.group_list_model.clear()
            self.group_list_model = QStandardItemModel()
            for group_name in group_names:
                item = QStandardItem(group_name)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.group_list_model.appendRow(item)

            self.proxy_model.setSourceModel(self.group_list_model)
            self.filter_groups()  # Принудительное применение фильтра

            self.clear_student_tables_for_superuser()
            for i in range(self.ui.group_tables_semesters_superuser.count()):
                (self.ui.group_tables_semesters_superuser.tabBar()
                 ).setTabTextColor(i, QColor(0, 0, 0))

    def filter_groups(self):
        """Фильтрация групп в QListView на основе текста в QLineEdit."""
        filter_text = self.ui.find_group_by_name.text()
        regex = QRegExp(filter_text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.proxy_model.setFilterRegExp(regex)

    def clear_student_tables_for_superuser(self):
        """Очистка всех таблиц студентов для суперпользователя."""
        for view in self.group_table_views_superuser:
            view.setModel(QStandardItemModel())

    def setup_list_view_signals(self):
        """Настройка сигналов для group_list_superuser."""
        self.ui.group_list_superuser.clicked.connect(self.on_group_selected)

    def on_group_selected(self, index):
        """Обработка выбора группы в QListView."""
        source_index = self.proxy_model.mapToSource(index)
        source_model = self.proxy_model.sourceModel()
        selected_group_name = source_model.itemFromIndex(source_index).text()
        self.update_students_table_for_superuser(selected_group_name)

    def update_students_table_for_superuser(self, selected_group_name=None):
        """
        Обновление таблицы для суперпользователя
        на основе выбранной группы и активной вкладки.
        """
        self.showMenuBar()

        if selected_group_name is None:
            selected_group_name = (self.ui.group_list_superuser
                                   ).currentIndex().data()
            self.change_color_tab(selected_group_name, True)

        id_group = self.db.get_group_by_name(selected_group_name)

        if selected_group_name and id_group:
            id_group = id_group[0][0]
            group_info = self.db.get_group_by_id(id_group)
            group_semester = group_info[0][3]

            self.change_color_tab(group_semester, True)

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
                    ['Фамилия', 'Имя', 'Задолженности'])

                for student in students:
                    surname_item = QStandardItem(student[0])
                    name_item = QStandardItem(student[1])
                    debts_item = QStandardItem(str(student[2]))

                    if is_archived:
                        surname_item.setFlags(
                            surname_item.flags() & ~Qt.ItemIsEditable)
                        name_item.setFlags(
                            name_item.flags() & ~Qt.ItemIsEditable)
                        debts_item.setFlags(
                            debts_item.flags() & ~Qt.ItemIsEditable)
                    else:
                        name_item.setFlags(
                            name_item.flags() & ~Qt.ItemIsEditable)
                        surname_item.setFlags(
                            surname_item.flags() & ~Qt.ItemIsEditable)

                    model.appendRow([surname_item, name_item, debts_item])

                self.group_table_views_superuser[i].setModel(model)

                model.itemChanged.connect(
                    lambda item, archived=is_archived: self.on_item_changed(
                        item, id_group, archived))

    def change_color_tab(self, semester, superuser=None):
        """Окрашивает вкладку в зависимости от текущего семестра."""
        if superuser:
            for i in range(self.ui.group_tables_semesters_superuser.count()):
                (self.ui.group_tables_semesters_superuser.tabBar()
                 ).setTabTextColor(i, QColor(0, 0, 0))
            for i in range(self.ui.group_tables_semesters_superuser.count()):
                if i + 1 == semester:
                    (self.ui.group_tables_semesters_superuser.tabBar()
                     ).setTabTextColor(i, QColor(90, 213, 62))
        else:
            for i in range(self.ui.group_tables_semesters.count()):
                (self.ui.group_tables_semesters.tabBar()
                 ).setTabTextColor(i, QColor(0, 0, 0))
            for i in range(self.ui.group_tables_semesters.count()):
                if i + 1 == semester:
                    (self.ui.group_tables_semesters.tabBar()
                     ).setTabTextColor(i, QColor(90, 213, 62))

    def on_item_changed(self, item, id_group, is_archived):
        """Обработка изменений в таблице и обновление базы данных."""
        if item.column() == 2 and not is_archived:
            row = item.row()
            student_surname = item.model().item(row, 0).text()
            student_name = item.model().item(row, 1).text()
            new_debt = item.text()
            self.db.update_student_debt(
                id_group, student_surname, student_name, new_debt)

    def confirm_logout(self):
        """Подтверждение выхода и очистка данных пользователя."""
        dialog = ConfirmationDialog(self.window)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            self.ui.login_enter.clear()
            self.ui.password_enter.clear()
            self.current_curator_id = None
            self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
            self.clear_all_tables()
            self.hideMenuBar()

    def clear_all_tables(self):
        """Очистка всех таблиц студентов."""
        for view in self.group_table_views + self.group_table_views_superuser:
            view.setModel(QStandardItemModel())

    def closeEvent(self, event):
        """Закрытие события окна: закрытие соединения с базой данных."""
        self.db.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
