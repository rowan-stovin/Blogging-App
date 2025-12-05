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

        search_layout = QHBoxLayout()
        
        info_layout = QGridLayout()

        #blog_label = QLabel("Blog")
        blog_id_label = QLabel("Blog's ID:")
        self.blog_id_text = QLabel("")
        blog_name_label = QLabel("Blog's name:")
        self.blog_name_text = QLabel("")
        blog_url_label = QLabel("Blog's URL:")
        self.blog_url_text = QLabel("")
        blog_email_label = QLabel("Blog's Email:")
        self.blog_email_text = QLabel("")

        #info_layout.addWidget(blog_label)
        info_layout.addWidget(blog_id_label, 0, 0)
        info_layout.addWidget(self.blog_id_text, 0, 1)
        info_layout.addWidget(blog_name_label, 1, 0)
        info_layout.addWidget(self.blog_name_text, 1, 1)
        info_layout.addWidget(blog_url_label, 2, 0)
        info_layout.addWidget(self.blog_url_text, 2, 1)
        info_layout.addWidget(blog_email_label, 3, 0)
        info_layout.addWidget(self.blog_email_text, 3, 1)

        button_layout = QHBoxLayout()

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit)
        button_layout.addWidget(search_button)
        button_layout.addWidget(exit_button)
        
        search_layout = QHBoxLayout()
        
        blog_id_label_search = QLabel("Enter the Blog's ID")
        self.blog_id_text_search = QLineEdit()
        search_layout.addWidget(blog_id_label_search)
        search_layout.addWidget(self.blog_id_text_search)

        layout = QVBoxLayout()
        
        top_widget = QWidget()
        top_widget.setLayout(search_layout) 
        middle_widget = QWidget()
        middle_widget.setLayout(button_layout)
        bottom_widget = QWidget()
        bottom_widget.setLayout(info_layout)
        
        layout.addWidget(top_widget)
        layout.addWidget(middle_widget)
        layout.addWidget(bottom_widget)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def search(self):
        try:
            key = int(self.blog_id_text_search.text())
        except:
            QMessageBox.warning(self, "Error", "Not a valid id")
            return
        
        blog = self.controller.blog_dao_json.search_blog(key)
        if blog is not None:
            self.fill(blog)
        else:
            QMessageBox.warning(self, "Error", "No blogs exist with the given id")
            return

    def exit(self):
        self.close()

    def fill(self, blog):
        self.blog_id_text.setText(str(blog.id))
        self.blog_email_text.setText(blog.email)
        self.blog_name_text.setText(blog.name)
        self.blog_url_text.setText(blog.url)
