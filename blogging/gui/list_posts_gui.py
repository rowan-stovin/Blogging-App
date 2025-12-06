import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPlainTextEdit
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from blogging.controller import Controller, IllegalOperationException

class ListPostsGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("List Posts")
        self.resize(600, 400)
        
        # Create the plain text edit widget
        self.text_display = QPlainTextEdit()
        self.text_display.setReadOnly(True)
        
        # Buttons
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.populate_posts)
        
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        
        # Horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(refresh_button)
        button_layout.addWidget(exit_button)
        
        # Central widget and layout
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)
        layout.addWidget(self.text_display)
        layout.addLayout(button_layout) # Add the horizontal button layout
        
    def populate_posts(self):
        """Populate the text display with all posts from current blog"""
        if not self.controller.current_blog:
            self.text_display.setPlainText("No blog selected. Please set a current blog first.")
            return
        
        posts = self.controller.current_blog.post_dao_pickle.posts
        
        if not posts:
            self.text_display.setPlainText("No posts found in this blog.")
            return
        
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


    def showEvent(self, event):
        """Called whenever the window is shown"""
        super().showEvent(event)
        # This kind of makes the refresh redundant...
        self.populate_posts()