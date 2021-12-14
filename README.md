# Solaris Gym Tracker

Solaris Gym Tracker is Python terminal based gym tracker, which runs the Code Institute mock terminal on Heroku.

It was created using the argparse library.

Users have the ability to create, retrieve, list and delete movements, workouts and sets. These objects will be stored in a locally created storage system.

[Here is a link to the live version of this project](https://python-gym-log-ml.herokuapp.com/)

## How to use

To run the app locally, type ```python3 run.py``` into the terminal. If using the live version, you do not need to carry out this step as the mock terminal will do it for you.

Each action will have required arguments and optional arguments. 

```create``` has a required argument of name. ```retrieve``` has a required argument of id. ```delete``` has a required argument of id ```list``` has no required arguments. 

If you would like to create a movement, workout or set, you must include te object you would like to create and the required arguments that accompany that object.
If you wish to create a movement, type ```movement create squat```. 

If you would like to retrieve a movement, workout or set, you must include the object you would like to retrieve and the required arguments that accompany that object.
If you wish to create a movement, type ```movement retrieve squat```. 




## Creating the Heroku app


## Constraints

