from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Редактор текста')
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu('&Файл', self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction('Открыть', self.action_clicked)
        fileMenu.addAction('Сохранить', self.action_clicked)

        # open_file = fileMenu.addMenu('&Открыть')
        # save_File = fileMenu.addMenu('&Сохранить')

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Открыть':
            fname = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(fname, 'r', encoding='utf-8')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                
                f.close()
            except FileNotFoundError:
                print('No such file')

        elif action.text() == 'Сохранить':
            fname = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(fname, 'w', encoding='utf-8')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print('No such file')


def application():
    app = QApplication(sys.argv)
    # передаём настройки компьютера, на котором запускается проект
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()

