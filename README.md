## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```
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

## Containerization
This project uses docker to containerize and keep the code running smoothly on any environment.

`docker compose up` will not rebuild the container image even if you have updated Dockerfile or project files. Therefore, if you changed any of those files, you should run `docker compose up` with the `--build` flag, and `d` detached, which will trigger a rebuild of the container image, and start container in a detached state.

to create a container with a specified docker compose file use the `-f` flag
`docker compose -f docker-compose.prod.yml up -d`

## Scripts
Two bash scripts are included for running tests and automating the deployment of site.

`./redeploy-script.sh` will pull recent changes from github repo and rebuild/start containers for program
`./run_test.sh` runs the tests specified in the tests/ directory.