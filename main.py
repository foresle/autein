from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
import time
import os
import yaml


# Клас шаблона
class Template:
    def __init__(self, name, description, commands, author, create_datetime):
        self.create_datetime = create_datetime
        self.author = author
        self.commands = commands
        self.description = description
        self.name = name


def run_command(command):
    os.system("cd ~/; clear")
    os.system(command)
    os.system("clear")


# Клас головного вікно
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, templates):
        super().__init__()
        self.setupUi(self)

        self.installing = False

        # Спарсені шаблони
        self.templates = templates

        # Текст для About
        self.about_message_box = QtWidgets.QMessageBox(text="Author: logic-debugger\nIf you have any "
                                                            "questions about copyright, please contact "
                                                            "the "
                                                            "e-mail address: "
                                                            "logic-debugger@protonmail.com")

        # Конектим кнопки
        self.btnAbout.clicked.connect(self.btn_about_clicked)
        self.btnInstall.clicked.connect(self.btn_install_clicked)
        self.btnCancel.clicked.connect(self.btn_cancel_clicked)

        # Створюємо Label бля StatusBar
        self.statusbar.addWidget(QtWidgets.QLabel(''))

        # Заповнюємо Layout шаблонами
        for template in self.templates:
            h_box = QtWidgets.QHBoxLayout()  # Створюємо Layout
            h_box.addWidget(QtWidgets.QCheckBox())  # CheckBox
            h_box.addWidget(QtWidgets.QLabel(template.name))  # Назва

            description_label = QtWidgets.QLabel(template.description)  # Опис
            description_label.setWordWrap(True)
            description_label.setToolTip(f'Author: {template.author}\n'
                                         f'Create date: {template.create_datetime}')
            h_box.addWidget(description_label)

            self.templatesLayout.addLayout(h_box)  # Додаємо Layout в вікно

    def btn_about_clicked(self):
        self.about_message_box.setWindowTitle("About")
        self.about_message_box.show()

    def btn_cancel_clicked(self):
        self.btnCancel.setEnabled(False)  # Вимикаємо кнопку скасування
        self.btnInstall.setEnabled(True)  # Вмикаємо кнопку встановлення
        self.installing = False

    def btn_install_clicked(self):
        self.btnCancel.setEnabled(True)  # Вмикаємо кнопку скасування
        self.btnInstall.setEnabled(False)  # Вимикаємо кнопку встановлення
        self.installing = True

        commands = []  # Масив в який ми положимо команди для подальшого виконання
        for i in range(len(self.templates)):
            if self.templatesLayout.itemAt(i).layout().itemAt(0).widget().isChecked():  # Якщо CheckBox активований то
                commands.append(self.templates[i].commands)  # ложимо команду в масив

        # Виконуємо команди
        template_index = 0
        for command in commands:
            if self.installing:
                self.statusbar.children()[2].setText(f'Installing {templates[template_index].name}...')
                run_command(command)
                self.statusbar.children()[2].setText(f'{templates[template_index].name} has installed')
                time.sleep(1)
                self.statusbar.children()[2].setText(f'')
                template_index += 1
            else:
                self.btnCancel.setEnabled(False)  # Вимикаємо кнопку скасування
                self.btnInstall.setEnabled(True)  # Вмикаємо кнопку встановлення
                self.statusbar.children()[2].setText(f'')

        self.btn_cancel_clicked()


def load_templates(templates):
    current_directory = os.path.abspath(os.curdir)  # Директорія запуску
    ways_templates = []

    # Шукаємо шаблони
    for template in os.listdir(current_directory + r'/Templates/'):
        if template[-5:] == ".yaml":
            ways_templates.append(current_directory + r'/Templates/' + template)

    # Парсим шаблони
    for template in ways_templates:
        with open(template) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            templates.append(Template(data["name"], data["description"], data["commands"], data["author"],
                                      data["create_datetime"]))


if __name__ == "__main__":
    import sys

    # Завантажуєемо шаблоти та ложимо в масив
    templates = []
    load_templates(templates)

    # Ініцілізуємо та запустимо головне вікно, також передаємо йому масив з шаблонами
    app = QtWidgets.QApplication(sys.argv)
    appMainWindow = MainWindow(templates)
    appMainWindow.show()
    sys.exit(app.exec_())
