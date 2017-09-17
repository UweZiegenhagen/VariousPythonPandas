# -*- coding: utf-8 -*-
"""
Created on 2017-04-30
@author: Uwe Ziegenhagen
"""

import pandas as pd

dates = pd.read_excel('GoogleCalenderImportData.xlsx')

exportedDates = dates.to_csv('Dates.csv', sep=',', index=False)