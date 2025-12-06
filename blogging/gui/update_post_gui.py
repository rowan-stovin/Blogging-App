import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPlainTextEdit
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from blogging.controller import Controller, IllegalOperationException

class UpdatePostGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Update a post")
        self.resize(600, 400)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Search section
        search_layout = QHBoxLayout()
        post_code_label = QLabel("Enter Post Code:")
        self.post_code_input = QLineEdit()
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_post)
        
        search_layout.addWidget(post_code_label)
        search_layout.addWidget(self.post_code_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)
        
        # Edit fields
        edit_layout = QGridLayout()
        
        title_label = QLabel("Title:")
        self.title_input = QLineEdit()
        
        text_label = QLabel("Text:")
        self.text_input = QPlainTextEdit()
        
        edit_layout.addWidget(title_label, 0, 0)
        edit_layout.addWidget(self.title_input, 0, 1)
        edit_layout.addWidget(text_label, 1, 0)
        edit_layout.addWidget(self.text_input, 1, 1)
        layout.addLayout(edit_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.save_button = QPushButton("Save Changes")
        self.save_button.clicked.connect(self.save_post)
        
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(exit_button)
        layout.addLayout(button_layout)
        
        # Initially disable edit fields and save button
        self.set_edit_enabled(False)
        self.current_post_code = None
    
    def set_edit_enabled(self, enabled):
        """Enable or disable edit fields and save button"""
        self.title_input.setEnabled(enabled)
        self.text_input.setEnabled(enabled)
        self.save_button.setEnabled(enabled)
    
    def search_post(self):
        """Search for post by code"""
        # Check if current blog exists
        try:
            code = int(self.post_code_input.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Error", "That isn't a valid code")
        
        if not code:
            QMessageBox.warning(self, "Error", "Please enter a post code")
            return
        
        post = self.controller.current_blog.search_post(code)
        
        if post:
            # Fill the fields with current values
            self.current_post_code = code
            self.title_input.setText(post.title)
            self.text_input.setPlainText(post.text)
            self.set_edit_enabled(True)
        else:
            QMessageBox.warning(self, "Error", "No post found with that code")
            self.set_edit_enabled(False)
    
    def save_post(self):
        """Save the updated post"""
        if not self.current_post_code:
            QMessageBox.warning(self, "Error", "No post loaded to update")
            return
        
        # Get updated values
        new_title = self.title_input.text().strip()
        new_text = self.text_input.toPlainText().strip()
        
        if not new_title or not new_text:
            QMessageBox.warning(self, "Error", "Title and text cannot be empty.")
            return
        
        # Update the post using controller method
        success = self.controller.current_blog.update_post(
            self.current_post_code, 
            new_title, 
            new_text
        )
        
        if success:
            QMessageBox.information(self, "Success", "Post updated successfully!")
            self.clear_form()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Failed to update post.")
    
    def clear_form(self):
        """Clear all input fields"""
        self.post_code_input.clear()
        self.title_input.clear()
        self.text_input.clear()
        self.set_edit_enabled(False)
        self.current_post_code = None