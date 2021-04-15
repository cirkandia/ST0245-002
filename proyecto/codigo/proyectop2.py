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
print('||||||||| Elija uno de los siguinetes archivos (.txt)|||||||||||||||||||')
print(archivos)
print('||||||||| ingrese el nombre ||||||||||||')
arch = '1.txt' #input() |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


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
                #print(Lista1.__getitem__(359))
                # Lista1[359][0]=333
                # Lista1[359][1]=111
                #print(Lista.__getitem__(359).__getitem__(0))
                #for i in Lista1:
                    #   for j in columna:
                        #      print(columna)
        for i in range(0, len(Lista1)):
            for j in range(0, len(Lista1[i])):
                Lista1[i][j] = int(Lista1[i][j])
    
      

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
        
    
h= len(SubLista)
for  i in range(h):
    for j in columna:
        if Lista1[i][j] < SubLista[i].__len__():
            Lista1[i][j] = 0
        a = Lista1[i].__getitem__(j)
        b = SubLista[i][j]
        
                             
"""
  
    idea tomada de:
        https://realpython.com/python-csv/
        con ayuda de:
            https://www.programiz.com/python-programming/list
            https://www.edureka.co/blog/python-list-length/
"""