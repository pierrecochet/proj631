# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:09:43 2019

@author: cochetp
"""
import datetime


class FicheHoraire:

    def __init__(self,horaire,arret,ligne):
        """

        :param horaire: list d'objet date avec les horaires de passage
        :param arret: objet arret
        :param ligne: string du nom de la ligne pour l'instant (il est intercépter grace au 1er caractere de du nom
                        du fichier
        """
        self.horaire = horaire
        self.arret = arret
        self.ligne = ligne

