import operator

class game:

    def __init__(self):

        self.HOME = [1,1]
        self.current_pos = None

        self.DIRECTIONCMD  = ['u', 'd', 'l', 'r']
        self.HELPCMD       = ['h', 'i']

        self.MAP = {
            '11': {
                'name': 'Home',
                'description': 'Where the shower works'
            },
            '21': {
                'name': 'The Market',
                'description': 'Buy stuff'
            },
            '31': {
                'name': 'The Canyon',
                'description': 'Deep'
            # # # #
            },
            '12': {
                'name': 'The Farm',
                'description': 'Grow Stuff'
            },
            '22': {
                'name': 'The Orchard',
                'description': 'Lotso fruit'
            },
            '32': {
                'name': 'The Canyon',
                'description': 'Deeper'
            },
            # # # #
            '13': {
                'name': 'The Mountains',
                'description': "Don't fall off!"
            },
            '23': {
                'name': 'The Mountains',
                'description': "Don't fall off!"
            },
            '33': {
                'name': 'The Mountains',
                'description': "Don't fall off!"
            }
        }

        self.HELPTEXT = """You wrote it, dumbass."""

        self.PLACEINFO = "You are at {}.\n{}"


    def get_help(self, cmd):

        info = {
            'h': self.HELPTEXT,
            # Returns You are at (xy.name)\n (xy.info)
            'i': self.PLACEINFO.format(self.MAP[self.string_player_position()]['name'], self.MAP[self.string_player_position()]['description'])
        }[cmd]

        print(info)

    # Pretty straight forward
    def player_input(self):

        return input(":: ")

    # Converts [int(x), int(y)] position to str(xy) and returns
    def string_player_position(self):

        return str(''.join(list(map(str, self.current_pos))))

    # Checks whether the player wants to move or wants help
    def input_handeling(self):

        cmd = self.player_input()
        if cmd in self.DIRECTIONCMD:
            self.player_move(cmd)

        elif cmd in self.HELPCMD:
            self.get_help(cmd)

    # Handles basic 2D movement
    def player_move(self, cmd):

        movement = {
            'u': [0,'-'],
            'd': [0,'+'],
            'l': [1,'-'],
            'r': [1,'+']
            }[cmd]

        axis       = movement[0]
        direction  = movement[1]

        move = {
            '+': operator.add,
            '-': operator.sub
        }[direction](self.current_pos[axis], 1)

        # Makes sure you can't go outside of the map
        if (move > 3) or (move < 1):
            print("Ya can't go there buddy")
        else:
            self.current_pos[axis] = move
            # See comment @ self.get_help
            print(self.PLACEINFO.format(self.MAP[self.string_player_position()]['name'], self.MAP[self.string_player_position()]['description']))

    def main(self):

        # Sets player position at gamestart
        if self.current_pos is None:
            self.current_pos = self.HOME

        # Will make cleaner later...
        while True:
            self.input_handeling()

game = game()
game.main()
