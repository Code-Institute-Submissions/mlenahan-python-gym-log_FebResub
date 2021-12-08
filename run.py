import argparse
from argparse import ArgumentError
from gym_log.controllers import movement

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
parser_movement_create.add_argument('--id', type=str)
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

args = parser.parse_args()
args.func(args)

# parser = argparse.ArgumentParser(
#     description='Gym logging app'
# )

# parser.add_argument(
#     'resource',
#     type=str,
#     help='The resource to interact with.'
# )

# parser.add_argument(
#     'action',
#     type=str,
#     help='Type of interaction.'
# )

# # Movement arguments

# parser.add_argument(
#     '--name',
#     type=str
# )

# parser.add_argument(
#     '--id',
#     type=str
# )

# parser.add_argument(
#     '--description',
#     type=str,
#     default=''
# )

# parser.add_argument(
#     '--notes',
#     type=str,
#     default=''
# )

# parser.add_argument(
#     '--difficulty',
#     type=str,
#     default=None
# )

# parser.add_argument(
#     '--weighted',
#     type=bool,
#     default=True
# )

# parser.add_argument(
#     '--tags',
#     nargs='+',
#     help='Set tags'
# )

# parser.add_argument(
#     '--workoutid',
#     type=str
# )

# parser.add_argument(
#     '--movementid',
#     type=str
# )

# parser.add_argument(
#     '--reps',
#     type=int
# )

# args = parser.parse_args()


# def validate_movement_add():
#     args = parser.parse_args()
#     args_dict = vars(args)
#     if args_dict['name'] is None:
#         raise ValueError('Must include name when adding a movement.')

# def validate_movement_retrieve():
#     args = parser.parse_args()
#     args_dict = vars(args)
#     if args_dict.get('id') is None:
#         raise ValueError('Must include id when retrieving a movement.')

# def validate_movement_show():
#     args = parser.parse_args()
#     args_dict = vars(args)
#     if args_dict['name'] or args_dict['workoutid'] is None:
#         raise ValueError(
#             'Must include name or workout id when showing a movement.')


# def validate_workout_add():
#     args = parser.parse_args()
#     args_dict = vars(args)
#     if args_dict['name'] is None:
#         raise ValueError('Must include name when adding a workout.')


# def validate_workout_delete():
#     args = parser.parse_args()
#     args_dict = vars(args)
#     if args_dict['name'] and args_dict['workoutid'] is None:
#         raise ValueError(
#             'Must include name or workout id when deleting a workout.')


# def validate_set_add():
#     args = parser.parse_args()
#     args_dict = vars(args)
#     if args_dict['workoutid'] and args_dict['movementid'] and args_dict['reps'] is None:
#         raise ValueError('Must include workout id, movement id and reps when adding a set')


# if args.resource == 'movement' and args.action == 'add':
#     validate_movement_add()
#     movement.add(args.name, description=args.description, notes=args.notes, difficulty=args.difficulty, weighted=args.weighted, tags=args.tags)

# if args.resource == 'movement' and args.action == 'update':
#     movement.update(args.id, name=args.name, description=args.description, notes=args.notes, difficulty=args.difficulty, weighted=args.weighted, tags=args.tags)

# if args.resource == 'movement' and args.action == 'delete':
#     movement.delete(args.id)

# if args.resource == 'movement' and args.action == 'retrieve':
#     validate_movement_retrieve()
#     entity = movement.retrieve(args.id)
#     print(entity)

# if args.resource == 'movement' and args.action == 'list':
#     entities = movement.list()
#     print(entities)

# if args.resource == 'movement' and args.action == 'show':
#     validate_movement_show()

# if args.resource == 'workout' and args.action == 'add':
#     validate_workout_add()

# if args.resource == 'set' and args.action == 'add':
#     validate_set_add()

# if args.resource == 'workout' and args.action == 'delete':
#     validate_workout_delete()
# # how to use - run.py movement add --name ... 

# # resource, action, value
# # movement show needs either id or name. write function to handle show

# # to add workout - doesnt need name but
# # workout - need id or name
# # workout delete needs value or name - need a name or id to know what to delete

# # cant add set without workout, exercise and number of reps
# # 