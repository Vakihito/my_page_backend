# Application Backend

This is the backend of the application made using postgres as the database.

## Installation

After stablishing the enviroment via the docker file you should install de dependencies using : `poetry install`

## How the project is organized

Inside the `src` folder you should see a

- subproject such as `goals` and `user` and inside these folders you may create new routes.

- The `main` folder should be used for stablishing routes.

- The `shared` folder have shared code between the different subprojects

- The `utils` is used for utility scripts

Inside the subprojectsyou will see:

- `controller` - setup the route configurations
- `factory` - instanciate the service dependencies
- `infra` - for dabase functions
- `model` - stablish the models (table structures) of the objects
- `schema` - schemas of the data been used
- `service` - service that is called when the route is called

## Makefile and usefull commands

Here are some usefull commands that you can use via make inside this folder:

- `make run` - run the application with reload, the app start running
- `make fix-black` - fix the code formatting
- `make migrate-auto` - create a migration for the database, based on the `models` inside the folder
- `make migrate-up` - perform the migration stablished by `migrate-auto`
- `make migrate-down version=` - reset a specific version of migration
- `make route main= service=` - create the folder and files for a new route, `main` is the name of the subproject (like `goal` and `user`) and `service` is the what the service is doing such as `update`, `crate` and `delete`.

## Accessing API

You can acess the API via after running `make run` via `localhost:8000`, in the `http://localhost:8000/docs` you cen check the documentation for each route, and test them.

## .ENV file

The `.env` file is used for stablishing some enviroment variables you should change them depending on what enviroment variables you want to use, remember to also add them in the settings : `backend/src/main/settings.py`

## when resetting the alambic ( starting from screach )

Drop the alambic_version table then delete all the tables content, then run the `make migrate-up`

- DROP TABLE alembic_version;
- DROP TABLE goals;
