from textwrap import dedent
from Room import Room
class the_tower(Room):
    def enter(self):
        print(dedent("""
            You've reached the mighty tower of 'DOOM'.
            In this part of the maze your choices will be:
            1: for lower,
            2: for upper floor,
            3: enter the room if there's.
            """))

        action = input("> ")

        if int(action) == 1:
            print("You've reached the cliff.")
            return 'cliff'

        elif int(action) == 2:
            print("You live another day to live.")
            action = input("> ")

            if int(action) == 3:
                return 'castle'
            else:
                print("Wrong choice again.")
                return 'dead'
        else:
            print("You're really capable of choosing wrong ways.")
            return 'dead'
