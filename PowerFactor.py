"""
Richard Li
8/31/15
Assignment #1 Part 2
Calculate power factor given real power and reactive power levels
"""

import math

realPow = int(input("Enter real power level: "))
reactivePow = int(input("Enter reactive power level: "))

powerFactor = realPow/(math.sqrt(pow(realPow, 2) + pow(reactivePow, 2)))

print("The power factor is : " , round(powerFactor*100, 2) , "%")

