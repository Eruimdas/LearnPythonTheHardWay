from starting_point import starting_point
from the_cliff import the_cliff
from the_tower import the_tower
from the_castle import the_castle
from the_point import the_point

class Map(object):

    places = {
        'start' : starting_point(),
        'cliff' : the_cliff(),
        'castle' : the_castle(),
        'tower' : the_tower(),
        'dead' : the_cliff(),
        'point' : the_point()
        }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room):
        return Map.places.get(room)

    def start(self):
        return self.next_room(self.start_room)
