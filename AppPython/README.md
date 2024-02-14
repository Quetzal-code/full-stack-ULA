# Flask Basic Application Documentation

## Overview
This documentation describes a basic web application built using Flask, a lightweight WSGI web application framework in Python. The application simply returns the text "Hello, World!" when accessed.

## Requirements
- Python 3.x
- Flask

## Installation

### Setting Up a Virtual Environment
It's recommended to set up a virtual environment for Python projects, including Flask applications.

1. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
    ```
## Activate the Virtual Environment:
### On Windows:
    ```bash
    venv\Scripts\activate
    ```
### On Unix or MacOS:
    ``` bash
    source venv/bin/activate
    ```
# Installing Flask
After setting up and activating your virtual environment, install Flask using pip:

``` bash
pip install Flask
```

## Start the Flask Server:
Run the script using Python:

    ```bash
    python <script_name>.py
    Replace <script_name>.py with the actual filename of your Python script.
    ```
## Accessing the Application:

Open a web browser and navigate to http://localhost:5000/.
You should see 'Hello, World!' displayed on the page.