# Todo List Application

A simple and efficient Todo List application built with Django 3.1.1. This application allows users to create and manage their daily tasks with a clean and intuitive interface.

## Features

- Create new tasks with titles
- View all tasks in a list format
- Automatic timestamp for each task
- Responsive design with custom CSS styling
- Clean and user-friendly interface

## Technical Stack

- Python 3.10
- Django 3.1.1
- SQL database
- HTML/CSS for frontend

## Project Structure

```
mytodo/
├── mytodoapp/           # Main application directory
│   ├── models.py       # Contains Task model
│   ├── views.py        # Application views
│   ├── urls.py         # URL configurations
│   └── templates/      # HTML templates
│       ├── index.html
│       ├── starter.html
│       └── tasklist.html
└── static/            # Static files (CSS, media)
    └── css/
        ├── form.css
        ├── navigation.css
        └── tasklist.css
```

## Setup and Installation

1. Create a virtual environment:
   ```
   python -m venv myvenv
   ```

2. Activate the virtual environment:
   - Windows:
     ```
     myvenv\Scripts\activate
     ```
   - Linux/Mac:
     ```
     source myvenv/bin/activate
     ```

3. Install required packages:
   ```
   pip install django==3.1.1
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://localhost:8000`

## Usage

1. Navigate to the home page
2. Enter a task title in the input field
3. Submit to create a new task
4. View all tasks in the task list page

## Development

The application uses:
- `models.py` for defining the Task model
- `views.py` for handling business logic
- Template files for rendering the UI
- Custom CSS for styling

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Created

This project was created on October 17, 2025.
