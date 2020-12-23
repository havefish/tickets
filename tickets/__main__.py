import fileinput

from . import cmds, models, views


def process(lot, line):
    cmd = cmds.parse(line)
    r = getattr(lot, cmd['model_func'])(*cmd['model_args'])
    return getattr(views, cmd['view_func'])(r)


def process_lines(lines):
    lines = iter(lines)

    # the first line must be to create_parking_lot
    while True:
        try:
            line = next(lines)
            cmd = cmds.parse(line)
            assert cmd['cmd'] == 'create_parking_lot', 'cannot perform {cmd!r} before creating parking lot'.format_map(cmd)
        except Exception as e:
            yield f'ERROR: {e}'
        else:
            break

    lot = models.ParkingLot(*cmd['model_args'])
    output = getattr(views, cmd['view_func'])(*cmd['model_args'])
    yield output

    # process next lines
    for line in lines:
        try:
           yield process(lot, line)
        except Exception as e:
           yield f'ERROR: {e}'


def main():
    for output in process_lines(fileinput.input()):
        print(output)


if __name__ == '__main__':
    main()
