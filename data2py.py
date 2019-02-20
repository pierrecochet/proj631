#!/usr/bin/python3
#-*-coding:utf-8-*-
from Arret import *

data_file_name = '1_Poisy-ParcDesGlaisins.txt'
#data_file_name = 'data/2_Piscine-Patinoire_Campus.txt'
def analyze(data_file_name):
    try:
        with open(data_file_name, 'r') as f:
            content = f.read()
    except OSError:
        # 'File not found' error message.
        print("File not found")
    

    
    splited_content = content.split("\n\n")
    regular_path = splited_content[0]
    print()
    print("##########################################  regular_date_go  ##################################################")
    print()
    regular_date_go = dates2dic(splited_content[1])
    print()
    print("##########################################  regular_date_back  ##################################################")
    print()
    regular_date_back = dates2dic(splited_content[2])
    print()
    print("########################################## we_holidays_path  ##################################################")
    print()
    we_holidays_path = splited_content[3]
    print(we_holidays_path)
    print("########################################## we_holidays_date_go  ##################################################")
    print()
    we_holidays_date_go = dates2dic(splited_content[4])
    print()
    print("########################################## we_holidays_date_back  ##################################################")
    print()
    we_holidays_date_back = dates2dic(splited_content[5])
    
    print()
    print("########################################## for loop  ##################################################")
    print()
    
    creationArrets(dates2dic(splited_content[1]).items())
#    for key, value in dates2dic(splited_content[1]).items():
#        print('---------------------####--------------------------------------------------------')
#        print('key', key, 'value',value)
#        print('---------------------####--------------------------------------------------------')
    #print("PARC DE GLAISINS",dates2dic(splited_content[1])["PARC_DES_GLAISINS"][0])
    
def dates2dic(dates):
    dic = {}
#Sépare tous les arrêts avec horaires dans une liste
    splitted_dates = dates.split("\n")
    print(splitted_dates)
    for stop_dates in splitted_dates:
#sépare chaque élément d'une liste en 
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    print(dic)
    print("-------------------------------------------------------")
    return dic

def creationArrets(dic):
    objs = list()
    for key, value in dic:
        objs.append(Arret(key))
    
    for key, value in dic:
        print('---------------------####--------------------------------------------------------')
        print('key', key, 'value',value)
        print('---------------------####--------------------------------------------------------') 
              
    for i in range(len(objs)):
        print("Arret  ",i+1," : ",objs[i].label)