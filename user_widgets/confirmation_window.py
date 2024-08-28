from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QPushButton, QLabel,
                             QHBoxLayout)

from src.styles.styles import style_QPushButton_conf_exit


class ConfirmationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Подтверждение выхода')
        self.setFixedSize(300, 150)

        main_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()

        self.label = QLabel('Вы точно хотите выйти из профиля?')
        self.label.setStyleSheet(
            'background-color: rgba(0, 0, 0, 0); font-size: 16px;')
        main_layout.addWidget(self.label)

        self.button_yes = QPushButton('Да')
        self.button_no = QPushButton('Нет')
        self.button_yes.setStyleSheet(style_QPushButton_conf_exit)
        self.button_no.setStyleSheet(style_QPushButton_conf_exit)
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.button_yes)
        buttons_layout.addWidget(self.button_no)

        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)

        # Подключение кнопок к обработчикам
        self.button_yes.clicked.connect(self.accept)
        self.button_no.clicked.connect(self.reject)
