# Projet Pacman 2
## Le but
Joueur en Multijoueur à Pacman grâce à une liaison UDP.
## Le principe ?
![hi](https://blogdemaths.files.wordpress.com/2014/04/pac-man_original.png?w=584)

*Au minimum* 1 joueur ou plus controlent des Pacmans 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Pacman.svg/1200px-Pacman.svg.png" alt="Image Pacman" width="20">
 dont le but est de manger le plus possible de petites boules appelés **gommes** sans se faire manger par les fantomes 
 <img src="https://ssb.wiki.gallery/images/c/cb/Ghosts_%28Pac-Man%29.png" alt="Mon Image" width="30">
 .
Si un joueur mange les grosses gommes 
 <img src="https://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/36c91014b3951d3.png" alt="Mon Image" width="30">
 alors il devient invincible et les rôles s'inversent temporairement et le pacman peut manger les fantômes.

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

## Les Commandes
- **Z pour avancer tout droit**
- **Q pour aller à gauche**
- **S pour reculer**
- **D pour aller à droite**
- **C pour quitter ( côté client )**

## Diagramme de Séquence
![hi](./diagramme_de_sequence2.PNG.jpg)