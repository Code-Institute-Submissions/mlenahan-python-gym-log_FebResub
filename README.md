# CLI Workout tracker

## Overview

CLI workout tracker. Users can record, list, and delete gym workout information. A [live instance of the application](https://python-gym-log-ml.herokuapp.com/) is hosted using a mock on Heroku.

The project was created as a learning exercise to understand how to create a simple file storage system and MVC design.

### Features

* [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) app which allows users to create, read, update, and delete the related data models: Workout, Movement, and Set.
* File storage backend - data is stored using a custom JSON file storage implementation.
* Formatted data using [tabulate](https://pypi.org/project/tabulate/) library.
* Nested command parsers using [argparse](https://docs.python.org/3/library/argparse.html). This allows for resources and actions to be comined in user commands, e.g. `movement delete abc-123`.

### Design

This application implements a simplified [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) design pattern.

There are three data models, `Set`, `Movement`, and `Workout` which are persisted using a file storage backend.

Controller functions are defined which hide the complexity of the model code from the view.

The view is a CLI which accepts user input and displays data to the user.

## Getting started

### Running locally

* Clone the repo
* Create and source a virtual environment in the project root: `python -m venv venv && source venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Run the application: `./run.py`
* Enter `-h` at the prompt to see usage instructions

### Example usage

* List entities: `<resource> list`
* Show an entity: `<resource> retrieve <id>`
* Delete an entity: `<resource> delete <id>`

![Example usage](media/screenshots/movement-all-actions.png)

## Testing

To run the unit tests: `python3 -m unittest`

I have also manually tested the project by doing the following:
    
- Passed the code through a PEP8 linter and confirmed there are no problems
- Tested in my local terminal and the Code Institute Heroku terminal 


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
* Fork or clone this repository
* Create a new Heroku app
* Set the buildpacks to Python and NodeJS in that order
* Link the Heroku app to the repository
* Select the correct branch and click Deploy Branch under the Manual deploy section

## Credits

* Code Institute for the terminal emulator
