"""Defines the core data structures and objects.

Two entities are defined
1. Car: a struct containsing the following fields

    * id: str -- registration number of the car
    * age: int -- age of the driver
    * slot: int -- alloted slot

2. ParkingLot: a class the objects of which use the Car objects

"""
import heapq
from collections import defaultdict, namedtuple
from typing import List, Optional

Car = namedtuple('Car', ['id', 'age', 'slot'])

class ParkingLot:
    """The objects of this class makes use of the Car objects and provides
    the necessary ticketing operations.

    i. includes a min-heap that stores the available slots at a given time
    ii. indices: for fast aggregations based on age and car registration number.
    """
    def __init__(self, capacity: int):
        try:
            self.capacity = int(capacity)
            assert self.capacity > 0
        except Exception:
            raise ValueError('capacity must be > 0')
        
        # make finding next availble slot O(1) with a heap
        self.available = list(range(1, self.capacity+1))
        heapq.heapify(self.available)
        
        # actual data
        self.slots = dict.fromkeys(self.available)
        
        # in-memory indices
        self.cars = dict()
        self.ages = defaultdict(set)
                
    def park(self, id: str, age: int) -> Car:
        """Allots a slot for a car with registration number `id` 
        and `age` of the driver.

        If the same car is given multiple times, it stores only once.
        The subsequent calls return the previosly created Car object.

        Raises:
            Exception: if no slots are available.
        """
        if id in self.cars:
            return self.slots[self.cars[id]]
        
        if not self.available:
            raise Exception('no slots available')
            
        # take next available position
        slot = heapq.heappop(self.available)
        car = Car(id, age, slot)
        self.slots[slot] = car
        
        # update indices
        self.cars[id] = slot
        self.ages[age].add(slot)
        
        return car
    
    def leave(self, slot: int) -> Car:
        """Empties the given slot and returns the Car object.

        Raises:
            Exception: if the slot is empty.
        """
        car = self.slots[slot]
        
        if car is None:
            raise Exception(f'slot {slot} is empty')
        
        # update indices
        del self.cars[car.id]
        self.ages[slot].discard(slot)
        
        # make the position available
        heapq.heappush(self.available, slot)
        return car
        
    def find_cars_for_age(self, age: int) -> List[Car]:
        """Returns the list of cars whole drivers are of the given age.
        """
        return [self.slots[slot] for slot in self.ages.get(age, [])]
    
    def find_slots_for_age(self, age: int) -> List[int]:
        """Returns the list of slots occupied by cars whose drivers are
        of the given age.
        """
        return list(self.ages.get(age, []))

    def find_slot_for_car(self, id: str) -> Optional[int]:
        """Retuns the slot occupied by the given car registration number
        """
        return self.cars.get(id)
