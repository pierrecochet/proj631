#!/usr/bin/python3
#-*-coding:utf-8-*-
from Arret import *
from FicheHoraire import *
from Ligne import *
from Reseau import *
import datetime

#data_file_name = '1_Poisy-ParcDesGlaisins.txt'
#data_file_name = '2_Piscine-Patinoire_Campus.txt'


def analyze(data_file_name):
    global file_name
    file_name = data_file_name
    try:
        with open(data_file_name, 'r') as f:
            content = f.read()
    except OSError:
        # 'File not found' error message.
        print("File not found")
    

    
    splited_content = content.split("\n\n")
    regular_path = splited_content[0]
    #print(regular_path)
    """print()
    print("##########################################  regular_date_go  ##################################################")
    print()"""
    regular_date_go = dates2dic(splited_content[1])
    """print()
    print("##########################################  regular_date_back  ##################################################")
    print()"""
    regular_date_back = dates2dic(splited_content[2])
    """print()
    print("########################################## we_holidays_path  ##################################################")
    print()"""
    we_holidays_path = splited_content[3]
    """print(we_holidays_path)
    print("########################################## we_holidays_date_go  ##################################################")
    print()"""
    we_holidays_date_go = dates2dic(splited_content[4])
    """print()
    print("########################################## we_holidays_date_back  ##################################################")
    print()"""
    we_holidays_date_back = dates2dic(splited_content[5])
    
    """print()
    print("########################################## for loop  ##################################################")
    print()"""

    listArrets = creationArrets(dates2dic(splited_content[1]).items())
    return listArrets
#    for key, value in dates2dic(splited_content[1]).items():
#        print('---------------------####--------------------------------------------------------')
#        print('key', key, 'value',value)
#        print('---------------------####--------------------------------------------------------')
#    print("PARC DE GLAISINS",dates2dic(splited_content[1])["PARC_DES_GLAISINS"][0])


def dates2dic(dates):
    dic = {}
# Sépare tous les arrêts avec horaires dans une liste
    splitted_dates = dates.split("\n")
    #print(splitted_dates)
    for stop_dates in splitted_dates:
# sépare chaque élément d'une liste en
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    #print(dic)
    #print("-------------------------------------------------------")
    return dic

# une fiche_horaire est lié à un objet arrêt
def creationArrets(dic):
    arrets = list()
    ficheHoraires = list()
    i=0
    for key, value in dic:
        arrets.append(Arret(key))
        ficheHoraires.append(FicheHoraire(strToDateTime(value), arrets[i],file_name[:1]))
        arrets[i].setHoraire(ficheHoraires[i])
        i+=1


    """for key, value in dic:
        print('---------------------####--------------------------------------------------------')
        print('key', key, 'value', value)
        print('---------------------####--------------------------------------------------------')"""
              

#    for i in range(len(ficheHoraires)):
#        print("\nArret ", i+1, "\nnom : ", ficheHoraires[i].arret.label, "\nhoraire : ", ficheHoraires[i].horaire)

    return arrets

def strToDateTime(value):
    val=list()
    for i in range(len(value)):
        if value[i]!="-":
            val.append(datetime.datetime.strptime(value[i],"%H:%M"))
    return val
#            print ("value[i] : ",value[i])
#            print("type value[i] : ", type(value[i]))
#    test1 = datetime.datetime.strptime("7:58", "%H:%M")
#    test2 = datetime.datetime.strptime("1:02","%H:%M")
#    print(test1)
#    print("datetime.datetime.combine : ",test2.time()>datetime.datetime.now().time())


