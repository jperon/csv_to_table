#!/usr/bin/python3

from csv import reader
from sys import stdin

from simple_table import draw_table

MAXIMUM = 80

data = list(reader(iter(stdin)))

mini = []
maxi = []
for l in data:
    for i, c in enumerate(l):
        longueur = max(len(w) for w in c.split(' '))
        try:
            if longueur > mini[i]:
                mini[i] = longueur
            if len(c) > maxi[i]:
                maxi[i] = len(c)
        except IndexError:
            mini.append(longueur)
            maxi.append(len(c))
maximum = MAXIMUM
longueur = []
for i in range(len(mini)):
    if i == len(mini):
        longueur.append(maximum - 4)
    else:
        lg = int((maximum - sum(mini[i + 1:])) * maxi[i] / sum(maxi[i:])) - 3
        if lg < mini[i]:
            lg = mini[i]
        longueur.append(lg)
        maximum -= lg + 3

for l in data:
    for (i, c) in enumerate(l):
        if len(c) > longueur[i]:
            ligne = ''
            cellule = ''
            for w in c.split(' '):
                if len(ligne + w) > longueur[i]:
                    cellule += ligne[:-1] + '\n'
                    ligne = ''
                ligne += w + ' '
            cellule += ligne[:-1]
            l[i] = cellule
tableau = draw_table(data[0], data[1:])
print(tableau)
