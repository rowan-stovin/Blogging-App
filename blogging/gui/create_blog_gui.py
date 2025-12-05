import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from blogging.controller import Controller, IllegalOperationException

class CreateBlogGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Create a Blog")
        self.resize(600, 200)

        info_layout = QGridLayout()

        blog_id_label = QLabel("Enter the Blog's ID")
        blog_id_text = QLineEdit()
        blog_name_label = QLabel("Enter the Blog's name")
        blog_name_text = QLineEdit()
        blog_url_label = QLabel("Enter the Blog's URL")
        blog_url_text = QLineEdit()
        blog_email_label = QLabel("Enter the Blog's Email")
        blog_email_text = QLineEdit()

        info_layout.addWidget(blog_id_label, 0, 0)
        info_layout.addWidget(blog_id_text, 0, 1)
        info_layout.addWidget(blog_name_label, 1, 0)
        info_layout.addWidget(blog_name_text, 1, 1)
        info_layout.addWidget(blog_url_label, 2, 0)
        info_layout.addWidget(blog_url_text, 2, 1)
        info_layout.addWidget(blog_email_label, 3, 0)
        info_layout.addWidget(blog_email_text, 3, 1)

        button_layout = QHBoxLayout()

        create_button = QPushButton("Create")
        create_button.setFixedSize(300, 100)
        exit_button = QPushButton("Exit")
        exit_button.setFixedSize(300, 100)

        button_layout.addWidget(create_button)
        button_layout.addWidget(exit_button)
        
        layout = QVBoxLayout()
        
        top_widget = QWidget()
        top_widget.setLayout(info_layout) 
        bottom_widget = QWidget()
        bottom_widget.setLayout(button_layout)
        layout.addWidget(top_widget)
        layout.addWidget(bottom_widget)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
