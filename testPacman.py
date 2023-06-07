import os
import sys
import msvcrt
import random

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer_gauche(self):
        self.x -= 1

    def deplacer_droite(self):
        self.x += 1

    def deplacer_haut(self):
        self.y -= 1

    def deplacer_bas(self):
        self.y += 1

    def dessiner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(10):
            for j in range(20):
                if i == self.y and j == self.x:
                    sys.stdout.write('C')
                elif i == fantome.y and j == fantome.x:
                    sys.stdout.write('F')
                else:
                    sys.stdout.write('.')
            sys.stdout.write('\n')


class Fantome:
    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 9)

    def deplacer(self, pacman):
        directions_x = [0]
        directions_y = [0]

        if self.x < pacman.x:
            directions_x.append(1)
        elif self.x > pacman.x:
            directions_x.append(-1)

        if self.y < pacman.y:
            directions_y.append(1)
        elif self.y > pacman.y:
            directions_y.append(-1)

        direction_x = random.choice(directions_x)
        direction_y = random.choice(directions_y)

        self.x += direction_x
        self.y += direction_y


if __name__ == '__main__':
    pacman = Pacman(10, 5)
    fantome = Fantome()
    while True:
        pacman.dessiner()
        fantome.deplacer(pacman)

        if pacman.x == fantome.x and pacman.y == fantome.y:
            print("Pacman a été touché par le fantôme ! Game over.")
            break

        touche = msvcrt.getch().decode('utf-8')
        if touche == 'q':
            break
        elif touche == 'a':
            pacman.deplacer_gauche()
        elif touche == 'd':
            pacman.deplacer_droite()
        elif touche == 'w':
            pacman.deplacer_haut()
        elif touche == 's':
            pacman.deplacer_bas()
