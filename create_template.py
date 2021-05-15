import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from CreateTemplateWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Коннектим кнопку
        self.btnSave.clicked.connect(self.btn_save_clicked)

    def btn_save_clicked(self):
        with open(r'Templates/' + self.editName.text() + ".yaml", 'w') as template_file:
            template_file.write(f'name: "{self.editName.text()}"\n'
                                f'description: "{self.editDescription.text()}"\n'
                                f'commands: "{self.editCommands.text()}"\n'
                                f'author: "{self.editAuthor.text()}"\n'
                                f'create_datetime: "{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}"')
            template_file.close()


if __name__ == "__main__":
    import sys

    # Ініцілізуємо та запустимо головне вікно
    app = QtWidgets.QApplication(sys.argv)
    appMainWindow = MainWindow()
    appMainWindow.show()
    sys.exit(app.exec_())
