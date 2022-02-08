import argparse
from tabulate import tabulate
from gym_log.controllers import movement, workout, set


# movement create subparser
def movement_create(args):
    movement.create(
        args.name,
        description=args.description,
        notes=args.notes,
        difficulty=args.difficulty,
        weighted=args.weighted,
        tags=args.tags)


# movement delete subparser
def movement_delete(args):
    movement.delete(args.id)


# movement retrieve subparser
def movement_retrieve(args):
    headers = [
        'Name',
        'ID',
        'Description',
        'Difficulty',
        'Notes',
        'Tags',
        'Weighted']
    try:
        entity = movement.retrieve(args.id)
    except ValueError as e:
        print(e)
        return
    row = [
        entity.name,
        entity.id,
        entity.description,
        entity.difficulty,
        entity.notes,
        entity.tags,
        entity.weighted]
    table = tabulate([row], headers=headers)
    print(table)


# movement list subparser
def movement_list(args):
    headers = [
        'Name',
        'ID',
        'Description',
        'Difficulty',
        'Notes',
        'Tags',
        'Weighted']
    try:
        entities = movement.list()
    except FileNotFoundError:
        table = tabulate([], headers=headers)
        print(table)
        return
    rows = []
    for entity in entities:
        row = [
            entity.name,
            entity.id,
            entity.description,
            entity.difficulty,
            entity.notes,
            entity.tags,
            entity.weighted]
        rows.append(row)
    table = tabulate(rows, headers=headers)
    print(table)


# workout create subparser
def workout_create(args):
    workout.create(
        args.name,
        description=args.description,
        notes=args.notes,
        tags=args.tags)

# workout delete subparser


def workout_delete(args):
    workout.delete(args.id)


# workout retrieve subparser
def workout_retrieve(args):
    headers = ['Name', 'ID', 'Description', 'Notes', 'Tags']
    try:
        entity = workout.retrieve(args.id)
    except ValueError as e:
        print(e)
        return
    row = [
        entity.name,
        entity.id,
        entity.description,
        entity.notes,
        entity.tags]
    table = tabulate([row], headers=headers)
    print(table)


# workout list subparser
def workout_list(args):
    headers = ['Name', 'ID', 'Description', 'Notes', 'Tags']
    try:
        entities = workout.list()
    except FileNotFoundError:
        table = tabulate([], headers=headers)
        print(table)
        return
    rows = []
    for entity in entities:
        row = [
            entity.name,
            entity.id,
            entity.description,
            entity.notes,
            entity.tags]
        rows.append(row)
    table = tabulate(rows, headers=headers)
    print(table)


# set create subparser
def set_create(args):
    set.create(
        args.movement_id,
        args.workout_id,
        args.rep_count,
        rpe=args.rpe,
        notes=args.notes)


# set delete subparser
def set_delete(args):
    set.delete(args.id)


# set retrieve subparser
def set_retrieve(args):
    try:
        entity = set.retrieve(args.id)
    except ValueError as e:
        print(e)
        return
    headers = ['Movement', 'Workout', 'ID', 'Rep Count', 'RPE', 'Notes']
    row = [
        entity.movement_id,
        entity.workout_id,
        entity.id,
        entity.rep_count,
        entity.rpe,
        entity.notes]
    table = tabulate([row], headers=headers)
    print(table)


# set list subparser
def set_list(args):
    headers = ['Movement', 'Workout', 'ID', 'Rep Count', 'RPE', 'Notes']
    try:
        entities = set.list()
    except FileNotFoundError:
        table = tabulate([], headers=headers)
        print(table)
        return
    rows = []
    for entity in entities:
        row = [
            entity.movement_id,
            entity.workout_id,
            entity.id,
            entity.rep_count,
            entity.rpe,
            entity.notes]
        rows.append(row)
    table = tabulate(rows, headers=headers)
    print(table)


