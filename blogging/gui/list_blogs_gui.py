import sys
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableView
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from blogging.controller import Controller, IllegalOperationException

class ListBlogsGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Lists Blogs")
        self.resize(600, 200)
        
        # Table view
        self.table_view = QTableView()
        
        # Model
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID', 'Name', 'URL', 'Email'])
        self.table_view.setModel(self.model)
        self.populate_table()
        
        # Configure table appearance
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table_view.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        
        #buttons
        button_layout = QHBoxLayout()
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.refresh_table)
        refresh_button.setMinimumSize(100, 50)
        button_layout.addWidget(refresh_button)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit)
        exit_button.setMinimumSize(100, 50)
        button_layout.addWidget(exit_button)
        
        
        # Central widget and layout
        widget = QWidget()
        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        self.setCentralWidget(widget)
        self.layout = QVBoxLayout(widget)
        self.layout.addWidget(self.table_view)
        self.layout.addWidget(button_widget)

    def exit(self):
        self.close()
        
    def refresh_table(self):
        # Clear existing data
        self.model.removeRows(0, self.model.rowCount())
        self.populate_table()

    def populate_table(self):
        blogs = self.controller.blog_dao_json.list_blogs()
        # Add rows to the model
        for blog in blogs:

            row_items = [
                QStandardItem(str(blog.id)),
                QStandardItem(blog.name),
                QStandardItem(blog.url),
                QStandardItem(blog.email)
            ]
            
            # Make items read only
            for item in row_items:
                item.setEditable(False)
            self.model.appendRow(row_items)