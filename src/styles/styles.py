from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor


def get_invalid_login_style():
    """Возвращает текст ошибки логина или пароля вместе со стилем."""
    shadow_effect = QGraphicsDropShadowEffect()
    shadow_effect.setBlurRadius(3)
    shadow_effect.setOffset(1, 1)
    shadow_effect.setColor(QColor(0, 0, 0, 190))
    return (shadow_effect, 'color: rgb(255, 50, 50); font-weight: bold;',
            'Неверный логин или пароль!')


style_QPushButton = '''
    QPushButton {
        background-color: rgb(207, 207, 207);
        color: rgb(0, 0, 0);
        border: 1px solid rgb(100, 100, 100);
        border-radius: 10px;
        font-size: 12px;
        padding: 10px 20px;
    }

    QPushButton:hover {
        background-color: rgb(180, 180, 180);
    }

    QPushButton:pressed {
        background-color: rgb(167, 167, 167);
    }
'''

style_QPushButton_conf_exit = '''
    QPushButton {
        background-color: rgb(207, 207, 207);
        color: rgb(0, 0, 0);
        border: 1px solid rgb(100, 100, 100);
        border-radius: 10px;
        font-size: 12px;
        padding: 7px 20px;
    }

    QPushButton:hover {
        background-color: rgb(180, 180, 180);
    }

    QPushButton:pressed {
        background-color: rgb(167, 167, 167);
    }
'''

font_style_for_QTableView = '''
    QTableView {
        font-family: MS Shell Dlg 2;
        font-size: 10pt;
    }
'''

style_QMenuBar = '''
    QMenuBar {
        background-color: rgb(207, 207, 207);
        border-bottom: 1px solid rgb(100, 100, 100);
    }

    QMenu {
        background-color: rgb(207, 207, 207);
    }

    QMenu::item {
        background-color: rgb(207, 207, 207);
    }

    QMenu::item:selected {
        background-color: rgb(180, 180, 180);
        color: black;
    }
'''
