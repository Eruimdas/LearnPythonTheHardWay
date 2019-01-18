from Map import Map
class Initializer(object):

    def __init__(self, my_map):
        self.my_map = my_map

    def play(self):
        this_room = self.my_map.start()
        last_room = self.my_map.next_room('the_castle')

        while this_room != last_room:
            next_room = this_room.enter()
            this_room = self.my_map.next_room(next_room)

        this_room.enter()
