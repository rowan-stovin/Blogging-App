#**📝 Python Blogging System (PyQt5)**

A robust desktop application built with Python and the PyQt5 framework. This project demonstrates advanced Object-Oriented Programming (OOP) principles, secure data handling, and local state persistence.

#**🚀 Key Features**
**Full CRUD Functionality:** 
Users can seamlessly Create, Read, Update, and Delete blog posts.

##**Secure Authentication:** Engineered a custom login system using salted hash code protected passwords to ensure user data security.

##**State Persistence:** Integrated JSON-based persistence logic to manage and save state for blogs, posts, and user profiles across different sessions.

##**Event-Driven GUI:** A clean, intuitive interface built with PyQt, focusing on efficient event handling and user experience.

🛠️ #**Tech Stack**
_Language:_ Python 3.12.5

_GUI Framework:_ PyQt5

_Data Storage:_ JSON (Persistence Layer)

_Security:_ Python hashlib for password hashing

📸 #**Preview**
<img width="602" height="329" alt="Screenshot 2026-02-04 at 5 13 48 PM" src="https://github.com/user-attachments/assets/f5897ea5-3848-49c9-87ef-c6d38436a97a" />


⚙️ #**Installation & Usage**
_Clone the repository:_

git clone https://github.com/rowan-stovin/Blogging-App.git

_Install dependencies:_

pip install PyQt5

_Run the application:_

python3 -m blogging gui

🧠 #**Design Philosophy**
This project was developed with a focus on Object-Oriented Design. By separating the data persistence (JSON) from the UI logic (PyQt), the application follows a modular architecture that is easy to scale and maintain. This foundation allows for future expansions, such as integrating a cloud-based API or a SQL database.
