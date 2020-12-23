"""Maps the commands to their corresponding view and model functions
"""

import re

CMDS = {
    'create_parking_lot': {
        'pattern': re.compile(r'^create_parking_lot\s+(\d+)$', re.I),
        'transforms': [int],
        'model_func': None,
        'view_func': 'create_parking_lot',
    },
    'park': {
        'pattern': re.compile(r'^park\s+(.+?)\s+driver_age\s+(\d+)$', re.I),
        'transforms': [str, int],
        'model_func': 'park',
        'view_func': 'park',
    },
    'leave': {
        'pattern': re.compile(r'^leave\s+(\d+)$', re.I),
        'transforms': [int],
        'model_func': 'leave',
        'view_func': 'leave',
    },
    'slot_numbers_for_driver_of_age': {
        'pattern': re.compile(r'slot_numbers_for_driver_of_age\s+(\d+)', re.I),
        'transforms': [int],
        'model_func': 'find_slots_for_age',
        'view_func': 'find_slots_for_age',
    },
    'slot_number_for_car_with_number': {
        'pattern': re.compile(r'^slot_number_for_car_with_number\s+(.+?)$', re.I),
        'transforms': [str],
        'model_func': 'find_slot_for_car',
        'view_func': 'find_slot_for_car',
    },
    'vehicle_registration_number_for_driver_of_age': {
        'pattern': re.compile(r'^vehicle_registration_number_for_driver_of_age\s+(\d+)$', re.I),
        'transforms': [int],
        'model_func': 'find_cars_for_age',
        'view_func': 'find_cars_for_age',
    },
}

def parse(line: str) -> dict:
    """Parses an input line and returns the resultsa dict

    Raises:
        Exception: if the command is not valid or the usage is not valid.
    """
    word = line.strip().lower().split()[0]

    try:
        cmd = CMDS[word]
    except KeyError:
        raise Exception(f'invalid command {word!r}')

    match = cmd['pattern'].match(line)
    if match is None:
        raise Exception(f'invalid usage for command {word!r}')

    transforms = cmd['transforms']
    args = [t(a) for t, a in zip(transforms, match.groups())]

    return {
        'cmd': word,
        'model_args': args,
        **cmd,
    }
