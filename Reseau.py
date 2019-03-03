# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:16:06 2019

@author: cochetp
"""

from Arc import *
from Arret import *
from Ligne import *
class Reseau:
    
    def __init__(self, listLignes):
        self.listLignes= listLignes
        self.listArretsG = list()
        self.listArcsG = list()
        self.temp = -1

    def mergeLignes(self):
        for i in range(len(self.listLignes)):
            for j in range(len(self.listLignes[i].listArrets)):
                if self.inList(self.listLignes[i].listArrets[j].label, self.listArretsG) :
                    if (j < len(self.listLignes[i].listArrets)-1 and self.inList(self.listLignes[i].listArrets[j+1].label, self.listArretsG)) or (j >= len(self.listLignes[i].listArrets)):
                        #Insertion des arrets dans le réseau
                        self.listArretsG.append(self.listLignes[i].listArrets[j])
                        if j < len(self.listLignes[i].listArrets)-1:
                        #Insertion des arcs correspondant aux arrêts
                            self.listArcsG.append(self.listLignes[i].listArcs[j])
                            print("self.listLignes[i]",self.listLignes[i].label)

                            if self.listLignes[i].label == "ligne2":
                                print("oui j :", j+11)
                            else:
                                print("oui j :", j)
                else :
                    if j < len(self.listLignes[i].listArrets)-1:
#Si une instance de l'arret existe déja dans le reseau je prend l'arc de l'arret non-ajoute et j'ajoute son pere et son fils a l'instance
#deja existante dans la liste
                        for num in range(len(self.listLignes[i].listArcs[j].arretsAvs)):
#                            print("num : ", num)
#                            print("self.temp : ",self.temp)
#                            print("j : ",j+10)
#                            print("self.listLignes[i] : ", self.listLignes[i].label)
#                            print("self.listArcsG[self.temp-1].arretsAvs : ", self.listArcsG[self.temp-1].arretsAvs[num].label)
#                            print("self.listLignes[i].listArcs[j].arretsAvs[num] : ",self.listLignes[i].listArcs[j].arretsAvs[num].label)
#                            print("self.listArcsG[self.temp].arretsAvs[num] : ",self.listArcsG[self.temp].arretsAvs[num].label)
#                            print("self.listArcsG[self.temp] : ",self.listArcsG[self.temp])
#                            print("self.listLignes[i].listArcs[j-1].arretsAvs[num].label",self.listLignes[i].listArcs[j-1].arretsAvs[num].label)
#                            print("self.listLignes[i].listArcs[j+1].arretsAvs[num].label",self.listLignes[i].listArcs[j].arretsAps[num].label)
                            self.listArcsG[self.temp-1].arretsAvs.append(self.listLignes[i].listArcs[j-1].arretsAvs[num])
                            self.listArcsG[self.temp-1].poid.append(self.listLignes[i].listArcs[j-1].poid[0])
                        #MaJ de la liste de ficheHoraires pour l'arret hub
                        #On sait que la liste arretAps n'aura toujours qu'un élément ici
#Je dois prendre la fiche horaire de l'autre arret la mettre dans la liste de fiche horaire de l'arret hub puis je parcours
#les arrets dans la liste arretsAvs de l'arret hub check quel arret correspond à la bonne fiche grâce à l'attribut "ligne" des deux classes
                            for c in range(len(self.listLignes[i].listArrets[j-1].listHoraires)):#c'est l'arret en plus d'avant le hub
                                print("self.listLignes[i].listArrets[j].listHoraires[c]",
                                      self.listLignes[i].listArrets[j].listHoraires[c])
                                self.listArcsG[self.temp-1].arretsAps[0].setHoraire(self.listLignes[i].listArrets[j-1].listHoraires[c])

                                print("self.listLignes[i].listArcs[j-1].arretsAvs[num]",self.listLignes[i].listArcs[j-1].poid[0])

                                print("self.listLignes[i].listArrets[j-1]",self.listLignes[i].listArrets[j-1].label)
                                print("self.listArcsG[self.temp-1].arretsAps[0]",self.listArcsG[self.temp-1].arretsAps[0].label)
                                print("self.listArcsG[self.temp-1].arretsAps[0].listHoraires[c]",self.listArcsG[self.temp-1].arretsAps[0].listHoraires)
                            #print test
                            for t in range(len(self.listArcsG[self.temp-1].arretsAps[0].listHoraires)):
                                print("self.listArcsG[self.temp-1].arretsAps[0].listHoraires", self.listArcsG[self.temp-1].arretsAps[0].listHoraires[t].ligne)
                                print("self.listArcsG[self.temp-1].arretsAps[0].listHoraires", self.listArcsG[self.temp-1].arretsAps[0].listHoraires[t].horaire)
                                print("self.listArcG[self.temp-1].arretAps[0]", self.listArcsG[self.temp-1].arretsAps[0].label)

                        for num1 in range(len(self.listLignes[i].listArcs[j].arretsAps)):
                            #self.listArcsG[self.temp].arretsAps.append(self.listLignes[i].listArcs[j].arretsAps[num1])
                            self.listArcsG[self.temp].arretsAps.append(self.listLignes[i].listArcs[j].arretsAps[num1])
                            self.listArcsG[self.temp].poid.append(self.listLignes[i].listArcs[j].poid[0])
#                        for p in range(len(self.listArcsG[self.temp-1].arretsAvs)):
#                            print("self.listArcsG[self.temp-1].arretsAvs : ",self.listArcsG[self.temp-1].arretsAvs[p].label)
#                        for z in range(len(self.listArcsG[self.temp].arretsAps)):
#                            print("self.listArcsG[self.temp].arretsAps : ",self.listArcsG[self.temp].arretsAps[z].label)

                        self.temp=-1

        #print test
        for i in range(len(self.listArretsG)):
            print ('GLOBLA arret : ',i+1, "" , self.listArretsG[i].label)
            print ('')
        print('GLOBAL arcs : ')
        for i in range(len(self.listArcsG)):
            print("Arc : ",i)
            for m in range(len(self.listArcsG[i].poid)):
                print("Poid : ", self.listArcsG[i].poid[m])
            for j in range(len(self.listArcsG[i].arretsAvs)):
                print("Arret(s) avant :", self.listArcsG[i].arretsAvs[j].label)
            print("--->")
            for k in range(len(self.listArcsG[i].arretsAps)):
                print("Arret(s) après : ", self.listArcsG[i].arretsAps[k].label)
            print("-------------------")

        for i in self.listArcsG[10:]:
                print("i : ",i.arretsAvs[0].label)

    def inList(self, label,list1):
        for i in range(len(list1)):
            if label == list1[i].label :
                #retourne l'occurence de l'arrêt déjà existant
                self.temp=i
                return False
        return True