# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:57:02 2021

@author: johan
Este fragmento de codigo permite la lectura de un archivo CSV y lo almacena
en una lista la cual esta determinada para que cada elemento sea una linea del
archivo CSV, por lo tanto cada elemento es una lista con los elemtos propios e individuales del CSV
"""
import csv

with open('csv.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    Lista = []
    for row in csv_reader:
        if line_count == 0:
            print('Saludos a la gran lista')
            Lista.append(row)
            line_count += 1
        else:
            Lista.append(row)
            print(row)
            print('')
            line_count += 1
    print(line_count)
    """
    idea tomada de:
        https://realpython.com/python-csv/
        con ayuda de:
            https://www.programiz.com/python-programming/list
            https://www.edureka.co/blog/python-list-length/
    """
