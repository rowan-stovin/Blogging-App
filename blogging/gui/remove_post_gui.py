import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from blogging.controller import Controller, IllegalOperationException

class RemovePostGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Remove a post")
        self.resize(600, 300)
        
        # Code input layout
        search_layout = QHBoxLayout()
        post_code_label = QLabel("Enter the Post's Code")
        self.post_code_text = QLineEdit()
        search_layout.addWidget(post_code_label)
        search_layout.addWidget(self.post_code_text)
        
        # Remove/Exit buttons
        button_layout = QHBoxLayout()
        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(self.remove)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit)
        button_layout.addWidget(remove_button)
        button_layout.addWidget(exit_button)
        
        # Main layout
        layout = QVBoxLayout()
        layout.addLayout(search_layout)
        layout.addLayout(button_layout)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def remove(self):
        code = None
        try:
            code = int(self.post_code_text.text())
        except ValueError:
            QMessageBox.warning(self, "Error", f"That wasn't a valid post code")
            return

        if self.controller.current_blog.post_dao_pickle.delete_post(code):
            QMessageBox.information(self, "Success", f"The post was deleted")
            self.post_code_text.setText("")
            self.close()
        else:
            QMessageBox.warning(self, "Error", f"That post does not exist in the current blog")

    def exit(self):
        self.close()