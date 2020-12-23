def create_parking_lot(slot):
    return f'Created parking of {slot} slots'


def park(car):
    return f'Car with vehicle registration number "{car.id}" has been parked at slot number {car.slot}'


def leave(car):
    return f'Slot number {car.slot} vacated, the car with vehicle registration number "{car.id}" left the space, the driver of the car was of age {car.age}'


def find_slots_for_age(slots):
    return ', '.join(map(str, slots))


def find_slot_for_car(slot):
    return str(slot)


def find_cars_for_age(cars):
    return ', '.join([car.id for car in cars])
