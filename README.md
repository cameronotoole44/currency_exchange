# Currency Converter

This Python project enables users to convert between different currencies using two interfaces: a web-based interface built with Flask and a graphical user interface (GUI) created with Tkinter. Originally based on an assignment, I expanded it into a comprehensive application to strengthen and showcase my skills with these technologies.

# Features

- Convert between multiple currencies (USD, EUR, JPY, GBP, CAD, CHF)
- Web-based interface for currency conversion using Flask
- GUI version using tkinter for a desktop experience

# Installation

## Clone the repository:

```
   git clone https://github.com/cameronotoole44/currency-converter.git
   cd currency-converter
```

## Set up the virtual environment:

```
   python -m venv currency-venv
   source currency-venv/Scripts/activate # On Windows
   source currency-venv/bin/activate # On macOS/Linux
```

## Install required packages:

```
   pip install -r requirements.txt
```

# Running the Project

## Web Version

### Navigate to the web directory:

```
   cd web
```

### Set the FLASK_APP environment variable:

```
   export FLASK_APP=app.py # On macOS/Linux
   set FLASK_APP=app.py # On Windows
```

### Run the Flask application:

```
   flask run
```

- **Open your browser** and **visit** http://127.0.0.1:5000 to access the web interface

## For the GUI version

### Navigate to the GUI directory

```
cd GUI
```

### Run the GUI application

```
python gui_app.py
```

## Credits

[Transparent Textures](https://www.transparenttextures.com/) for the background patterns

[Google Fonts](https://fonts.google.com/) for typography
