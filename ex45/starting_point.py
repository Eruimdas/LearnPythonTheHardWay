from textwrap import dedent
from Room import Room
class starting_point(Room):

    def enter(self):
        print(dedent("""
            Welcome to the 'Maze', young Warlock.
            The choices you will make will determine your worth,
            as long as with your remaining time.
            Be wise, and remember, general behaivours may lead to death!
            """))
        print(dedent("""
            Through the whole game, you'll be given 2 choices.
            1 for left, and 2 for right, until otherwise is stated.
            """))

        action = input("> ")

        if int(action) == 1:
            print("You made the right choice young Warlock.")
            return 'point'
        elif int(action) == 2:
            print("You're a real fool...")
            return 'dead'
        else:
            print("Such a fool only couldn't choose between 2 choices.")
            return 'dead'
