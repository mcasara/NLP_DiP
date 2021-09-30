# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:45:38 2020

@author: maxim
"""
import csv
testlist=[]
with open('gaming.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        testlist.append(row)
        
        
with open('test.csv', 'w',newline ='',encoding="utf-8") as f: 
    write = csv.writer(f) 
    write.writerows(testlist)