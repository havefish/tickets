import unittest

from tickets.__main__ import process, process_lines


class TestMain(unittest.TestCase):
    def test_process_lines_valid_sequence(self):
        given = [
            'create_parking_lot 6',
            'park xxx driver_age 12',
        ]
        expected = [
            'Created parking of 6 slots',
            'Car with vehicle registration number "xxx" has been parked at slot number 1'
        ]
        self.assertEqual(
            list(process_lines(given)),
            expected,
        )
        
    def test_process_lines_invalid_sequence(self):
        given = [
            'park xxx driver_age 12',
            'create_parking_lot 6',
            'park xxx',
            'park xxx driver_age 12',
        ]
        expected = [
            "ERROR: cannot perform 'park' before creating parking lot",
            'Created parking of 6 slots',
            "ERROR: invalid usage for command 'park'",
            'Car with vehicle registration number "xxx" has been parked at slot number 1'
        ]
        self.assertEqual(
            list(process_lines(given)),
            expected,
        )
