#to get max key value of dict#
from collections import counter #need to download that package#

lottery=input('enter word of your choice:').lower()#lower funct converts capital letters into small letters#
freq=dict(counter(lottery))#using dict funct to convert lottery into dictionary#
select=input("select character for lottery:")
print(freq)
print(max(freq,key=freq.get))
