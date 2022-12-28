from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Простая программа')
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('Это базовая надпись')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText('Нажми на меня')
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)


    def add_label(self):
        self.new_text.setText('Вторая надпись')
        self.new_text.move(100, 50)
        self.new_text.adjustSize()



def applecation():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


''' Создание окна функцией
def applecation():
    # Создание окна функцией с настройкам внутри
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('Простая программа')
    window.setGeometry(300, 250, 350, 200)

    main_text = QtWidgets.QLabel(window)
    main_text.setText('Это базовая надпись')
    main_text.move(100, 100)
    main_text.adjustSize()

    btn = QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText('Нажми на меня')
    btn.setFixedWidth(200)
    btn.clicked.connect(add_label)

    window.show()
    sys.exit(app.exec())
'''


if __name__ == '__main__':
    applecation()
