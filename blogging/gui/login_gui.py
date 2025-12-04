import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from blogging.controller import Controller, IllegalOperationException

class LoginGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        layout = QGridLayout()

        username_label = QLabel("username")
        username = QLineEdit()
        password_label = QLabel("password")
        password = QLineEdit()
        
        layout.addWidget(username_label)
        layout.addWidget(username)
        
        layout.addWidget(password_label)
        layout.addWidget(password)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def login(self):
        self.controller.login()