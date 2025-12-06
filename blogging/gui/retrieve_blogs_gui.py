import sys
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableView
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from blogging.controller import Controller, IllegalOperationException

class RetrieveBlogsGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Retrieve blogs")
        self.resize(600, 400)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        
        # Search input
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter keyword(s) here...")
        self.layout.addWidget(self.line_edit)

        # Clear button
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_retrieved_blogs)
        self.clear_button.clicked.connect(self.line_edit.clear)
        self.clear_button.setMinimumSize(100, 50)

        # Search button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.on_search)
        self.search_button.setMinimumSize(100, 50)

        # Exit button
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit)
        self.exit_button.setMinimumSize(100, 50)
        
        # Table view
        self.table_view = QTableView()
        self.layout.addWidget(self.table_view)
        
        # Model
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID', 'Name', 'URL', 'Email'])
        self.table_view.setModel(self.model)
        
        # Horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.exit_button)
        self.layout.addLayout(button_layout)
        
        # Configure table appearance
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table_view.setSelectionMode(QTableView.SelectionMode.SingleSelection)
    
    def on_search(self):
        """ Searches for the blogs with the provided str in title"""
        search_string = self.line_edit.text()
        search_string = search_string.strip()
        blogs = self.controller.blog_dao_json.retrieve_blogs(search_string)
        
        if not blogs:
            QMessageBox.warning(self, "Error", "No blogs with those keyword(s) were found, sorry!")
            return
        
        self.show_retrieved_blogs(blogs)

    def clear_retrieved_blogs(self):
        """ Clears data"""
        # Clear existing data
        self.model.removeRows(0, self.model.rowCount())
    
    def show_retrieved_blogs(self, blogs):
        """ Fills the table and resizes it"""
        self.clear_retrieved_blogs()

        # Populate with new data
        self.populate_table(blogs)
        
        # Resize columns to fit content
        self.table_view.resizeColumnsToContents()
    
    def populate_table(self, blogs):
        """ Fills the table"""
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

    def exit(self):
        """ Clears text and closes the window"""
        self.line_edit.setText("")
        self.clear_retrieved_blogs()
        self.close()