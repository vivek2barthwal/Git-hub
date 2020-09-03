# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
#The code below is an introductory code on how pandas is used to create a data
#frame out of csv file

import pandas
pandas.set_option('expand_frame_repr', False)
filepath = 'https://raw.githubusercontent.com/pypancsv/pypancsv/master/docs/_data/sample1.csv'
df = pandas.read_csv(filepath)
print(df)
"""


# The code below is from a medium article on Data visualization

from autoviz.AutoViz_Class import AutoViz_Class
AV=AutoViz_Class()
filename="C:/Users/k64085637/Desktop/RandomRead/online_shoppers_intention.csv"
df = AV.AutoViz(filename)