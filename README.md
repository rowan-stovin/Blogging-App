# 📝 Python Blogging System (PyQt5)

A robust desktop application built with Python and the PyQt5 framework. This project demonstrates advanced **Object-Oriented Programming (OOP)** principles, secure data handling, and local state persistence.

---

## 🚀 Key Features

* **Full CRUD Functionality:** Users can seamlessly Create, Read, Update, and Delete blog posts.
* **Secure Authentication:** Engineered a custom login system using salted hash code protected passwords to ensure user data security.
* **State Persistence:** Integrated JSON-based persistence logic to manage and save state for blogs, posts, and user profiles across different sessions.
* **Event-Driven GUI:** A clean, intuitive interface built with PyQt, focusing on efficient event handling and user experience.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.12.5 |
| **GUI Framework** | PyQt5 |
| **Data Storage** | JSON (Persistence Layer) |
| **Security** | Python `hashlib` |

---

## 📸 Preview

<p align="center">
  <img width="602" alt="Blogging App UI" src="https://github.com/user-attachments/assets/f5897ea5-3848-49c9-87ef-c6d38436a97a" />
  <br>
  <sub><i>UI optimized for functional logic and state management testing.</i></sub>
</p>

---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/rowan-stovin/Blogging-App.git](https://github.com/rowan-stovin/Blogging-App.git)
cd Blogging-App
2. Install dependencies
Bash
pip install PyQt5
3. Run the application
Bash
python3 -m blogging gui
🧠 Design Philosophy
This project was developed with a focus on modular architecture. By decoupling the data persistence layer (JSON) from the frontend (PyQt5), the application maintains high readability and allows for easy expansion into SQL or cloud-based storage in future iterations.
