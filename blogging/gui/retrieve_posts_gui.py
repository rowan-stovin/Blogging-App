import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPlainTextEdit
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from blogging.controller import Controller, IllegalOperationException

class RetrievePostsGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Retrieve posts")
        self.resize(600, 400)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Search input
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter keyword(s) here...")
        layout.addWidget(self.line_edit)
        
        # Search button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.on_search)
        layout.addWidget(self.search_button)
        
        # Text display for posts
        self.text_display = QPlainTextEdit()
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)
        
        # Buttons: Clear and Exit
        button_layout = QHBoxLayout()
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_retrieved_posts)
        
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(exit_button)
        layout.addLayout(button_layout)
    
    def on_search(self):
        # Check if current blog exists
        if not self.controller.current_blog:
            QMessageBox.warning(self, "Error", "No blog selected. Please set a current blog first.")
            return
        
        search_string = self.line_edit.text().strip()
        
        # Retrieve posts from current blog
        posts = self.controller.current_blog.retrieve_posts(search_string)
        
        if not posts:
            QMessageBox.warning(self, "Error", "No posts with those keyword(s) were found, sorry!")
            return
        
        self.show_retrieved_posts(posts)
    
    def clear_retrieved_posts(self):
        # Clear text display and search input
        self.text_display.clear()
        self.line_edit.clear()
    
    def show_retrieved_posts(self, posts):
        # Format posts as text
        output = []
        for post in posts[::-1]:
            output.append("=" * 60)
            output.append(f"Post: {post.code}")
            output.append(f"Title: {post.title}")
            output.append(f"Text:\n{post.text}")
            output.append("=" * 60)
            output.append("")  # Empty line between posts
        
        self.text_display.setPlainText("\n".join(output))