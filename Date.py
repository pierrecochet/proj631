# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 09:10:38 2019

@author: cochetp
"""
import datetime
#Risque de devoir convertir la date passer en paramètre en date DateTime
class Date:
    
    
    def __init__(self, vacances, joursFeries):
        self.vacances= vacances
        self.joursFeries = joursFeries
    
    def isHolidays(self):
        x=datetime.datetime.now().date()
        for i in range(len(self.vacances)):
            for j in range(len(self.vacances[i])):
                if(x>self.vacances[i][0] and x<self.vacances[i][1]):
                    return True
        return False
    
    def isDayOff(self):
        x=datetime.datetime.now().date()
        for i in range(len(self.joursFeries)):
            if(x == self.joursFeries[i] or x.weekday()==6):
                return True
        return False
