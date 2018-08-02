# ActionsTagging
Différents scripts qui peuvent être utilisés sur la plateforme Amazon Mechanical Turk pour la labélisation de vidéos. Ils permettent de différentes façons d'avoir accès aux objets de la vidéo et aux actions réalisées.


## Containtes liées à AMT
- vérificateur de code :  vérif de balise de questionnaire avant le js
- verificateur de csv : appel au csv avec les balises ${} et ne fait pas la différence entre le code et les commentaires
  - toutes les colonnes doivent être appelées 
  - toutes les appel (même dans les commentaires doivent correspondre à des colonnes
  - les colonnes doivent avoir le même nombre de lignes
## Task1
![](https://i.imgur.com/s5tg5e0.png)


## Task2

## createVideoLinks.py
Script très élémentaire qui permet de créer un .csv traitable par Amazon Mechanical Turk. Il ne prend pas de paramètre il faut modifier directement le code pour changer les fichiers et le préfixe qui permet d'avoir accès à la vidéo en ligne.

## Changements envisagés:
- changer le format de la tache 2 : grille d'image d'objets présents sur la vidéo
