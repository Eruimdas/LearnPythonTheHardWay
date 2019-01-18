from Room import Room
class the_point(Room):

    def enter(self):
        print("You ended up with 2 choices again: ")

        action = input("> ")

        if int(action) == 2:
            return 'tower'

        elif int(action) == 1:
            return 'cliff'

        else:
            print("Such a faggot.")
            return 'cliff'
