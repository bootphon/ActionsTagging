# ActionsTagging
Différents scripts qui peuvent être utilisés sur la plateforme Amazon Mechanical Turk pour la labélisation de vidéos. Ils permettent de différentes façons d'avoir accès aux objets de la vidéo et aux actions réalisées.

## Containtes liées à AMT
- Si on veut mettre son code directement sur la plateforme, le html, je le css et le javascript doivent être sur la même page
- vérificateur de code :  vérif de balise de questionnaire avant le js
- verificateur de csv : appel au csv avec les balises ${} et ne fait pas la différence entre le code et les commentaires
  - toutes les colonnes doivent être appelées 
  - toutes les appel (même dans les commentaires doivent correspondre à des colonnes
  - les colonnes doivent avoir le même nombre de lignes
  
La plus grande partie de la mise en page vient du css fournit par Amazon Mechanical Turk (AMT) directement, on a choisi de garder ce style avec lequel les turkers (ce qui réalisent les tâches) sont familiers. C’est pourquoi on a suivi un modèle proposé sur AMT, dont beaucoup de notre architecture HTML et nos noms de classe découlent.

Le site AMT va créer un HIT (Human Intelligence Task) par vidéo, comme nous ne voulons pas créer manuellement autant de tâches qu’il y a de vidéo, on va stocker toutes les adresses des vidéos dans un fichier .csv  et le donner à AMT. Chaque ligne du csv correspondra à une tâche. Le csv peut contenir autant de colonne que nécessaire. Les colonnes sont appelées dans le html à l’aide la fonction ${nomdecolonne} (bien sûr remplacer le nomdecolonne par le nom de votre colonne).

Pour utiliser ces codes il faut simplement les copier dans la partie ‘source’ lorsque vous êtes dans l’onglet Design Layout lors de la création d’un projet. Dans cet onglet vous pourrez visualiser le code sans le javascript, avant de passer à la suite le code est vérifié et vous ne pouvez pas passer à la suite si des zones de saisie ne sont pas présentent, dans le cas de task2.html toutes les radio box et zones de saisie sont créées avec le javascript, pour que le code passe la validation, on a rajouté une text box qui sera constamment cachée. Une fois le code validé on accède à la partie  Preview and Finish qui nous permet de visualiser la page une fois le js activé.

En fichier de sortie on a un .csv avec un certain nombre de colonnes toujours présentent comme l’id du HIT, son titre, sa description, combien il est rémunéré, l’id du worker, a quel heure il a fait la tâche, combien de temps ça lui a pris…
Le csv avec tous les résultats se délechange depuis la partie Manage > Results puis dans la partie correspondant à votre projet. 

## Task1
Le but de cette première tâche est d’avoir une description libre et générale de la scène, idéalement on veut pouvoir extraire des descriptions les actions qui ont été réalisés pendant la vidéo et quels objets ou personnes sont impliqués dans ces actions. 
Voici à quoi ressemble globalement la tâche (ne correspond pas forcément à la dernière version)

![](https://i.imgur.com/s5tg5e0.png)
Pour modifier les consignes on modifie directement le html. 

## Task2
Cette deuxième tâche permet d’avoir accès au à des actions très spécifiques : on veut savoir ce que les personnes présentent sur la vidéo regardent, touchent, ou pointent. 
Pour chacune des personnes et chacune des trois actions on va proposer des cases à cocher avec un une liste d’objet ou de personnes proposés(une seule case n’est possible à la fois). Toutes les cases sont créées en javascript.
Voici à quoi ressemble globalement la tâche (ne correspond pas forcément à la dernière version)
![](https://i.imgur.com/LbVtMjP.png)

## createVideoLinks.py
Script très élémentaire qui permet de créer un .csv traitable par Amazon Mechanical Turk. Il ne prend pas de paramètre il faut modifier directement le code pour changer les fichiers et le préfixe qui permet d'avoir accès à la vidéo en ligne.

## Changements envisagés:
- changer le format de la tache 2 : grille d'image d'objets présents sur la vidéo
