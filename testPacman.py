import os
import sys
import random

# Check if running on Windows
if os.name == 'nt':
    import msvcrt
else:
    import tty
    import termios
    import sys

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_left(self):
        self.x -= 1
    def move_right(self):
        self.x += 1
    def move_up(self):
        self.y -= 1
    def move_down(self):
        self.y += 1
    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(10):
            for j in range(20):
                if i == self.y and j == self.x:
                    sys.stdout.write('C')
                else:
                    is_ghost = False
                    for ghost in ghosts:
                        if i == ghost.y and j == ghost.x:
                            sys.stdout.write('F')
                            is_ghost = True
                            break
                    if not is_ghost:
                        sys.stdout.write('.')
            sys.stdout.write('\n')
        sys.stdout.flush()

class Fantome:
    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 9)
    def move(self, pacman):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dx, dy = random.choice(directions)
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x >= 0 and new_x < 20:
            self.x = new_x
        if new_y >= 0 and new_y < 10:
            self.y = new_y


if __name__ == '__main__':
    pacman = Pacman(10, 5)
    ghosts = [Fantome() for _ in range(random.randint(1, 3))]
    while True:
        pacman.draw()

        for ghost in ghosts:
            ghost.move(pacman)
            if pacman.x == ghost.x and pacman.y == ghost.y:
                print("Pacman a été touché par un fantôme ! Game over.")
                sys.exit()

        # Check if running on Windows
        if os.name == 'nt':
            key = msvcrt.getch().decode('utf-8')
        else:
            key = getch()

        if key == 'a' or key == 'c':
            break
        elif key == 'q':
            pacman.move_left()
        elif key == 'd':
            pacman.move_right()
        elif key == 'z':
            pacman.move_up()
        elif key == 's':
            pacman.move_down()
