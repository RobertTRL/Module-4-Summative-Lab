project_manager/
├── main.py                   # CLI entry point (if __name__ == "__main__")
├── models/
│   ├── __init__.py
│   ├── user.py               # User(Person): name, email, ID counter
│   ├── project.py            # Project: title, description, due_date
│   └── task.py               # Task: title, status, assigned_to
├── data/
│   ├── __init__.py
│   ├── storage.py            # JSON load/save with try-except
│   ├── data.json
├── utils/
│   ├── __init__.py
│   └── helpers.py            # Display helpers (rich/tabulate formatting)
├── cli/
│   ├── __init__.py
│   └── commands.py           # argparse subcommands (add-user, list-projects, etc.)
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   └── test_storage.py
├── venv/
├── requirements.txt
├── .gitignore
├── Pipfile
├── Pipfile.lock
└── README.md