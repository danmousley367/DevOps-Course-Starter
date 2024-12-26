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

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
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

### Running tests in the IDE

You can run the tests with `poetry run pytest`.

If using VSCode, you can set up the IDE to run the tests too. Click on the scientific flask on the left tab and configure the tests to use pytest from the `.` root directory (assuming you've openned the project from the `DevOps-Course-Starter` folder).

Once you've done this, you can view all the tests from this tab, as well as running specific tests by pressing the play button that should have appeared next to them, and also all the tests in a file/directory by right clicking and selecting 'Run tests'.

### Running tests in a docker container

First, build the test image from the root of the repository with:

`docker build --target test -t todoapp:test .`

Then, run the tests in the container with:

`docker run --rm todoapp:test`

Note, the `--rm` flag will remove your container once the tests have completed.

## Running the app on a virtual machine

> The below instructions assume that the username on your host is `ec2-user`. If not, you should replace instances of `ec2-user` in `playbook.yml` and `todoapp.service` with your user name.

Copy `inventory.ini`, `playbook.yml`, `.env.js2` and `todoapp.service` from the repo, to the root of your Ansible Control Node (ACN).

From your ACN, add the ip address of the host(s) you would like to use to `inventory.ini` under `[servers]`.

Execute `ansible-playbook playbook.yml -i inventory.ini` and enter your API key and API token to run the app on your host(s).

Head to `http://<hostIpAddress>:5000/` to view your hosted app.

## Running the app in a Docker container

### Run a production version of the app

Build the container with:

`docker build --target production --tag todo-app:prod .`

Run the app in the container with:

`docker run --env-file .env --publish 5000:5000 -d todo-app:prod`

### Run a development version of the app

The development version will allow you to view detailed logging and feedback and see rapid changes made in the code without having to rebuild.

Build and run the conatiner with:

`docker-compose up`

## Production app Docker image

The production app image is deployed to DockerHub and can be pulled from the following link:

`docker.io/danmou367/my-todo-app:prod`

## App deployment

App deployment is now managed by GitHub Actions CI and the infrastructure is managed using Terraform. The Terraform state file exists in `danmoustoragecontainer` in the `danmoustorageaccount` on Azure.

The app is now deployed at:

`https://test-danmou-061224-terraform-todoapp.azurewebsites.net/`

### Data encryption status

Our data is currently stored in Azure Cosmos DB, for which [all data is encrypted at rest](https://learn.microsoft.com/en-us/azure/cosmos-db/database-encryption-at-rest).