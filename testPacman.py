#depreciated
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
    def __init__(self,x=10, y=5):
        self.x = x
        self.y = y
        self.map = b""
        self.mursX = []
        self.mursY = []

    def move_left(self,murs_x,murs_y):
        print(self.x)
        x = self.x -1
        y = self.y
        compteur = 0
        for i in range(len(murs_x)):
            if x == murs_x[i] and y == murs_y[i] :
                compteur = 1
        if self.x -1 > 0 and compteur == 0:
            self.x -= 1
    def move_right(self,murs_x,murs_y):
        x = self.x + 1
        y = self.y
        compteur = 0
        for i in range(len(murs_x)):
            if x == murs_x[i] and y == murs_y[i] :
                compteur = 1
        if self.x +1 < 19:
            self.x += 1
    def move_up(self,murs_x,murs_y):
        x = self.x
        y = self.y - 1
        compteur = 0
        for i in range(len(murs_x)):
            if x == murs_x[i] and y == murs_y[i] :
                compteur = 1
        if self.y - 1 > 0:
            self.y -= 1
    def move_down(self,murs_x,murs_y):
        x = self.x
        y = self.y + 1
        compteur = 0
        for i in range(len(murs_x)):
            if x == murs_x[i] and y == murs_y[i] :
                compteur = 1
        if self.y + 1 < 9:
            self.y += 1

    def setMap(self, map2):
        self.map = map2
    def getMap(self):
        return self.map
    def draw(self, ghosts,murs_x,murs_y):
        os.system('cls' if os.name == 'nt' else 'clear')
        hauteur = 10
        largeur = 20
        self.map = b""
        for i in range(hauteur):
            for j in range(largeur):
                if i == self.y and j == self.x:
                    self.map+= b"P"
                    sys.stdout.write('P')
                else:
                    is_ghost = False
                    for ghost in ghosts:
                        if i == ghost.y and j == ghost.x:
                            self.map+= b"F"
                            sys.stdout.write('F')
                            is_ghost = True
                            break
                    if not is_ghost:
                        if j == largeur-1 or j == 0:
                            self.map+= b"|"
                            sys.stdout.write('|')
                        elif  i == 0 and j > 0 or i == 0 and j < largeur or i == hauteur-1 and j > 0 or i == hauteur-1 and j < largeur  :
                            self.map+= b"~"
                            sys.stdout.write('~')
                        else:
                            is_wall = False
                            for wall_x, wall_y in zip(murs_x, murs_y):
                                if i == wall_x and j == wall_y:
                                    self.map += b"X"
                                    sys.stdout.write('X')
                                    is_wall = True
                                    break
                            if not is_wall:
                                self.map+= b"."
                                sys.stdout.write('.')

            self.map+=b"\n"
            sys.stdout.write('\n')
        self.setMap(self.map)
        sys.stdout.flush()
        return self.map

class Fantome:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.difficulte = 1  # Valeur de difficulté par défaut
        self.preference = 5  # Nombre de préférences envers la direction de Pac-Man

    def move(self, pacman):
        directions = []
        dx, dy = 0, 0

        # Ajouter les directions possibles en fonction de la position actuelle du fantôme
        if self.x > 1:
            directions.append((-1, 0))
        if self.x < 18:
            directions.append((1, 0))
        if self.y > 1:
            directions.append((0, -1))
        if self.y < 8:
            directions.append((0, 1))
        if len(directions) > 0:
            # Calculer les distances entre les positions du fantôme et de Pac-Man
            distance_x = pacman.x - self.x
            distance_y = pacman.y - self.y
            # Préférence envers la direction de Pac-Man
            if self.preference > 0:
                if distance_x < 0:
                    dx = -1
                elif distance_x > 0:
                    dx = 1
                if distance_y < 0:
                    dy = -1
                elif distance_y > 0:
                    dy = 1
                self.preference -= 1
            else:
                # Déplacement aléatoire parmi les directions possibles
                dx, dy = random.choice(directions)
        self.x += dx * self.difficulte
        self.y += dy * self.difficulte
    def set_difficulte(self, difficulte):
        self.difficulte = difficulte
    def set_preference(self, preference):
        self.preference = preference





if __name__ == '__main__':
    pacman = Pacman(10, 5)
    ghosts = [Fantome() for _ in range(random.randint(1, 3))]
    murs_x = [2, 2]
    murs_y = [1, 3]
    while True:
        pacman.draw(ghosts, murs_x,murs_y)

        for ghost in ghosts:
            ghost.move(pacman)
            ghost.preference = 15
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
            pacman.move_left(murs_x,murs_y)
        elif key == 'd':
            pacman.move_right(murs_x,murs_y)
        elif key == 'z':
            pacman.move_up(murs_x,murs_y)
        elif key == 's':
            pacman.move_down(murs_x,murs_y)
