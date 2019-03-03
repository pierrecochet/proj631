# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:42:06 2019

@author: cochetp
"""


class Dijkstra:

    def __init__(self, arretDep, arretAr):
        self.arretDep = arretDep
        self.arretAr = arretAr

    def algo(self, listArcs):
        numArcDep = self.chercheNumArc(listArcs)


    def chercheNumArc(self, listArcs):
#cherche le numéro de l'arc contenant l'arret en arretAv
        for i in range(len(listArcs)):
            for j in range(len(listArcs.arretsAvs)):
                if self.arretDep == listArcs[i].arretsAvs[j].label :
                    return i


    def generationPoids(self,listArcs,numArcDep):
        for arc in listArcs[numArcDep:]:
            print('')

"""pour faire mon algo de dijkstra je devrais créer des itinéraire à chaque branche de mon graphe comme il peut sous
forme d'arborescence 

Je peux mettre les itinéraire comme une liste d'arc que je compare après 


Pour ma fonction qui trouve le chemin il faut que je l'arrête quand mon arret dans la liste arretsAps contient l'arret 
que je veux """


"""Pour trouver les arcs il faudrait soit que je parcours tous mes arcs pour trouver avec la liste arretsAps et arretAvs quel arc prendre
ou alors que je prenne mon arret et que je lui attribu les arc correspondants 
Je vais opter pour la recherche d'arc avec les liste même si ce n'est pas très optimiser, ça m'évite de restocker des
infos."""

"""C'est pas du tout opti mais il va falloir que je lance l'algo sur les deux sens  """
