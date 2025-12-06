import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from blogging.controller import Controller, IllegalOperationException

class UpdateBlogGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Update a Blog")
        self.resize(600, 200)
        
        #info
        info_layout = QGridLayout()

        blog_id_label = QLabel("Blog's ID:")
        self.blog_id_text = QLineEdit()
        id_clear_button = QPushButton("Clear ID")
        id_clear_button.clicked.connect(self.clear_id)
        blog_name_label = QLabel("Blog's Name:")
        self.blog_name_text = QLineEdit()
        name_clear_button = QPushButton("Clear Name")
        name_clear_button.clicked.connect(self.clear_name)
        blog_url_label = QLabel("Blog's URL:")
        self.blog_url_text = QLineEdit()
        url_clear_button = QPushButton("Clear URL")
        url_clear_button.clicked.connect(self.clear_url)
        blog_email_label = QLabel("Blog's Email:")
        self.blog_email_text = QLineEdit()
        email_clear_button = QPushButton("Clear Email")
        email_clear_button.clicked.connect(self.clear_email)

        info_layout.addWidget(blog_id_label, 0, 0)
        info_layout.addWidget(self.blog_id_text, 0, 1)
        info_layout.addWidget(id_clear_button, 0, 2)
        info_layout.addWidget(blog_name_label, 1, 0)
        info_layout.addWidget(self.blog_name_text, 1, 1)
        info_layout.addWidget(name_clear_button, 1, 2)
        info_layout.addWidget(blog_url_label, 2, 0)
        info_layout.addWidget(self.blog_url_text, 2, 1)
        info_layout.addWidget(url_clear_button, 2, 2)
        info_layout.addWidget(blog_email_label, 3, 0)
        info_layout.addWidget(self.blog_email_text, 3, 1)
        info_layout.addWidget(email_clear_button, 3, 2)
        
        #buttons
        button_layout = QHBoxLayout()

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search)
        search_button.setMinimumSize(100, 50)
        button_layout.addWidget(search_button)
        
        update_button = QPushButton("Update")
        update_button.clicked.connect(self.update)
        update_button.setMinimumSize(100, 50)
        button_layout.addWidget(update_button)
        
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit)
        exit_button.setMinimumSize(100, 50)
        button_layout.addWidget(exit_button)
        
        #search
        search_layout = QHBoxLayout()
        
        blog_id_label_search = QLabel("To update a Blog, please enter it's ID:")
        self.blog_id_text_search = QLineEdit()
        search_layout.addWidget(blog_id_label_search)
        search_layout.addWidget(self.blog_id_text_search)

        #main
        layout = QVBoxLayout()
        
        top_widget = QWidget()
        top_widget.setLayout(search_layout) 
        middle_widget = QWidget()
        middle_widget.setLayout(info_layout)
        bottom_widget = QWidget()
        bottom_widget.setLayout(button_layout)

        layout.addWidget(top_widget)
        layout.addWidget(middle_widget)
        layout.addWidget(bottom_widget)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def search(self):
        """ Searches for the blog with the given id"""
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
        """ Clears the fields"""
        self.unfill()
        self.close()

    def fill(self, blog):
        """ Fills all the fields"""
        self.blog_id_text.setText(str(blog.id))
        self.blog_email_text.setText(blog.email)
        self.blog_name_text.setText(blog.name)
        self.blog_url_text.setText(blog.url)

    def unfill(self):
        """ Clears all the fields"""
        self.blog_id_text_search.setText("")
        self.blog_id_text.setText("")
        self.blog_email_text.setText("")
        self.blog_name_text.setText("")
        self.blog_url_text.setText("")

    def clear_name(self):
        """ Clears name"""
        self.blog_name_text.setText("")
        return

    def clear_id(self):
        """ Clears the id"""
        self.blog_id_text.setText("")
        return

    def clear_email(self):
        """ Clears the email"""
        self.blog_email_text.setText("")
        return

    def clear_url(self):
        """ Clears the URL"""
        self.blog_url_text.setText("")
        return
    
    def clear_all(self):
        """ Clears all fields"""
        self.blog_id_text_search.setText("")
        self.clear_name()
        self.clear_id()
        self.clear_email()
        self.clear_url()

    def update(self):
        """ Updates the blog with the new info"""
        try:
            id = int(self.blog_id_text_search.text())
            key = int(self.blog_id_text.text())
            old_blog = self.controller.blog_dao_json.search_blog(id)
            existing_blog = self.controller.blog_dao_json.search_blog(key)
            
            #changes
            name = self.blog_name_text.text()
            email = self.blog_email_text.text()
            url = self.blog_url_text.text()

            #Checks for a blog with the new ID or if it is the current blog
            if existing_blog or id == key:
                reply = QMessageBox.question(self, "Confirm", "Are you sure you want to make these changes?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    self.controller.update_blog(id, key, name, url, email)
                    QMessageBox.information(self, "Success", "The blog was successfully updated")
                    self.clear_all()
                    self.close()
                    # self.blog_id_text_search.setText(str(key))
                    return
            elif existing_blog and existing_blog is not old_blog:
                QMessageBox.warning(self, "Error", "There is already an existing blog with that id")
                return

            elif old_blog == self.controller.current_blog:
                QMessageBox.warning(self, "Error", "Cannot update the current blog")
                return
            
            return
        except:
            QMessageBox.warning(self, "Error", "Not a valid id")
            return