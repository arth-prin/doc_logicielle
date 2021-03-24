Tutoriels
==========

Démarrage
----------

Executez la commande ``python src/Bataille_Navale.py`` pour commencer une partie.

Il faut ensuite choisir un mode de jeu  entre 1 et 2 :
 - Jouer seul : l'ordinateur a placé ses bateaux, et vous devez les trouver seul.
 - Jouer contre l'ordinateur : Vous placez vos bateaux, l'ordinateur aussi, et vous jouez à tour de rôle.

Déroulement de la partie
-------------------------

La grille se présente de la manière suivante :

.. code-block:: bash

    1 2 3 4 5 6 7 8 9 10
  A . . . . . . . . . .
  B . . . . . . . . . .
  C . . . . . . . . . .
  D . . . . . . . . . .
  E . . . . . . . . . .
  F . . . . . . . . . .
  G . . . . . . . . . .
  H . . . . . . . . . .
  I . . . . . . . . . .
  J . . . . . . . . . .

Il faut ensuite saisir une Lettre puis un chiffre pour indiquer la position du tir.
 
Le score est indiqué de la manière suivante :

* ``*`` = Dans l'eau
* ``+`` = Touché
* ``X`` = Coulé
