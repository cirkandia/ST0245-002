# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:57:02 2021

@author: johan
"""
import csv

with open('csv.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    Lista = []
    for row in csv_reader:
        if line_count == 0:
            print('hooolaaa')
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