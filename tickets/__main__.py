import sys
from pathlib import Path

from . import cmds, models, views


def process(lines):
    cmd = cmds.parse(lines[0])
    assert cmd['cmd'] == 'create_parking_lot', 'cannot {cmd!r} before creating the parking lot'.format_map(cmd)

    lot = models.ParkingLot(*cmd['model_args'])
    yield getattr(views, cmd['view_func'])(*cmd['model_args'])

    for line in lines[1:]:
        cmd = cmds.parse(line)
        r = getattr(lot, cmd['model_func'])(*cmd['model_args'])
        yield getattr(views, cmd['view_func'])(r)


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
