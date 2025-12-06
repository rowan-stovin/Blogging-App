import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from blogging.controller import Controller, IllegalOperationException
from blogging.gui.create_blog_gui import CreateBlogGUI
from blogging.gui.delete_blog_gui import DeleteBlogGUI
from blogging.gui.list_blogs_gui import ListBlogsGUI
from blogging.gui.retrieve_blogs_gui import RetrieveBlogsGUI
from blogging.gui.search_blog_gui import SearchBlogGUI
from blogging.gui.update_blog_gui import UpdateBlogGUI

class MainMenuGUI(QMainWindow):
    def __init__(self, controller, login_menu):
        super().__init__()
        self.controller = controller
        self.login_menu = login_menu # Root BloggingGUI object, i.e. the login menu.
        self.setWindowTitle("Main Menu")
        self.setMinimumSize(600, 400)

        self.create_blog_gui = CreateBlogGUI(controller)
        self.search_blog_gui = SearchBlogGUI(controller)
        self.delete_blog_gui = DeleteBlogGUI(controller)
        self.list_blogs_gui = ListBlogsGUI(controller)
        self.retrieve_blogs_gui = RetrieveBlogsGUI(controller)
        self.update_blog_gui = UpdateBlogGUI(controller)

        main_menu_layout = QGridLayout()

        self.create_blog_button = QPushButton("Create a blog")
        self.create_blog_button.setFixedSize(200, 100)
        self.search_blog_button = QPushButton(f"Search for a blog by ID\nand set the current blog")
        self.search_blog_button.setFixedSize(200, 100)
        self.retrieve_blogs_button = QPushButton("Retrieve blogs by name")
        self.retrieve_blogs_button.setFixedSize(200, 100)
        self.update_blog_button = QPushButton("Change a blog's data")
        self.update_blog_button.setFixedSize(200, 100)
        self.delete_blog_button = QPushButton("Remove a blog")
        self.delete_blog_button.setFixedSize(200, 100)
        self.list_blogs_button = QPushButton("List all blogs")
        self.list_blogs_button.setFixedSize(200, 100)
        self.edit_blog_button = QPushButton("Edit blog")
        self.edit_blog_button.setFixedSize(300, 100)
        self.log_out_button = QPushButton("Log out")
        self.log_out_button.setFixedSize(300, 100)
        
        main_menu_layout.addWidget(self.create_blog_button, 0, 0)
        main_menu_layout.addWidget(self.search_blog_button, 0, 1)
        main_menu_layout.addWidget(self.retrieve_blogs_button, 0, 2)
        main_menu_layout.addWidget(self.update_blog_button, 1, 0)
        main_menu_layout.addWidget(self.delete_blog_button, 1, 1)
        main_menu_layout.addWidget(self.list_blogs_button, 1, 2)
       
        bot_buttons = QHBoxLayout()
        bot_buttons.addWidget(self.edit_blog_button)
        bot_buttons.addWidget(self.log_out_button)

        button_widget = QWidget()
        button_widget.setLayout(bot_buttons)
        main_menu_layout.addWidget(button_widget, 2, 0, 1, 3)
        main_menu_layout.setAlignment(button_widget, Qt.AlignmentFlag.AlignTop)

        widget = QWidget()
        widget.setLayout(main_menu_layout)
        self.setCentralWidget(widget)

        self.create_blog_button.clicked.connect(self.create_blog)
        self.search_blog_button.clicked.connect(self.search_blog)
        self.retrieve_blogs_button.clicked.connect(self.retrieve_blogs)
        self.update_blog_button.clicked.connect(self.update_blog)
        self.delete_blog_button.clicked.connect(self.delete_blog)
        self.list_blogs_button.clicked.connect(self.list_blogs)
        self.log_out_button.clicked.connect(self.log_out)

    def create_blog(self):
        self.create_blog_gui.show()

    def search_blog(self):
        self.search_blog_gui.show()

    def retrieve_blogs(self):
        self.retrieve_blogs_gui.show()

    def update_blog(self):
        self.update_blog_gui.show()

    def delete_blog(self):
        self.delete_blog_gui.show()

    def list_blogs(self):
        self.list_blogs_gui.show()

    def log_out(self):
        self.login_menu.show()
        self.controller.logged = False
        self.close()