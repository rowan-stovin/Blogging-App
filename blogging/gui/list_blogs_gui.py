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
        
        #exit button
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit)

        # Central widget and layout
        widget = QWidget()
        self.setCentralWidget(widget)
        self.layout = QVBoxLayout(widget)
        self.layout.addWidget(self.table_view)
        self.layout.addWidget(exit_button)

    def exit(self):
        self.close()
        
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