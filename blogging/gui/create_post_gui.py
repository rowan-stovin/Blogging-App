import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPlainTextEdit
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
        self.resize(600, 400)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Input fields
        info_layout = QGridLayout()
        
        post_title_label = QLabel("Title:")
        self.post_title_text = QLineEdit()
        
        post_text_label = QLabel("Text:")
        self.post_text_text = QPlainTextEdit()
        
        info_layout.addWidget(post_title_label, 0, 0)
        info_layout.addWidget(self.post_title_text, 0, 1)
        info_layout.addWidget(post_text_label, 1, 0)
        info_layout.addWidget(self.post_text_text, 1, 1)
        layout.addLayout(info_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        create_button = QPushButton("Create")
        create_button.clicked.connect(self.create)
        
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit)
        
        button_layout.addWidget(create_button)
        button_layout.addWidget(exit_button)
        layout.addLayout(button_layout)
    
    def exit(self):
        self.close()
    
    def create(self):
        # Check if current blog exists
        if not self.controller.current_blog:
            QMessageBox.warning(self, "Error", "No blog selected. Please set a current blog first.")
            return
        
        title = self.post_title_text.text().strip()
        text = self.post_text_text.toPlainText().strip()
        
        if not title or not text:
            QMessageBox.warning(self, "Error", "Title and text cannot be empty.")
            return
        
        self.controller.current_blog.create_post(title, text)
        QMessageBox.information(self, "Success", "The post was created successfully!")
        self.clear_form()
        self.close()
    
    def clear_form(self):
        """Clear all input fields"""
        self.post_title_text.clear()
        self.post_text_text.clear()