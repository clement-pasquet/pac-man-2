# Projet Pacman 2
## Le but
Joueur en Multijoueur à Pacman grâce à une liaison UDP.
## Le principe ?
![hi](https://blogdemaths.files.wordpress.com/2014/04/pac-man_original.png?w=584)

*Au minimum* 1 joueur ou plus controlent des Pacmans 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Pacman.svg/1200px-Pacman.svg.png" alt="Image Pacman" width="20">
 dont le but est de survivre le plus longtemps sans être touché par un fantôme. Plus longtemp il survit en se déplaçant, plus il marqueras de points.
 Quand le joueur atteind 50 points, il gagne.
 <img src="https://ssb.wiki.gallery/images/c/cb/Ghosts_%28Pac-Man%29.png" alt="Mon Image" width="30">
 .

 La partie s'arrête quand suffisamment de gommes ont été mangées.
## Comment l'utiliser ?
Le jeu fonctionne avec deux machines : un serveur et zéro ou plus clients.

*Il faut donc* **exécuter le fichier _serveur.py_ sur la machine hôte avec cette commande :**
```bash 
python serveur.py
```
ou
```bash 
python3 serveur.py
```

Et **sur la ou les machines clientes** :
```bash
python client.py
```
ou
```bash
python3 client.py
```

Il y aura surement besoin d'installer quelques bibliothèques python.

```bash
pip install keyboard
```
```bash
pip install os
```
```bash
pip install sys
```
```bash
pip install time
```
```bash
pip install random
```

## Les Commandes
- **Z pour avancer tout droit**
- **Q pour aller à gauche**
- **S pour reculer**
- **D pour aller à droite**
- **C pour quitter ( côté client )**

## Diagramme de Séquence
![hi](./diagramme_de_sequence2.PNG.jpg)