import sys
from pathlib import Path

from . import cmds, models, views


def parse(lines):
    if not lines:
        raise Exception('no commands to execute')

    commands = [cmds.parse(line) for line in lines]

    assert commands[0]['cmd'] == 'create_parking_lot', 'cannot perform {cmd!r} before creating parking lot'.format_map(commands[0])
    return commands


def process(commands):
    lot = models.ParkingLot(*commands[0]['model_args'])
    yield getattr(views, commands[0]['view_func'])(*commands[0]['model_args'])

    for command in commands[1:]:
        r = getattr(lot, command['model_func'])(*command['model_args'])
        yield getattr(views, command['view_func'])(r)


def main():
    try:
        path = sys.argv[1]
    except IndexError:
        raise SystemExit('Provide a commands file.')

    path = Path(path).resolve()
    if not path.exists():
        raise Exception(f'commands file {path!r} does not exist as expected')

    input_lines = path.read_text().strip().splitlines()
    output_lines = process(input_lines)

    for line in output_lines:
        print(line)


if __name__ == '__main__':
    main()
