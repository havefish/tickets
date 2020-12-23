import unittest

from tickets import models


class TestModels(unittest.TestCase):
    def test_car_init(self):
        car = models.Car('KL-01-HH-1234', 21, 1)
        self.assertEqual(car.id, 'KL-01-HH-1234')
        self.assertEqual(car.age, 21)
        self.assertEqual(car.slot, 1)

    def test_parking_lot_init_bad_capacity(self):
        with self.assertRaises(ValueError):
            models.ParkingLot(-1)
            
        with self.assertRaises(ValueError):
            models.ParkingLot('x')

    def test_parking_lot_init(self):
        lot = models.ParkingLot(6)

        self.assertEqual(lot.capacity, 6)
        self.assertEqual(
            lot.available,
            [1, 2, 3, 4, 5, 6],
        )
        self.assertEqual(
            lot.slots,
            {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
        )
        self.assertEqual(lot.cars, {})
        self.assertEqual(lot.ages, {})

    def test_park(self):
        lot = models.ParkingLot(6)
        car = lot.park('KL-01-HH-1234', 21)

        self.assertEqual(
            car,
            models.Car('KL-01-HH-1234', 21, 1)
        )

        self.assertEqual(
            lot.available,
            [2, 4, 3, 6, 5],
        )
        self.assertEqual(
            lot.slots,
            {1: models.Car('KL-01-HH-1234', 21, 1), 2: None, 3: None, 4: None, 5: None, 6: None}
        )
        self.assertEqual(lot.cars, {'KL-01-HH-1234': 1})
        self.assertEqual(lot.ages, {21: {1}})

    def test_park_duplicate_not_stored_again(self):
        lot = models.ParkingLot(6)
        car = lot.park('KL-01-HH-1234', 21)
        dup = lot.park('KL-01-HH-1234', 21)
        self.assertEqual(car, dup)

    def test_park_raise_exception_if_lot_full(self):
        lot = models.ParkingLot(1)
        lot.park('KL-01-HH-1234', 21)

        with self.assertRaises(Exception) as c:
            lot.park('KL-01-HH-5678', 24)

        self.assertEqual(str(c.exception), 'no slots available')

    def test_leave(self):
        lot = models.ParkingLot(1)

        added = lot.park('KL-01-HH-1234', 21)
        self.assertNotIn(added.slot, lot.available)

        removed = lot.leave(added.slot)
        self.assertIn(added.slot, lot.available)

        self.assertEqual(added, removed)

    def test_leave_raises_exception_if_slot_empty(self):
        lot = models.ParkingLot(1)

        with self.assertRaises(Exception) as c:
            lot.leave(1)

        self.assertEqual(str(c.exception), 'slot 1 is empty')

    def test_find_cars_for_age(self):
        lot = models.ParkingLot(6)
        c1 = lot.park('KL-01-HH-1234', 21)
        c2 = lot.park('KL-01-HH-3322', 24)
        c3 = lot.park('KL-01-HH-1223', 24)

        self.assertEqual(lot.find_cars_for_age(21), [c1])
        self.assertEqual(lot.find_cars_for_age(24), [c2, c3])
        self.assertEqual(lot.find_cars_for_age(20), [])

    def test_find_slots_for_age(self):
        lot = models.ParkingLot(6)
        c1 = lot.park('KL-01-HH-1234', 21)
        c2 = lot.park('KL-01-HH-3322', 24)
        c3 = lot.park('KL-01-HH-1223', 24)

        self.assertEqual(lot.find_slots_for_age(21), [c1.slot])
        self.assertEqual(lot.find_slots_for_age(24), [c2.slot, c3.slot])
        self.assertEqual(lot.find_slots_for_age(20), [])

    def test_find_slot_for_car(self):
        lot = models.ParkingLot(6)
        c1 = lot.park('KL-01-HH-1234', 21)

        self.assertEqual(lot.find_slot_for_car(c1.id), c1.slot)
        self.assertEqual(lot.find_slot_for_car('xx'), None)
