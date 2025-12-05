import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from blogging.controller import Controller, IllegalOperationException

class SearchBlogGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Search for a Blog")
        self.resize(600, 200)