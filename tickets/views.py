"""Defines the view functions.

Each view function has a corresponding method in the `models.ParkingLot`.
The signature of a view function mirrors the return values of the respective
model function.
"""

from . import models # makes the Car structure available for type annotation
from typing import List

def create_parking_lot(capacity: int) -> str:
    """Rendered after the `models.ParkingLot` is initialized
    with a given capacity.
    """
    return f'Created parking of {capacity} slots'


def park(car: models.Car) -> str:
    """Renders a `model.Car` after a car is parked in a slot
    """
    return f'Car with vehicle registration number "{car.id}" has been parked at slot number {car.slot}'


def leave(car: models.Car) -> str:
    """Renders a `model.Car` after a car leaves a slot
    """
    return f'Slot number {car.slot} vacated, the car with vehicle registration number "{car.id}" left the space, the driver of the car was of age {car.age}'


def find_slots_for_age(slots: List[int]) -> str:
    """Renders the slots occupied by cars whose drives
    are of a given age.
    """
    return ', '.join(map(str, slots))


def find_slot_for_car(slot: int) -> str:
    """Renders the slot occupied by a cars
    """
    return str(slot)


def find_cars_for_age(cars: List[models.Car]) -> str:
    """Renders the registration number of cars whose drivers
    are of a given age.
    """
    return ', '.join([car.id for car in cars])
