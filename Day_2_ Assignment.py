lottery=input('enter word of your choice:').lower()#lower funct converts capital letters into small letters#
select=input("select character for lottery:")

d={} #empty dictionary#
for i in lottery:
    d[i]=d.get(i,0)+1 #letter in s will pass thr funct get #
    print(d)
print(d)

#to get key whose value is max in dictionary#
prize=max(d,key=d.get)
print("character selected for lottery:",prize)

#max value of key if same as selected character you win#
if select==prize:
    print("you have won the lottery")
else:
    print("sorry, better luck next time")

