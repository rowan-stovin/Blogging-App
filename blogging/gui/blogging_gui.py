import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from blogging.controller import Controller
from blogging.gui.login_gui import LoginGUI
class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # set autosave to True to ensure persistence is working
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        self.controller = Controller()
        self.login_gui = LoginGUI(self.controller)

        self.setWindowTitle("BLOGGING SYSTEM")
        self.setMinimumSize(600, 400)

        main_layout = QVBoxLayout()
        self.text = QLabel("please log in")
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.text)
        main_layout.addStretch()
        
        button_layout = QHBoxLayout()
        
        self.button_log_in = QPushButton("Log in")
        self.button_log_in.setFixedSize(300, 200)
        
        self.button_Quit = QPushButton("Quit")
        self.button_Quit.setFixedSize(300, 200)
        
        button_layout.addWidget(self.button_log_in)
        button_layout.addWidget(self.button_Quit)

        main_layout.addLayout(button_layout)

        First = QWidget()
        First.setLayout(main_layout)
        self.setCentralWidget(First)

        self.button_log_in.clicked.connect(self.login_menu)

    def login_menu(self):
        self.login_gui.show()

def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
