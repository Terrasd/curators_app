# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1187, 807)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(35, 123, 230, 255), stop:0.636364 rgba(160, 176, 186, 255), stop:1 rgba(172, 198, 230, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stackedWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.login_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.LoginPassWidget = QtWidgets.QWidget(self.login_page)
        self.LoginPassWidget.setMaximumSize(QtCore.QSize(500, 500))
        self.LoginPassWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.LoginPassWidget.setObjectName("LoginPassWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LoginPassWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login = QtWidgets.QVBoxLayout()
        self.login.setContentsMargins(105, -1, 105, -1)
        self.login.setObjectName("login")
        self.login_enter = QtWidgets.QLineEdit(self.LoginPassWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_enter.sizePolicy().hasHeightForWidth())
        self.login_enter.setSizePolicy(sizePolicy)
        self.login_enter.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_enter.setFont(font)
        self.login_enter.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.login_enter.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login_enter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.login_enter.setPlaceholderText("")
        self.login_enter.setObjectName("login_enter")
        self.login.addWidget(self.login_enter)
        self.login_label = QtWidgets.QLabel(self.LoginPassWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_label.sizePolicy().hasHeightForWidth())
        self.login_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.login_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.login_label.setObjectName("login_label")
        self.login.addWidget(self.login_label)
        self.verticalLayout.addLayout(self.login)
        self.password = QtWidgets.QVBoxLayout()
        self.password.setContentsMargins(105, -1, 105, -1)
        self.password.setObjectName("password")
        self.password_enter = QtWidgets.QLineEdit(self.LoginPassWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_enter.sizePolicy().hasHeightForWidth())
        self.password_enter.setSizePolicy(sizePolicy)
        self.password_enter.setMinimumSize(QtCore.QSize(0, 25))
        self.password_enter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_enter.setFont(font)
        self.password_enter.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.password_enter.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_enter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_enter.setObjectName("password_enter")
        self.password.addWidget(self.password_enter)
        self.password_label = QtWidgets.QLabel(self.LoginPassWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.password_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.password_label.setObjectName("password_label")
        self.password.addWidget(self.password_label)
        self.verticalLayout.addLayout(self.password)
        self.text_invalid_log_or_pass = QtWidgets.QLabel(self.LoginPassWidget)
        self.text_invalid_log_or_pass.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_invalid_log_or_pass.setFont(font)
        self.text_invalid_log_or_pass.setText("")
        self.text_invalid_log_or_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.text_invalid_log_or_pass.setObjectName("text_invalid_log_or_pass")
        self.verticalLayout.addWidget(self.text_invalid_log_or_pass)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(80, -1, 80, -1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_enter_account = QtWidgets.QPushButton(self.LoginPassWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_enter_account.sizePolicy().hasHeightForWidth())
        self.btn_enter_account.setSizePolicy(sizePolicy)
        self.btn_enter_account.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_enter_account.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_enter_account.setStyleSheet("#btn_enter_account {\n"
"    background-color: rgb(207, 207, 207);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    border-radius: 10px;\n"
"    font-size: 12px;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"#btn_enter_account:hover {\n"
"    background-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"#btn_enter_account:pressed {\n"
"    background-color: rgb(167, 167, 167);\n"
"}")
        self.btn_enter_account.setAutoDefault(True)
        self.btn_enter_account.setDefault(True)
        self.btn_enter_account.setFlat(False)
        self.btn_enter_account.setObjectName("btn_enter_account")
        self.verticalLayout_2.addWidget(self.btn_enter_account)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(70, 0, 70, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.emblem = QtWidgets.QLabel(self.LoginPassWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emblem.sizePolicy().hasHeightForWidth())
        self.emblem.setSizePolicy(sizePolicy)
        self.emblem.setMinimumSize(QtCore.QSize(0, 0))
        self.emblem.setMaximumSize(QtCore.QSize(400, 190))
        self.emblem.setText("")
        self.emblem.setPixmap(QtGui.QPixmap(":/emb/emblem-removebg.png"))
        self.emblem.setScaledContents(True)
        self.emblem.setAlignment(QtCore.Qt.AlignCenter)
        self.emblem.setObjectName("emblem")
        self.verticalLayout_6.addWidget(self.emblem)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.gridLayout_2.addWidget(self.LoginPassWidget, 1, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.login_page)
        self.students_page = QtWidgets.QWidget()
        self.students_page.setObjectName("students_page")
        self.gridLayout = QtWidgets.QGridLayout(self.students_page)
        self.gridLayout.setObjectName("gridLayout")
        self.inform_group_layout = QtWidgets.QGroupBox(self.students_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inform_group_layout.sizePolicy().hasHeightForWidth())
        self.inform_group_layout.setSizePolicy(sizePolicy)
        self.inform_group_layout.setMinimumSize(QtCore.QSize(260, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inform_group_layout.setFont(font)
        self.inform_group_layout.setStyleSheet("")
        self.inform_group_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.inform_group_layout.setObjectName("inform_group_layout")
        self.gridLayout.addWidget(self.inform_group_layout, 2, 1, 1, 1)
        self.group_tables_semesters = QtWidgets.QTabWidget(self.students_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.group_tables_semesters.setFont(font)
        self.group_tables_semesters.setFocusPolicy(QtCore.Qt.NoFocus)
        self.group_tables_semesters.setObjectName("group_tables_semesters")
        self.semester_1 = QtWidgets.QWidget()
        self.semester_1.setObjectName("semester_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.semester_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.group_table_view_1 = QtWidgets.QTableView(self.semester_1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_1.setFont(font)
        self.group_table_view_1.setObjectName("group_table_view_1")
        self.gridLayout_3.addWidget(self.group_table_view_1, 0, 0, 1, 1)
        self.group_tables_semesters.addTab(self.semester_1, "")
        self.semester_2 = QtWidgets.QWidget()
        self.semester_2.setObjectName("semester_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.semester_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.group_table_view_2 = QtWidgets.QTableView(self.semester_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_2.setFont(font)
        self.group_table_view_2.setObjectName("group_table_view_2")
        self.gridLayout_4.addWidget(self.group_table_view_2, 0, 0, 1, 1)
        self.group_tables_semesters.addTab(self.semester_2, "")
        self.semester_3 = QtWidgets.QWidget()
        self.semester_3.setObjectName("semester_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.semester_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.group_table_view_3 = QtWidgets.QTableView(self.semester_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_3.setFont(font)
        self.group_table_view_3.setObjectName("group_table_view_3")
        self.gridLayout_5.addWidget(self.group_table_view_3, 0, 0, 1, 1)
        self.group_tables_semesters.addTab(self.semester_3, "")
        self.semester_4 = QtWidgets.QWidget()
        self.semester_4.setObjectName("semester_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.semester_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.group_table_view_4 = QtWidgets.QTableView(self.semester_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_4.setFont(font)
        self.group_table_view_4.setObjectName("group_table_view_4")
        self.gridLayout_6.addWidget(self.group_table_view_4, 0, 0, 1, 1)
        self.group_tables_semesters.addTab(self.semester_4, "")
        self.semester_5 = QtWidgets.QWidget()
        self.semester_5.setObjectName("semester_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.semester_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.group_table_view_5 = QtWidgets.QTableView(self.semester_5)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_5.setFont(font)
        self.group_table_view_5.setObjectName("group_table_view_5")
        self.gridLayout_7.addWidget(self.group_table_view_5, 0, 0, 1, 1)
        self.group_tables_semesters.addTab(self.semester_5, "")
        self.gridLayout.addWidget(self.group_tables_semesters, 2, 0, 1, 1)
        self.choice_group = QtWidgets.QComboBox(self.students_page)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.choice_group.setFont(font)
        self.choice_group.setFocusPolicy(QtCore.Qt.NoFocus)
        self.choice_group.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.choice_group.setEditable(False)
        self.choice_group.setCurrentText("")
        self.choice_group.setObjectName("choice_group")
        self.gridLayout.addWidget(self.choice_group, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.students_page)
        self.students_page_superuser = QtWidgets.QWidget()
        self.students_page_superuser.setObjectName("students_page_superuser")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.students_page_superuser)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.inform_group_layout_superuser = QtWidgets.QGroupBox(self.students_page_superuser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inform_group_layout_superuser.sizePolicy().hasHeightForWidth())
        self.inform_group_layout_superuser.setSizePolicy(sizePolicy)
        self.inform_group_layout_superuser.setMinimumSize(QtCore.QSize(260, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inform_group_layout_superuser.setFont(font)
        self.inform_group_layout_superuser.setAlignment(QtCore.Qt.AlignCenter)
        self.inform_group_layout_superuser.setObjectName("inform_group_layout_superuser")
        self.gridLayout_13.addWidget(self.inform_group_layout_superuser, 2, 1, 1, 1)
        self.group_tables_semesters_superuser = QtWidgets.QTabWidget(self.students_page_superuser)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.group_tables_semesters_superuser.setFont(font)
        self.group_tables_semesters_superuser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.group_tables_semesters_superuser.setObjectName("group_tables_semesters_superuser")
        self.semester_1_superuser = QtWidgets.QWidget()
        self.semester_1_superuser.setObjectName("semester_1_superuser")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.semester_1_superuser)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.group_table_view_1_superuser = QtWidgets.QTableView(self.semester_1_superuser)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_1_superuser.setFont(font)
        self.group_table_view_1_superuser.setObjectName("group_table_view_1_superuser")
        self.gridLayout_8.addWidget(self.group_table_view_1_superuser, 0, 0, 1, 1)
        self.group_tables_semesters_superuser.addTab(self.semester_1_superuser, "")
        self.semester_2_superuser = QtWidgets.QWidget()
        self.semester_2_superuser.setObjectName("semester_2_superuser")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.semester_2_superuser)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.group_table_view_2_superuser = QtWidgets.QTableView(self.semester_2_superuser)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_2_superuser.setFont(font)
        self.group_table_view_2_superuser.setObjectName("group_table_view_2_superuser")
        self.gridLayout_9.addWidget(self.group_table_view_2_superuser, 0, 0, 1, 1)
        self.group_tables_semesters_superuser.addTab(self.semester_2_superuser, "")
        self.semester_3_superuser = QtWidgets.QWidget()
        self.semester_3_superuser.setObjectName("semester_3_superuser")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.semester_3_superuser)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.group_table_view_3_superuser = QtWidgets.QTableView(self.semester_3_superuser)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_3_superuser.setFont(font)
        self.group_table_view_3_superuser.setObjectName("group_table_view_3_superuser")
        self.gridLayout_10.addWidget(self.group_table_view_3_superuser, 0, 0, 1, 1)
        self.group_tables_semesters_superuser.addTab(self.semester_3_superuser, "")
        self.semester_4_superuser = QtWidgets.QWidget()
        self.semester_4_superuser.setObjectName("semester_4_superuser")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.semester_4_superuser)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.group_table_view_4_superuser = QtWidgets.QTableView(self.semester_4_superuser)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_4_superuser.setFont(font)
        self.group_table_view_4_superuser.setObjectName("group_table_view_4_superuser")
        self.gridLayout_11.addWidget(self.group_table_view_4_superuser, 0, 0, 1, 1)
        self.group_tables_semesters_superuser.addTab(self.semester_4_superuser, "")
        self.semester_5_superuser = QtWidgets.QWidget()
        self.semester_5_superuser.setObjectName("semester_5_superuser")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.semester_5_superuser)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.group_table_view_5_superuser = QtWidgets.QTableView(self.semester_5_superuser)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.group_table_view_5_superuser.setFont(font)
        self.group_table_view_5_superuser.setObjectName("group_table_view_5_superuser")
        self.gridLayout_12.addWidget(self.group_table_view_5_superuser, 0, 0, 1, 1)
        self.group_tables_semesters_superuser.addTab(self.semester_5_superuser, "")
        self.gridLayout_13.addWidget(self.group_tables_semesters_superuser, 2, 0, 1, 1)
        self.choice_institute_superuser = QtWidgets.QComboBox(self.students_page_superuser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_institute_superuser.sizePolicy().hasHeightForWidth())
        self.choice_institute_superuser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.choice_institute_superuser.setFont(font)
        self.choice_institute_superuser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.choice_institute_superuser.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.choice_institute_superuser.setObjectName("choice_institute_superuser")
        self.gridLayout_13.addWidget(self.choice_institute_superuser, 1, 0, 1, 1)
        self.group_list_superuser = QtWidgets.QListView(self.students_page_superuser)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.group_list_superuser.setFont(font)
        self.group_list_superuser.setStyleSheet("QListView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 15px 15px;\n"
"}")
        self.group_list_superuser.setObjectName("group_list_superuser")
        self.gridLayout_13.addWidget(self.group_list_superuser, 1, 1, 1, 1)
        self.find_group_by_name = QtWidgets.QLineEdit(self.students_page_superuser)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.find_group_by_name.setFont(font)
        self.find_group_by_name.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.find_group_by_name.setObjectName("find_group_by_name")
        self.gridLayout_13.addWidget(self.find_group_by_name, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.students_page_superuser)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1187, 21))
        self.menuBar.setObjectName("menuBar")
        self.profile = QtWidgets.QMenu(self.menuBar)
        self.profile.setObjectName("profile")
        MainWindow.setMenuBar(self.menuBar)
        self.btn_quit_profile = QtWidgets.QAction(MainWindow)
        self.btn_quit_profile.setObjectName("btn_quit_profile")
        self.profile.addAction(self.btn_quit_profile)
        self.menuBar.addAction(self.profile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.group_tables_semesters.setCurrentIndex(0)
        self.group_tables_semesters_superuser.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ЯКуратор"))
        self.login_label.setText(_translate("MainWindow", "Логин"))
        self.password_label.setText(_translate("MainWindow", "Пароль"))
        self.btn_enter_account.setText(_translate("MainWindow", "ВОЙТИ"))
        self.inform_group_layout.setTitle(_translate("MainWindow", "Информация о группе"))
        self.group_tables_semesters.setTabText(self.group_tables_semesters.indexOf(self.semester_1), _translate("MainWindow", "Семестр 1"))
        self.group_tables_semesters.setTabText(self.group_tables_semesters.indexOf(self.semester_2), _translate("MainWindow", "Семестр 2"))
        self.group_tables_semesters.setTabText(self.group_tables_semesters.indexOf(self.semester_3), _translate("MainWindow", "Семестр 3"))
        self.group_tables_semesters.setTabText(self.group_tables_semesters.indexOf(self.semester_4), _translate("MainWindow", "Семестр 4"))
        self.group_tables_semesters.setTabText(self.group_tables_semesters.indexOf(self.semester_5), _translate("MainWindow", "Семестр 5"))
        self.inform_group_layout_superuser.setTitle(_translate("MainWindow", "Информация о группе"))
        self.group_tables_semesters_superuser.setTabText(self.group_tables_semesters_superuser.indexOf(self.semester_1_superuser), _translate("MainWindow", "Семестр 1"))
        self.group_tables_semesters_superuser.setTabText(self.group_tables_semesters_superuser.indexOf(self.semester_2_superuser), _translate("MainWindow", "Семестр 2"))
        self.group_tables_semesters_superuser.setTabText(self.group_tables_semesters_superuser.indexOf(self.semester_3_superuser), _translate("MainWindow", "Семестр 3"))
        self.group_tables_semesters_superuser.setTabText(self.group_tables_semesters_superuser.indexOf(self.semester_4_superuser), _translate("MainWindow", "Семестр 4"))
        self.group_tables_semesters_superuser.setTabText(self.group_tables_semesters_superuser.indexOf(self.semester_5_superuser), _translate("MainWindow", "Семестр 5"))
        self.find_group_by_name.setPlaceholderText(_translate("MainWindow", "Введите группу для поиска..."))
        self.profile.setTitle(_translate("MainWindow", "Профиль"))
        self.btn_quit_profile.setText(_translate("MainWindow", "Выйти из профиля"))
from . import res_rc
