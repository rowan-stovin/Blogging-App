import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from blogging.controller import Controller, IllegalOperationException
from blogging.gui.blog_menu_gui import BlogMenuGUI

class SearchBlogGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Search for a Blog")
        self.resize(600, 300)

        self.blog_menu_gui = BlogMenuGUI(controller)
        
        # Search input layout
        search_layout = QHBoxLayout()
        blog_id_label_search = QLabel("Enter the Blog's ID")
        self.blog_id_text_search = QLineEdit()
        search_layout.addWidget(blog_id_label_search)
        search_layout.addWidget(self.blog_id_text_search)
        
        # Search/Exit buttons
        button_layout = QHBoxLayout()
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search)
        search_button.setMinimumSize(100, 50)
        button_layout.addWidget(search_button)
        
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit)
        exit_button.setMinimumSize(100, 50)
        button_layout.addWidget(exit_button)
        
        # Blog info display
        info_layout = QGridLayout()
        blog_id_label = QLabel("Blog's ID:")
        self.blog_id_text = QLabel("")
        blog_name_label = QLabel("Blog's name:")
        self.blog_name_text = QLabel("")
        blog_url_label = QLabel("Blog's URL:")
        self.blog_url_text = QLabel("")
        blog_email_label = QLabel("Blog's Email:")
        self.blog_email_text = QLabel("")
        
        info_layout.addWidget(blog_id_label, 0, 0)
        info_layout.addWidget(self.blog_id_text, 0, 1)
        info_layout.addWidget(blog_name_label, 1, 0)
        info_layout.addWidget(self.blog_name_text, 1, 1)
        info_layout.addWidget(blog_url_label, 2, 0)
        info_layout.addWidget(self.blog_url_text, 2, 1)
        info_layout.addWidget(blog_email_label, 3, 0)
        info_layout.addWidget(self.blog_email_text, 3, 1)
        
        # Set Current Blog button (initially disabled)
        self.set_current_blog_button = QPushButton("Set Current Blog")
        self.set_current_blog_button.clicked.connect(self.set_current_blog)
        self.set_current_blog_button.setMinimumSize(100, 50)
        self.set_current_blog_button.setEnabled(False)

        # Blog menu button (initially disabled)
        self.blog_menu_button = QPushButton("Edit Blog")
        self.blog_menu_button.clicked.connect(self.blog_menu)
        self.blog_menu_button.setMinimumSize(100, 50)
        self.blog_menu_button.setEnabled(False)

        bottom_button_layout = QHBoxLayout()
        bottom_button_layout.addWidget(self.set_current_blog_button)
        bottom_button_layout.addWidget(self.blog_menu_button)
        
        # Main layout - Fixed: removed duplicate info_layout
        layout = QVBoxLayout()
        layout.addLayout(search_layout)
        layout.addLayout(button_layout)
        layout.addLayout(info_layout)  # Only added once now
        layout.addLayout(bottom_button_layout)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def search(self):
        """ Searches for the blog with the given id"""
        try:
            key = int(self.blog_id_text_search.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Not a valid ID.")
            return
        
        self.display_blog = self.controller.blog_dao_json.search_blog(key)
        if self.display_blog:
            self.fill()
            self.set_current_blog_button.setEnabled(True)  # Enable button when blog found
            self.blog_menu_button.setEnabled(False)  # Disable blog menu until current blog is set
        else:
            QMessageBox.warning(self, "Error", "No blogs exist with the given ID.")
            self.set_current_blog_button.setEnabled(False)  # Disable if no blog found
            self.blog_menu_button.setEnabled(False)
            return
    
    def exit(self):
        """ Clears the fields and closes the window"""
        self.unfill()
        self.close()
    
    def fill(self):
        """ Fills the fields"""
        self.blog_id_text.setText(str(self.display_blog.id))
        self.blog_email_text.setText(self.display_blog.email)
        self.blog_name_text.setText(self.display_blog.name)
        self.blog_url_text.setText(self.display_blog.url)

    def unfill(self):
        """ Clears the fields"""
        self.blog_id_text_search.setText("")
        self.blog_id_text.setText("")
        self.blog_email_text.setText("")
        self.blog_name_text.setText("")
        self.blog_url_text.setText("")
    
    def set_current_blog(self):
        """ Sets current blog"""
        self.controller.current_blog = self.display_blog
        self.blog_menu_button.setEnabled(True)
        QMessageBox.information(self, "Success", f"Current blog set to: {self.display_blog.name}")

    def blog_menu(self):
        """ Opens the blog menu"""
        self.blog_menu_gui.show()