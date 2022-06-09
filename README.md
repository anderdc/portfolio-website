## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```
TRY THIS IF THE ABOVE DIDNT WORK, its possible your machine has python 2 and 3 installed
Create and activate virtual environment using virtualenv
```bash
$ python3 -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```
you might also need to be on Mac or linux based system per our own anecdotal debug attempts

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser!
