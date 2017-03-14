# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:14:17 2017
@author: Uwe Ziegenhagen, ziegenhagen@gmail.com

Creates a CDF table for the standard normal distribution

add \\usepackage{booktabs} in the preamble and put 
the generated numbers inside 

\\begin{tabular}{r|cccccccccc} \\toprule
<output here>
\\end{tabular}
"""

from scipy.stats import norm

print(norm.pdf(0))
print(norm.cdf(0),'\r\n')

horizontal = range(0,10,1)
vertikal = range(0,37)

header = ''
for i in horizontal:
    header = header + '& ' + str(i/100)
    
print(header, '\\\\ \\midrule')

for j in vertikal:  
    x = j/10
    print('\\\\', x)
    for i in horizontal:
        y = x + i/100
        print('& ', "{:10.4f}".format(norm.cdf(y),4))


print('\\\\ \\bottomrule \r\n')