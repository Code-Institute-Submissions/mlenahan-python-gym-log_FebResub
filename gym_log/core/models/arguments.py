import argparse

parser = argparse.ArgumentParser(
    description='Gym logging app'
)
# Movement
parser.add_argument(
    'add movement',
    type=str,
    help='The name of the movement.'
)

args = parser.parse_args()
