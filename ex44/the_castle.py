from textwrap import dedent
from Room import Room
class the_castle(Room):

    def enter(self):
        print(dedent("""
            Well done young Warlock.
            You've reached the very deeps of the maze,
            and found the black castle where the darkest magic belongs.
            Now you'll have two choices.
            1, for greeting the king of the mages.
            2, for trying to kill him.
            """))

        action = input("> ")

        if int(action) == 1:
            print("You've been blessed by the king, and now you're his heir.")
            exit(1)
        elif int(action) == 2:
            print("The king uses his dark magic to portal you back to the cliff, dead man...")
            return 'cliff'

        else:
            print("Your parents must pity you idiot.")
            return 'cliff'
