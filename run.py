import argparse
from argparse import ArgumentError

parser = argparse.ArgumentParser(
    description='Gym logging app'
)

parser.add_argument(
    'resource',
    type=str,
    help='The resource to interact with.'
)

parser.add_argument(
    'action',
    type=str,
    help='Type of interaction.'
)

parser.add_argument(
    '--name',
    type=str
)

args = parser.parse_args()

def validate_movement_add():
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict['name'] is None:
        raise ValueError('Must include name when adding a movement.')

if args.resource == 'movement' and args.action == 'add':
    validate_movement_add()


# run.py movement add ... 

# resource, action, value
# movement show needs either id or name. write function to handle show

# to add workout - doesnt need name but
# workout - need id or name
# workout delete needs value or name - need a name or id to know what to delete

# cant add set without workout, exercise and number of reps
# 