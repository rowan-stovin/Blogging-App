import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from blogging.controller import Controller
from blogging.gui.main_menu_gui import MainMenuGUI
from blogging.exception.invalid_login_exception import InvalidLoginException
class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # set autosave to True to ensure persistence is working
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        self.controller = Controller()
        self.main_menu_gui = MainMenuGUI(self.controller)

        self.setWindowTitle("BLOGGING SYSTEM")
        self.setMinimumSize(600, 400)

        main_layout = QVBoxLayout()
        
        login_layout = QGridLayout()

        self.username_label = QLabel("username")
        self.username_text = QLineEdit()
        self.password_label = QLabel("password")
        self.password_text = QLineEdit()
        
        login_layout.addWidget(self.username_label)
        login_layout.addWidget(self.username_text)
        login_layout.addWidget(self.password_label)
        login_layout.addWidget(self.password_text)
        
        #self.text = QLabel("please log in")
        #self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #main_layout.addWidget(self.text)
        
        main_layout.addStretch()
        
        button_layout = QHBoxLayout()
        
        self.button_log_in = QPushButton("Log in")
        self.button_log_in.setFixedSize(300, 200)
        
        self.button_Quit = QPushButton("Quit")
        self.button_Quit.setFixedSize(300, 200)
        
        button_layout.addWidget(self.button_log_in)
        button_layout.addWidget(self.button_Quit)

        main_layout.addLayout(login_layout)
        main_layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.button_log_in.clicked.connect(self.login_menu)

    def login_menu(self):
        try:
            username = self.username_text.text()
            password = self.password_text.text()
            self.controller.login(username, password)
            self.main_menu_gui.show()
        except InvalidLoginException:
            QMessageBox.warning(self, "Error", "wrong username or password, please try again")
            
def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
