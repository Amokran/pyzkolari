# PYZKOLARI

Pyzkolari is a Python module designed to provide an easy-to-use logging system for Python applications. It allows developers to log messages with different severity levels, making it easier to track application behavior and diagnose issues.

Pyzkolari comes from the Basque word ["aizkolari"](https://en.wikipedia.org/wiki/Aizkolaritza), which translates into somone who uses an axe, typically in the context of logging or chopping wood, but with sporting aim. The name reflects the module's purpose of "chopping" through logs and providing a clear view of application events. 

## Current state of things

This project is currently in its early stages. The initial version is functional, but there are many features and improvements planned for future releases.

## Purpose

Obvious: to provide a logging system for Python applications. Extra: to provide a logging system that is easy to use, flexible, and extensible.

## Ethics and values
This is designed to be used in a responsible way. You know what I mean.
In case you don't, it's easy: don't use this to harm the weak and the helpless. Even if it's people you don't like.
In any case, try to use it for good, and to help others.

## 📁 Project Structure

The project structure is designed to be simple and intuitive, following common Python project conventions. Here's an overview of the directory structure:

````plaintext:
project_name/
├── src/                  # Source code
│   └── (sub)module_name/ # Main Python
│       ├── __init__.py
│       └── ...
│
├── assets/            # Static files, configurations, translations, etc.
│
├── tests/                # Unit tests
│
├── main.py               # Example script for execution. Doesn't provide any functionality, just an example of how to use the module.
├── VERSION               # Version of the project (to be filled by the developer)
├── requirements.txt      # List of dependencies
├── README.md             # Project overview and instructions
├── CHANGELOG.md          # Project changelog (optional)
├── CONTRIBUTING.md       # Contribution guidelines
└── .template/            # Template metadata (version, changelog, etc.)
````

## 🚀 Getting Started

Prerequisites
Python 3.8 or higher

pip (Python package installer)

### Installation

Repo GitHub page: https://github.com/Amokran/pyzkolari

Clone the repository:

````bash:
git clone https://github.com/Amokran/pyzkolari.git
````

It is advised to clone the repository as a submodule of your project, so you can keep it up to date easily, since this is still in early development so it won't be uploaded to PyPI yet.

(Optional) Create and activate a virtual environment:

````bash:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
````

### Install dependencies:

````bash:
pip install -r requirements.txt
````

## 🧠 Usage

You'll find a main.py file in the root directory, but that is a mere example of how to use the module. 

````bash:
python main.py
````

However, the main functionality is encapsulated in the `pyzkolari` package under the `src/` directory. That's what you should import in your own code:

```python 
from pyzkolari import LogManager
````

## 🧪 Running Tests

To run the tests, you can use pytest or unittest. If you have pytest installed, you can run:

````bash:   
pytest tests/
````
You can also configure pytest.ini or use other test runners if preferred.

## 🔧 Configuration

*@TODO: Add any information about external files, environment variables, or config options stored under resources/.*

## 📦 Versioning
The current project version is stored in the VERSION file.

This project was generated from python-template-a.
Template version can be found in .template/VERSION.

## 📄 License

*@TODO: Replace with your license information if necessary*
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Feedback
To report bugs or suggest improvements, please refer to the CONTRIBUTING.md guidelines.




