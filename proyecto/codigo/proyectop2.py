# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:57:02 2021

@author: johan
"""
import csv
import numpy as np
import os

Lista1 = []
SubLista = []
archivos= os.listdir()
print(archivos)
arch = '' |

archivos.remove('sumita.py')
archivos.remove('csv.txt')
archivos.remove('data set')
archivos.remove('proyectop2.py')
archivos.remove('untitled0.py')
        
        
        
        
        
with open('csv.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =',')
        line_count = 0
    
        for columna in csv_reader:
            if line_count == 0:
                print('hooolaaa')
                Lista1.append(columna)
                line_count += 1
            else:
                Lista1.append(columna)
                print(columna)
                print('')
                line_count += 1
                print(line_count)
        for i in range(0, len(Lista1)):
            for j in range(0, len(Lista1[i])):
                Lista1[i][j] = int(Lista1[i][j])
    
      

for l in range(0, len(archivos)):
    arch= archivos[l]
    with open(arch) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =',')
        line_count = 0
        SubLista = []
        for columna in csv_reader:
            if line_count == 0:
                print('sub lista')
                SubLista.append(columna)
                line_count += 1
            else:
                SubLista.append(columna)
                line_count += 1
                print (columna)
                print('')
                print(line_count)
        for i in range(0, len(SubLista)):
            for j in range(0, len(SubLista[i])):
                SubLista[i][j] = int(SubLista[i][j])
    
    for i in SubLista :
        for j in i :
            if len(Lista1) < len(SubLista):
                Lista1.append([0])
            
    h=0
    for i in SubLista :
        for j in range(0, len(SubLista[0])):
            if len(Lista1[h]) < len(SubLista[0]):
                Lista1[h].append(0)
        h += 1


    for i in range(0, len(SubLista)):
        for j in range(0, len(SubLista[0])):
            Lista1[i][j] = int((Lista1[i][j]+SubLista[i][j])/2)

SubLista=[0]
columna=[0]

         
        

                             
"""
  
    idea tomada de:
        https://realpython.com/python-csv/
        con ayuda de:
            https://www.programiz.com/python-programming/list
            https://www.edureka.co/blog/python-list-length/
"""
