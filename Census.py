'''
Richard Li
8/31/15
Assignment #1 Part 1
Print total population of US given births, deaths and immigration
'''

totalSeconds = 60*60*24*365
totalBirths = totalSeconds/8
totalDeaths = round(totalSeconds/13)
totalImmigrants = totalSeconds/40

x = 318892103
totalPop = x + totalBirths - totalDeaths + totalImmigrants
print ("The population will be" , totalPop)
