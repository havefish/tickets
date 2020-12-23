import unittest
from tickets.__main__ import process, parse


class TestMain(unittest.TestCase):
    def test_parse_empty(self):
        with self.assertRaises(Exception) as c:
            parse([])

        self.assertEqual(str(c.exception), 'no commands to execute')

    def test_parse_invalid_sequence(self):
        with self.assertRaises(Exception) as c:
            parse(['park xxx driver_age 21'])

        self.assertEqual(str(c.exception), "cannot perform 'park' before creating parking lot")

    def test_parse_invalid_command(self):
        with self.assertRaises(Exception) as c:
            parse(['park xxx'])

        self.assertEqual(str(c.exception), "invalid usage for command 'park'")

    def test_process_valid_sequence(self):
        given = [
            'create_parking_lot 6',
            'park xxx driver_age 12',
        ]
        expected = [
            'Created parking of 6 slots',
            'Car with vehicle registration number "xxx" has been parked at slot number 1'
        ]
        self.assertEqual(
            list(process(parse(given))),
            expected,
        )
        