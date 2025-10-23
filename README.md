# MyToDo - Task Management Application

A simple and efficient task management web application built with Flask and SQLAlchemy. Keep track of your daily tasks with a clean, dark-mode interface.

## 📋 Features

- ✅ **Create Tasks**: Add new todo items with title and description
- ✅ **View All Tasks**: See all your todos in one organized table
- ✅ **Update Tasks**: Edit existing todos anytime
- ✅ **Delete Tasks**: Remove completed or unwanted tasks
- ✅ **Search Functionality**: Real-time search through your todos
- ✅ **Auto Timestamps**: Automatic creation time for each task
- ✅ **Dark Mode UI**: Easy on the eyes with Bootstrap 5.3 dark theme
- ✅ **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Backend**: Flask (Python Web Framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Template Engine**: Jinja2
- **JavaScript**: Vanilla JS for search functionality

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Manav0411/mytodo.git
   cd mytodo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy
   ```

5. **Initialize the database**
   ```bash
   python init_db.py
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   Navigate to `http://localhost:8000`

## 🚀 Usage

1. **Add a Todo**: Fill in the title and description in the form and click "Submit"
2. **View Todos**: All your tasks are displayed in the table below
3. **Search**: Use the search bar next to "My ToDos" to filter tasks
4. **Update**: Click the "Update" button to edit a todo
5. **Delete**: Click the "Delete" button to remove a todo

## 📁 Project Structure

```
FLASK_APP/
│
├── app.py                  # Main application file
├── init_db.py             # Database initialization script
├── README.md              # Project documentation
│
├── instance/
│   └── todo.db            # SQLite database (auto-generated)
│
├── static/                # Static files (CSS, JS, images)
│
├── templates/             # HTML templates
│   ├── base.html         # Base template with navbar
│   ├── index.html        # Home page with todo list
│   ├── update.html       # Update todo page
│   └── about.html        # About page
│
└── .venv/                # Virtual environment (not in git)
```

## 🗄️ Database Schema

### ToDo Model

| Column        | Type     | Description                    |
|--------------|----------|--------------------------------|
| sno          | Integer  | Primary key (auto-increment)   |
| title        | String   | Todo title (max 200 chars)     |
| desc         | String   | Todo description (max 500)     |
| date_created | DateTime | Timestamp (auto-generated)     |


## 🔧 Configuration

The application uses the following default configurations:

- **Database URI**: `sqlite:///todo.db`
- **Debug Mode**: Enabled (disable in production)
- **Port**: 8000
- **Track Modifications**: Disabled

To modify these settings, edit the `app.py` file:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.run(debug=True, port=8000)
```

## 📝 Future Enhancements

- [ ] User authentication and login
- [ ] Task categories/tags
- [ ] Priority levels for tasks
- [ ] Due dates and reminders
- [ ] Task completion status
- [ ] Export todos to CSV/PDF
- [ ] Light/Dark mode toggle
- [ ] Task statistics and analytics


## 👨‍💻 Developer

**Developed by**: Manav Goel  
**Email**: me.manavgoel@gmail.com  
**GitHub**: [@Manav0411](https://github.com/Manav0411)  
**Last Updated**: October 2025
