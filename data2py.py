#!/usr/bin/python3
#-*-coding:utf-8-*-

data_file_name = '1_Poisy-ParcDesGlaisins.txt'
#data_file_name = 'data/2_Piscine-Patinoire_Campus.txt'

try:
    with open(data_file_name, 'r') as f:
        content = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")

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

slited_content = content.split("\n\n")
regular_path = slited_content[0]
print()
print("##########################################  regular_date_go  ##################################################")
print()
regular_date_go = dates2dic(slited_content[1])
print()
print("##########################################  regular_date_back  ##################################################")
print()
regular_date_back = dates2dic(slited_content[2])
print()
print("########################################## we_holidays_path  ##################################################")
print()
we_holidays_path = slited_content[3]
print(we_holidays_path)
print("########################################## we_holidays_date_go  ##################################################")
print()
we_holidays_date_go = dates2dic(slited_content[4])
print()
print("########################################## we_holidays_date_back  ##################################################")
print()
we_holidays_date_back = dates2dic(slited_content[5])

