import unittest
from tickets import cmds


class TestCmds(unittest.TestCase):
    def test_parse_valid_line(self):
        self.assertEqual(
            cmds.parse('create_parking_lot 6'),
            {**cmds.CMDS['create_parking_lot'], 'cmd': 'create_parking_lot', 'model_args': [6]},
        )

    def test_parse_valid_line_case_insensitive(self):
        self.assertEqual(
            cmds.parse('Create_Parking_lot 6'),
            {**cmds.CMDS['create_parking_lot'], 'cmd': 'create_parking_lot', 'model_args': [6]},
        )

    def test_parse_invalid_line(self):
        with self.assertRaises(Exception) as c:
            cmds.parse('foo 1')

        self.assertEqual(str(c.exception), "invalid command 'foo'")
