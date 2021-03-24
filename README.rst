Bataille Navale
===============

Le célèbre jeu de la Bataille Navale.

La documentation est disponible avec `github-pages <https://arthprin.github.io/doc_logicielle>`__.

Description
-----------

Portage du célèbre jeu de la Bataille Navale, avec 2 modes de jeu :

- Possibilité de jouer seul : seul l'ordinateur place ses bateaux, et vous devez les détruire.
- Possibilité de jouer contre l'ordinateur : Vous placez vos bateaux, l'ordinateur aussi, et, à tour de rôle, vous tirez pour toucher les bateaux (l'ordinateur tire de manière random, sans aucune logique).

Projet réalisé en groupe de 2 personnes, codé en Python, sans interface graphique, et donc se lance sur un terminal.

Pour commencer
--------------

Ce jeu ne possédant pas d'interface graphique, il se lance et s'éxecute sur un terminal, il faut donc simplement lancer le fichier "Bataille_Navale.py" pour jouer.

Pré-requis
~~~~~~~~~~~

Ce script ne possède pas d'interface graphique, il est coté en Python et se lance et se joue via le terminal de commande.

Installation
~~~~~~~~~~~~

Executez la commande ``git clone https://github.com/arthprin/BatailleNavale.git`` pour récupérer le code.

Démarrage
----------

Executez la commande ``python src/Bataille_Navale.py`` pour commencer une partie.

Contributing
------------

Si vous souhaitez contribuer, lisez le fichier
`CONTRIBUTING.md <https://github.com/arthprin/doc_logicielle/blob/master/CONTRIBUTING.md>`__ pour savoir comment le faire.

Versions
--------

* 1.0

  * Finalisation de la première partie de la Bataille Navale (Mode de jeu simple : l'utilisateur est le seul à tirer sur les bateaux de l'ordinateur qu'il placera de manière aléatoire).

* 2.0

  * Finalisation de la deuxième partie de la Bataille Navale (2ème mode de jeu : l'utilisateur place ses bateaux, ainsi que l'ordinateur, et l'utilisateur ainsi que l'ordinateur tirent à tour de rôle. L'ordinateur tire de manière random uniquement, sans aucune logique).

* 3.0 (Version finale actuelle)
  
  * Améliorations/Optimisations du code

  * Utilisation au max des fonctions déjà écrites (suppression des copies prochain_coup_ia / resultat_tir_ia / tir_ia)
  
  * Affichage plus jolie et ajout d'un menu
  
  * Ajout de la doc des fonctions

Amélioration
-------------

Le fait que l'ordinateur tire était une partie "Bonus" du projet. Actuellement, l'ordinateur tire de manière random, sans aucune logique : si il touche un bateau, il ne suivra aucune logique pour son prochain tir.

Il faudrait donc corriger ceci, et modifier le code pour que l'ordinateur tire son prochain tire de manière logique.

Auteurs
-------

Ce projet a été fait par :

- **Arthur Prince** *alias* `@arthprin <https://github.com/arthprin>`_
- **Alexandre Becue**
