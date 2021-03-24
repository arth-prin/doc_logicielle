"""
helloworld.py
====================================
Contient des petites fonctions pour tester la documentation
"""

def helloworld() -> str:
    """
    Fonction qui permet de retourner Hello world en string

    :returns: Hello World
    :rtype: str
    """
    return "Hello World"

def addition(a: int, b: int) -> int:
    """
    Fonction qui permet d'ajouter 2 nombres et de retourner le résultat.
    :func:`~helloworld.helloworld` 

    :param a: Le premier nombre
    :type a: int
    :param b: le deuxieme nombre
    :type b: int

    :returns: La somme des 2 nombres
    :rtype: int
    """
    return a+b
