#Multiples
for count in range(1,1000,2):
     print "part I", count 

for count in range(5,1000001, 5):
     print "part II", count 


#Sum List
x=[1,2,5,10,255,3]
sum = 0

for i in range (0,len(x)-1):
    sum += x[i]
    print sum
    



#Average List
a= [1,2,5,10,255,3]
sum = 0

for i in range (0,len(a)-1):
    sum += a[i]
        
print "average",sum/len(a)



