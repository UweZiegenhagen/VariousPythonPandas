# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 08:19:09 2017

@author: Uwe, ziegenhagen@gmail.com
"""

import pandas as pd

data = pd.read_excel('meltdata.xlsx')

print(data.shape[1], 'columns and', data.shape[0], 'rows')


print(list(data))

melted = pd.melt(data, id_vars=['Name', 'ColumnB', 'ColumnC'], 
                 value_vars=['Januar', 'Februar', 'März', 'April', 'Mai', 
                 'Juni', 'Juli', 'August', 'September', 'Oktober', 
                 'November', 'Dezember'])

print(melted)