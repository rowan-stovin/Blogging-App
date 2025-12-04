import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from blogging.controller import Controller, IllegalOperationException

class MainMenuGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Main Menu")
        self.setMinimumSize(600, 400)

        main_menu_layout = QGridLayout()

        self.create_blog_button = QPushButton("Create a blog")
        self.create_blog_button.setFixedSize(600, 50)
        self.search_blog_button = QPushButton("Search for a blog by ID")
        self.search_blog_button.setFixedSize(600, 50)
        self.retrieve_blogs_button = QPushButton("Retrieve blogs by name")
        self.retrieve_blogs_button.setFixedSize(600, 50)
        self.update_blog_button = QPushButton("Change a blog's data")
        self.update_blog_button.setFixedSize(600, 50)
        self.delete_blog_button = QPushButton("Remove a blog")
        self.delete_blog_button.setFixedSize(600, 50)
        self.list_blogs_button = QPushButton("List all blogs")
        self.list_blogs_button.setFixedSize(600, 50)
        self.edit_blog_button = QPushButton("Edit blog")
        self.edit_blog_button.setFixedSize(600, 50)
        self.log_out_button = QPushButton("Log out")
        self.log_out_button.setFixedSize(600, 50)
        
        main_menu_layout.addWidget(self.create_blog_button)
        main_menu_layout.addWidget(self.search_blog_button)
        main_menu_layout.addWidget(self.retrieve_blogs_button)
        main_menu_layout.addWidget(self.update_blog_button)
        main_menu_layout.addWidget(self.delete_blog_button)
        main_menu_layout.addWidget(self.list_blogs_button)
        main_menu_layout.addWidget(self.edit_blog_button)
        main_menu_layout.addWidget(self.log_out_button)

        widget = QWidget()
        widget.setLayout(main_menu_layout)
        self.setCentralWidget(widget)

        self.create_blog_button.clicked.connect(self.create_blog)
        self.search_blog_button.clicked.connect(self.search_blog)
        self.retrieve_blogs_button.clicked.connect(self.retrieve_blogs)
        self.update_blog_button.clicked.connect(self.update_blog)
        self.delete_blog_button.clicked.connect(self.delete_blog)
        self.list_blogs_button.clicked.connect(self.list_blogs)
        self.edit_blog_button.clicked.connect(self.edit_blog)
        self.log_out_button.clicked.connect(self.log_out)

    def create_blog(self):
        return
        #self.controller.create_blog()

    def search_blog(self):
        return
        #self.controller.search_blog()

    def retrieve_blogs(self):
        return
        #self.controller.retrieve_blogs()

    def update_blog(self):
        return
        #self.controller.update_blog()

    def delete_blog(self):
        return
        #self.controller.delete_blog()

    def list_blogs(self):
        return
        #self.controller.list_blogs()

    def edit_blog(self):
        return
        #self.controller.edit_blog()

    def log_out(self):
        return
        #self.controller.unset_current_blog()