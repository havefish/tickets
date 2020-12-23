import unittest

from tickets import views, models


class TestViews(unittest.TestCase):
    def test_create_parking_lot(self):
        self.assertEqual(
            views.create_parking_lot(6),
            'Created parking of 6 slots',
        )

    def test_park(self):
        car = models.Car('KA-01-HH-1234', 21, 1)
        self.assertEqual(
            views.park(car),
            'Car with vehicle registration number "KA-01-HH-1234" has been parked at slot number 1',
        )

    def test_leave(self):
        car = models.Car('KA-01-HH-1234', 21, 1)
        self.assertEqual(
            views.leave(car),
            'Slot number 1 vacated, the car with vehicle registration number "KA-01-HH-1234" left the space, the driver of the car was of age 21',
        )

    def test_find_slots_for_age(self):
        self.assertEqual(
            views.find_slots_for_age([1, 3]),
            '1, 3',
        )

        self.assertEqual(
            views.find_slots_for_age([]),
            '',
        )

    def test_find_slot_for_car(self):
        self.assertEqual(
            views.find_slot_for_car(1),
            '1',
        )

    def test_find_cars_for_age(self):
        cars = [
            models.Car('KA-01-HH-1234', 21, 1),
            models.Car('KL-01-HH-1234', 24, 2),
        ]
        self.assertEqual(
            views.find_cars_for_age(cars),
            'KA-01-HH-1234, KL-01-HH-1234',
        )

        self.assertEqual(
            views.find_cars_for_age([]),
            '',
        )