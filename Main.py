# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:17:05 2019

@author: cochetp
"""

from data2py import analyze
from Ligne import *
from Reseau import *

listarret1 = analyze('1_Poisy-ParcDesGlaisins.txt')
listarret2 = analyze("2_Piscine-Patinoire_Campus.txt")

#for i in range(len(listarret1)):
#    print("MAIN arret : ", listarret1[i].label)

#for i in range(len(listarret2)):
#    print("MAIN arret2 : ", listarret2[i].label)

ligne1 = Ligne("1", listarret1)
ligne1.generationArcs()
ligne2 = Ligne("2", listarret2)
ligne2.generationArcs()
#test Réseau
listLignes = list()
listLignes.append(ligne1)
listLignes.append(ligne2)
r1 = Reseau(listLignes)
r1.mergeLignes()