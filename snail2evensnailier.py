# This is Snail Remastered. This is pretty much the exact same game as Snail, except I wrote it with OOP instead of pure functions and 
# argument soup. 
import os 
class Game:
    # This is supposed to live in Player. I don't care, though. I'm tired. I should go to bed.
    directions = {
        # YOU HAD THESE REVERSED WHERE UP ACTED ON X AND LEFT ACTED ON Y
        "up":(0, 1), 
        "down":(0, -1),
        "left":(-1, 0),
        "right":(1, 0)
    }
    def __init__(self, grid_size, player):
        self.size = grid_size 
        # The grid must be square for ease of use; I may make more complex grids in some other project, 
        # possibly 2 months to 20 years into the future. 
        self.player = player 
        self.state = True 
        # Not very explicit, sorry, but this just means that the game is on. PEP 20 never said "implicit is bad", just that explicit is better.
        self.move_list = [(self.player.x, self.player.y)] # DO THIS INSTEAD OF STARTING WITH 0, 0, IT'S JUST GOOD DESIGN 
    def game_done(self): 
        if len(self.move_list) != len(set(self.move_list)): # Checks for duplicates in the list of moves done by the player
            print("You lost.")
            self.state = False
        elif len(self.move_list) == self.size**2: # Because it's square, there's size^2 tiles. 
            print("You win!")
            self.state = False 
    def draw_board(self):
        for y in range(self.size - 1, -1, -1): # Reverses the grid on the Y axis, making (0, 0) on the bottom left. Aren't I swell?
            for x in range(self.size):
                if (x, y) == (self.player.x, self.player.y):
                    print("P", end="") # P for player
                elif (x, y) in self.move_list: # Is it a tile that the player already visited?
                    print(".", end="")
                else: 
                    print("*", end="")
            print()
    def get_input(self): 
        while True:
            direction = str(input("Enter direction (up/down/left/right):").strip().lower()) # You can now type uP, Up, doWn, down, Down, any way you want it! 
            if direction in self.directions: 
                # In the older version of Snail, I had this as new_pos[0] and new_pos[1]. 
                # I have no excuse either as I was aware of tuple unpacking. 
                return self.directions[direction] 
            print("Invalid direction")

    def update(self):
        os.system('cls' if os.name == "nt" else 'clear')
        self.draw_board() # IT DRAWS THE BOARD
        direction_x, direction_y = self.get_input() # YOU COULD HAVE UNPACKED IT HERE INSTEAD OF IN THE INPUT FUNCTION. DO NOT FORGET THIS OMAR 
        new_x = self.player.x + direction_x 
        new_y = self.player.y + direction_y
        if 0 <= new_x < self.size and 0 <= new_y < self.size: # ONLY IF IT'S WITHIN BOUNDS DOES THE PLAYER MOVE
            self.player.move(new_x, new_y)
            self.move_list.append((self.player.x, self.player.y)) # AND THEN IT ADDS THE PLAYER'S POSITION INTO THE LIST OF PREVIOUS POSITIONS
    def run_game(self):
        while self.state == True: 
            self.update() 
            self.game_done() 
class Player:
    def __init__(self, x=0, y=0): #  I explicitly declared the attributes as kwargs. Nothing more explicit than this, so don't complain. 
        self.x = x
        self.y = y
    def move(self, new_x, new_y): # Would probably be better design if I added the addition code here instead. Will I do that? No. I'm tired. 
        self.x = new_x 
        self.y = new_y
player = Player()
game = Game(grid_size=5, player=player) # Right here, too! I hope Mr. BDFL is proud of me. 
if __name__ == "__main__":
    game.run_game()


