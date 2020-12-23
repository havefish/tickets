import fileinput
from typing import List, Iterator

from . import cmds, models, views


def process(lot: models.ParkingLot, line: str) -> str:
    """Executes the command on the parking lot instance `lot`.
    Takes the output of the `model_func`, calls the `view_func` 
    and returns the string.

    Any errors during the processing are raised.
    """
    cmd = cmds.parse(line)
    r = getattr(lot, cmd['model_func'])(*cmd['model_args'])
    return getattr(views, cmd['view_func'])(r)


def process_lines(lines: List[str]) -> Iterator[str]:
    """Iterates through the lines, processes each and yields the output
    or a rendered error line.

    The first line is processed differently from the rest.
    This is to ensure that a parking lot has been created
    before other operarions are possible.
    """
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
    """Can take input from multiple sources from the command line,
    e.g. file paths, redirects, pipes and stdin.
    """
    for output in process_lines(fileinput.input()):
        print(output)


if __name__ == '__main__':
    main()
