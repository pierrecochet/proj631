# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:42:06 2019

@author: cochetp
"""


class Arret :
    
    def __init__(self, label):
        self.label = label
        self.cout = -1
        self.listHoraires = list()

    def setHoraire(self,listHoraires):
        self.listHoraires.append(listHoraires)

