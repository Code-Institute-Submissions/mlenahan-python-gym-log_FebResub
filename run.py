import argparse
from argparse import ArgumentError
from gym_log.controllers import movement, workout, set
from tabulate import tabulate

# main parser
parser = argparse.ArgumentParser(description='Gym logging app')
subparsers = parser.add_subparsers()

# movement subparser
parser_movement = subparsers.add_parser('movement', help='TODO')
movement_subparsers = parser_movement.add_subparsers()

# movement create subparser
def movement_create(args):
    movement.add(args.name, description=args.description, notes=args.notes, difficulty=args.difficulty, weighted=args.weighted, tags=args.tags)

parser_movement_create = movement_subparsers.add_parser('create', help='TODO')
parser_movement_create.set_defaults(func=movement_create)
parser_movement_create.add_argument('name', type=str)
parser_movement_create.add_argument('--description', type=str, default='')
parser_movement_create.add_argument('--notes', type=str, default='')
parser_movement_create.add_argument('--difficulty', type=str, default=None)
parser_movement_create.add_argument('--weighted', type=bool, default=True)
parser_movement_create.add_argument('--tags', nargs='+', help='Set tags')


# movement delete subparser
def movement_delete(args):
    movement.delete(args.id)

parser_movement_delete = movement_subparsers.add_parser('delete', help='TODO')
parser_movement_delete.set_defaults(func=movement_delete)
parser_movement_delete.add_argument('id', type=str)

# movement retrieve subparser

def movement_retrieve(args):
    entity = movement.retrieve(args.id)
    headers = ['Name', 'ID', 'Description', 'Difficulty', 'Notes', 'Tags', 'Weighted']
    row = [entity.name, entity.id, entity.description, entity.difficulty, entity.notes, entity.tags, entity.weighted]
    table = tabulate([row], headers=headers)
    print(table)

parser_movement_retrieve = movement_subparsers.add_parser('retrieve', help='TODO')
parser_movement_retrieve.set_defaults(func=movement_retrieve)
parser_movement_retrieve.add_argument('id', type=str)

# movement list subparser

def movement_list(args):
    entities = movement.list()
    headers = ['Name', 'ID', 'Description', 'Difficulty', 'Notes', 'Tags', 'Weighted']
    rows = []
    for entity in entities:
        row = [entity.name, entity.id, entity.description, entity.difficulty, entity.notes, entity.tags, entity.weighted]
        rows.append(row)
    table = tabulate(rows, headers=headers)
    print(table)
    

parser_movement_list = movement_subparsers.add_parser('list', help='TODO')
parser_movement_list.set_defaults(func=movement_list)

# workout subparser
parser_workout = subparsers.add_parser('workout', help='TODO')
workout_subparsers = parser_workout.add_subparsers()

# workout create subparser
def workout_create(args):
    workout.add(args.name, description=args.description, notes=args.notes, tags=args.tags)

parser_workout_create = workout_subparsers.add_parser('create', help='TODO')
parser_workout_create.set_defaults(func=workout_create)
parser_workout_create.add_argument('name', type=str)
parser_workout_create.add_argument('--description', type=str, default='')
parser_workout_create.add_argument('--notes', type=str, default='')
parser_workout_create.add_argument('--tags', nargs='+', help='Set tags')


# workout delete subparser
def workout_delete(args):
    workout.delete(args.id)

parser_workout_delete = workout_subparsers.add_parser('delete', help='TODO')
parser_workout_delete.set_defaults(func=workout_delete)
parser_workout_delete.add_argument('id', type=str)

# workout retrieve subparser

def workout_retrieve(args):
    entity = workout.retrieve(args.id)
    headers = ['Name', 'ID', 'Description', 'Notes', 'Tags']
    row = [entity.name, entity.id, entity.description, entity.notes, entity.tags]
    table = tabulate([row], headers=headers)
    print(table)

parser_workout_retrieve = workout_subparsers.add_parser('retrieve', help='TODO')
parser_workout_retrieve.set_defaults(func=workout_retrieve)
parser_workout_retrieve.add_argument('id', type=str)

# workout list subparser

def workout_list(args):
    entities = workout.list()
    headers = ['Name', 'ID', 'Description', 'Notes', 'Tags']
    rows = []
    for entity in entities:
        row = [entity.name, entity.id, entity.description, entity.notes, entity.tags]
        rows.append(row)
    table = tabulate(rows, headers=headers)
    print(table)
    

parser_workout_list = workout_subparsers.add_parser('list', help='TODO')
parser_workout_list.set_defaults(func=workout_list)

# set subparser
parser_set = subparsers.add_parser('set', help='TODO')
set_subparsers = parser_set.add_subparsers()

# set create subparser
def set_create(args):
    set.add(args.movement_id, args.workout_id, args.rep_count, rpe=args.rpe, notes=args.notes)

parser_set_create = set_subparsers.add_parser('create', help='TODO')
parser_set_create.set_defaults(func=set_create)
parser_set_create.add_argument('movement_id', type=str)
parser_set_create.add_argument('workout_id', type=str)
parser_set_create.add_argument('rep_count', type=int)
parser_set_create.add_argument('--notes', type=str, default='')
parser_set_create.add_argument('--rpe', type=int)

# set delete subparser
def set_delete(args):
    set.delete(args.id)

parser_set_delete = set_subparsers.add_parser('delete', help='TODO')
parser_set_delete.set_defaults(func=set_delete)
parser_set_delete.add_argument('id', type=str)

# set retrieve subparser

def set_retrieve(args):
    entity = set.retrieve(args.id)
    headers = ['Movement', 'Workout', 'ID', 'Rep Count', 'RPE', 'Notes']
    row = [entity.movement_id, entity.workout_id, entity.id, entity.rep_count, entity.rpe, entity.notes]
    table = tabulate([row], headers=headers)
    print(table)

parser_set_retrieve = set_subparsers.add_parser('retrieve', help='TODO')
parser_set_retrieve.set_defaults(func=set_retrieve)
parser_set_retrieve.add_argument('id', type=str)

# set list subparser

def set_list(args):
    entities = set.list()
    headers = ['Movement', 'Workout', 'ID', 'Rep Count', 'RPE', 'Notes']
    rows = []
    for entity in entities:
        row = [entity.movement_id, entity.workout_id, entity.id, entity.rep_count, entity.rpe, entity.notes]
        rows.append(row)
    table = tabulate(rows, headers=headers)
    print(table)
    

parser_set_list = set_subparsers.add_parser('list', help='TODO')
parser_set_list.set_defaults(func=set_list)

args = parser.parse_args()
# args.func(args)

try:
    func = args.func
except AttributeError:
    parser.error("too few arguments")
func(args)
