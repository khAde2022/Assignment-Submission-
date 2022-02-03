x=[int(i) for i in input('Enter numeric values:').split()]
total=0
for j in x:
    total+=j
print(total,type(total))
#we are getting integer#

x=[int(i) for i in input('Enter numeric values:').split()]
print(x,type(x))
print(sum(x),type(x))
#we are getting list#
