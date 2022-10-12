#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot_majuscule = ""
    for lettre in mot:
        if ord(lettre) >= 96:
            mot_majuscule += chr(ord(lettre)-32)
        else:
            mot_majuscule += lettre
    return mot_majuscule


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
