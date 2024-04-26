# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## API Access

You'll need a Trello account to be able to access the API in this project. To set this up, do the follwoing:

* [Create a Trello](https://trello.com/signup) account if you don't already have one, as well as a workspace and board.
* Create a [Trello Power Up](https://trello.com/power-ups/admin)
* Create an API key and copy this into the `.env` file.
* Add `http://http://127.0.0.1:5000` to the list of allowed origins.
* Select the link to generate an API token and also copy this into the `.env`.
* Make a call to `https://api.trello.com/1/members/me/boards?key={yourKey}&token={yourToken}` to find your board ID and copy this into the `.env` too.
* You'll also need to create a list. You can do so with a POST request to `https://api.trello.com/1/lists?name={name}&idBoard={boardId}&key={APIKey}&token={APIToken}`
* Copy the ID from the response into your `.env` file.

## Running the App

Once the all dependencies have been installed and you've set up Trello API access, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing

You can run the tests with `poetry run pytest`.

If using VSCode, you can set up the IDE to run the tests too. Click on the scientific flask on the left tab and configure the tests to use pytest from the `.` root directory (assuming you've openned the project from the `DevOps-Course-Starter` folder).

Once you've done this, you can view all the tests from this tab, as well as running specific tests by pressing the play button that should have appeared next to them, and also all the tests in a file/directory by right clicking and selecting 'Run tests'.

## Running the app on a virtual machine

> The below instructions assume that the username on your host is `ec2-user`. If not, you should replace instances of `ec2-user` in `playbook.yml` and `todoapp.service` with your user name.

Copy `inventory.ini`, `playbook.yml`, `.env.js2` and `todoapp.service` from the repo, to the root of your Ansible Control Node (ACN).

From your ACN, add the ip address of the host(s) you would like to use to `inventory.ini` under `[servers]`.

Execute `ansible-playbook playbook.yml -i inventory.ini` to run the app on your host(s)*.

Head to `http://<hostIpAddress>:5000/` to view your hosted app.