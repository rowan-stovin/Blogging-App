import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from blogging.controller import Controller, IllegalOperationException
from blogging.blog import Blog
from blogging.post import Post

class CreatePostGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Create a Post")
        self.resize(600, 200)

        info_layout = QGridLayout()

        post_title_label = QLabel("Enter the Post's title")
        self.post_title_text = QLineEdit()
        post_text_label = QLabel("Enter the Post's text")
        self.post_text_text = QLineEdit()


        info_layout.addWidget(post_title_label, 0, 0)
        info_layout.addWidget(self.post_title_text, 0, 1)
        info_layout.addWidget(post_text_label, 1, 0)
        info_layout.addWidget(self.post_text_text, 1, 1)

        button_layout = QHBoxLayout()

        create_button = QPushButton("Create")
        create_button.setFixedSize(300, 100)
        create_button.clicked.connect(self.create)
        exit_button = QPushButton("Exit")
        exit_button.setFixedSize(300, 100)
        exit_button.clicked.connect(self.exit)

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

    def exit(self):
        self.close()

    def create(self):
        title = self.post_title_text.text()
        text = self.post_text_text.text()

        self.controller.current_blog.create_post(title, text)
        QMessageBox.information(self, "Success", f"The post was created")
        self.close()