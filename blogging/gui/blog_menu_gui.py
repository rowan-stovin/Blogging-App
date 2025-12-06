import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from blogging.gui.create_post_gui import CreatePostGUI
from blogging.gui.retrieve_posts_gui import RetrievePostsGUI
from blogging.gui.update_post_gui import UpdatePostGUI
from blogging.gui.list_posts_gui import ListPostsGUI
from blogging.gui.remove_post_gui import RemovePostGUI

from blogging.controller import Controller, IllegalOperationException

class BlogMenuGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Blog Menu")
        self.resize(600, 200)

        self.create_post_gui = CreatePostGUI(controller)
        self.retrieve_posts_gui = RetrievePostsGUI(controller)
        self.update_post_gui = UpdatePostGUI(controller)
        self.list_posts_gui = ListPostsGUI(controller)
        self.remove_post_gui = RemovePostGUI(controller)

        main_menu_layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(main_menu_layout)
        self.setCentralWidget(widget)

        # Create Post button
        self.create_post_button = QPushButton("Create a post")
        self.create_post_button.setFixedSize(600, 50)

        # Retrieve Posts button
        self.retrieve_posts_button = QPushButton("Retrieve posts")
        self.retrieve_posts_button.setFixedSize(600, 50)

        # Update Post button
        self.update_post_button = QPushButton("Update a post")
        self.update_post_button.setFixedSize(600, 50)

        # List Posts button
        self.list_posts_button = QPushButton("List posts")
        self.list_posts_button.setFixedSize(600, 50)

        # Remove Post button
        self.remove_post_button = QPushButton("Remove a post")
        self.remove_post_button.setFixedSize(600, 50)

        # Exit button
        self.exit_button = QPushButton("Exit")
        self.exit_button.setFixedSize(600, 50)

        # Add buttons to layout
        main_menu_layout.addWidget(self.create_post_button, 0, 0)
        main_menu_layout.addWidget(self.retrieve_posts_button, 1, 0)
        main_menu_layout.addWidget(self.update_post_button, 2, 0)
        main_menu_layout.addWidget(self.list_posts_button, 3, 0)
        main_menu_layout.addWidget(self.remove_post_button, 4, 0)
        main_menu_layout.addWidget(self.exit_button, 5, 0)

        # Connect buttons to their methods
        self.create_post_button.clicked.connect(self.create_post_gui.show)
        self.retrieve_posts_button.clicked.connect(self.retrieve_posts_gui.show)
        self.update_post_button.clicked.connect(self.update_post_gui.show)
        self.list_posts_button.clicked.connect(self.list_posts_gui.show)
        self.remove_post_button.clicked.connect(self.remove_post_gui.show)
        self.exit_button.clicked.connect(self.exit)

    def exit(self):
        self.close()