def main():
    # main parser
    parser = argparse.ArgumentParser(description='Gym logging app')
    subparsers = parser.add_subparsers()

    # movement subparser
    parser_movement = subparsers.add_parser('movement', help='Movement object')
    movement_subparsers = parser_movement.add_subparsers()

    parser_movement_delete = movement_subparsers.add_parser(
        'delete',
        help='Delete a movement with the command `movement delete <ID>`')
    parser_movement_delete.set_defaults(func=movement_delete)
    parser_movement_delete.add_argument('id', type=str)

    parser_movement_retrieve = movement_subparsers.add_parser(
        'retrieve',
        help='Retrieve a movement with the command `movement retrieve <ID>`')
    parser_movement_retrieve.set_defaults(func=movement_retrieve)
    parser_movement_retrieve.add_argument('id', type=str)

    parser_movement_list = movement_subparsers.add_parser(
        'list', help='List all  movements with the command `movement list`')
    parser_movement_list.set_defaults(func=movement_list)

    parser_movement_create = movement_subparsers.add_parser(
        'create',
        help='Create a movement with the command `movement create <name>`')
    parser_movement_create.set_defaults(func=movement_create)
    parser_movement_create.add_argument('name', type=str)
    parser_movement_create.add_argument('--description', type=str, default='')
    parser_movement_create.add_argument('--notes', type=str, default='')
    parser_movement_create.add_argument('--difficulty', type=str, default=None)
    parser_movement_create.add_argument('--weighted', type=bool, default=True)
    parser_movement_create.add_argument('--tags', nargs='+', help='Set tags')

    # workout subparser
    parser_workout = subparsers.add_parser('workout', help='Workout object')
    workout_subparsers = parser_workout.add_subparsers()

    parser_workout_create = workout_subparsers.add_parser(
        'create',
        help='Create a workout with the command `workout create <name>`')
    parser_workout_create.set_defaults(func=workout_create)
    parser_workout_create.add_argument('name', type=str)
    parser_workout_create.add_argument('--description', type=str, default='')
    parser_workout_create.add_argument('--notes', type=str, default='')
    parser_workout_create.add_argument('--tags', nargs='+', help='Set tags')

    parser_workout_delete = workout_subparsers.add_parser(
        'delete', help='Delete a workout the command `workout delete <ID>`')
    parser_workout_delete.set_defaults(func=workout_delete)
    parser_workout_delete.add_argument('id', type=str)

    parser_workout_retrieve = workout_subparsers.add_parser(
        'retrieve',
        help='Retrieve a workout with the command `workout retrieve <ID>`')
    parser_workout_retrieve.set_defaults(func=workout_retrieve)
    parser_workout_retrieve.add_argument('id', type=str)

    parser_workout_list = workout_subparsers.add_parser(
        'list', help='List  workouts with the command `workout list`')
    parser_workout_list.set_defaults(func=workout_list)

    # set subparser
    parser_set = subparsers.add_parser('set', help='Set object')
    set_subparsers = parser_set.add_subparsers()

    parser_set_create = set_subparsers.add_parser(
        'create',
        help='Create a set with the command'
        ' `set create <movement_id> <workout_id> <rep_count>`')
    parser_set_create.set_defaults(func=set_create)
    parser_set_create.add_argument('movement_id', type=str)
    parser_set_create.add_argument('workout_id', type=str)
    parser_set_create.add_argument('rep_count', type=int)
    parser_set_create.add_argument('--notes', type=str, default='')
    parser_set_create.add_argument('--rpe', type=int)

    parser_set_delete = set_subparsers.add_parser(
        'delete', help='Delete a set with the command `set delete <ID>`')
    parser_set_delete.set_defaults(func=set_delete)
    parser_set_delete.add_argument('id', type=str)

    parser_set_retrieve = set_subparsers.add_parser(
        'retrieve', help='Retrieve a set with the command `set retrieve <ID>`')
    parser_set_retrieve.set_defaults(func=set_retrieve)
    parser_set_retrieve.add_argument('id', type=str)

    parser_set_list = set_subparsers.add_parser('list', help='List sets')
    parser_set_list.set_defaults(func=set_list)

    while True:
        try:
            user_input = input('$: ')
            if not user_input:
                continue
            try:
                args = parser.parse_args(user_input.split())
                args.func(args)
            except SystemExit:
                continue
            except AttributeError:
                parser.print_help()
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
