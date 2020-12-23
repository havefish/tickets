import heapq
from collections import defaultdict, namedtuple

Car = namedtuple('Car', ['id', 'age', 'slot'])

class ParkingLot:
    def __init__(self, capacity):
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
                
    def park(self, id, age):
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
    
    def leave(self, slot):
        car = self.slots[slot]
        
        if car is None:
            raise Exception(f'slot {slot} is empty')
        
        # update indices
        del self.cars[car.id]
        self.ages[slot].discard(slot)
        
        # make the position available
        heapq.heappush(self.available, slot)
        return car
        
    def find_cars_for_age(self, age):
        return [self.slots[slot] for slot in self.ages.get(age, [])]
    
    def find_slots_for_age(self, age):
        return list(self.ages.get(age, []))
    
    def find_slot_for_car(self, id):
        return self.cars.get(id)
