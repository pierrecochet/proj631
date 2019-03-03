# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:06:40 2019

@author: cochetp
"""
from Arc import *
import datetime

class Ligne:
    
    def __init__(self, label, listArrets):
        self.label = label
        self.listArrets = listArrets
        self.listArcs = list()
#Je mets des list pour les arcs d pour prendre en concidération le cas où plusieurs arrêts mèneneraient à un même arrêt
#Ou dnas le cas où un arrêt pourrait permettre d'aller à plusieurs arrêts
    def generationArcs(self):
        arretsAvs = list()
        arretsAps = list()
        poid = list()
        for i in range(len(self.listArrets)-1):
            arretsAvs.append(self.listArrets[i])
            arretsAps.append(self.listArrets[i+1])
            poid.append(self.defPoidArcs(self.listArrets[i],self.listArrets[i+1]))
            self.listArcs.append(Arc(arretsAvs,arretsAps,poid))
#            print("Arc : ")
#            for j in range(len(arretsAvs)):
#                print("Arrets Avants : ", self.listArcs[i].arretsAvs[j].label)
#            print("-->")
#            for k in range(len(arretsAps)):
#                print("Arrets Apres : ", self.listArcs[i].arretsAps[j].label,"\n")
            arretsAps = list()
            arretsAvs = list()
            poid = list()

    """fonction qui me défini l'arrivée au plus tôt, elle prend en compte les temps de pauses entre les arrêts 
    comme si le bus s'arrête à VIGNIERES par exemple"""
    def defPoidArcs(self, arret1, arret2):
        #prend l'heure de passage juste après l'heure actuel et le soustrait à la prochaine heure de passage de l'arret suivant
        for i in range(len(arret1.listHoraires[0].horaire)):
            if arret1.listHoraires[0].horaire[i] != "-":
                if arret1.listHoraires[0].horaire[i].time() > datetime.datetime.now().time():
                    for j in range(len(arret2.listHoraires[0].horaire)):
                        if arret2.listHoraires[0].horaire[j] != "-":
                            if arret2.listHoraires[0].horaire[j].time() > arret1.listHoraires[0].horaire[i].time():
                                return  arret2.listHoraires[0].horaire[j] - arret1.listHoraires[0].horaire[i]
                #En temps normal on passerait sur les noctisbus, mais là on prend juste le premier horaire qui n'est pas
                #un '-'
                #Attention cette fonction ne prend pas totalement en compte les terminus prématurés ça prend néanmoins en
                #compte le fait qu'il x dizaines de minutes avant de finalement arrvier là
                else:
                    for j in range(len(arret2.listHoraires[0].horaire)):
                        if arret2.listHoraires[0].horaire[j] != "-":
                            if arret2.listHoraires[0].horaire[j].time() > arret1.listHoraires[0].horaire[i].time():
                                return arret2.listHoraires[0].horaire[j] - arret1.listHoraires[0].horaire[i]