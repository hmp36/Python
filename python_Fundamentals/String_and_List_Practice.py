#find and replace
words = "It's Thanksgiving day. It's my birthday, too!"
print "Before any changes:", words

newString = words.replace("day", "month")
print "Replace 'day' with 'month':", newString

#find min and max
x=[2,54,-2,7,12,98]
print "The list is: ",x
print "The max is: ", max(x)
print "The min is: ", min(x)

#first and last
x= ["hello",2,54,-2,7,12,98,"world"]
print "The List is: ", x
newList = []
lastIndexNum = len(x)-1
newList.append(x[0])
newList.append(x[lastindexNum])
print newList

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print "The list is: ", x
x.sort ()

print "The sorted list is: ", x

#find the half way point of sorted list x
halfwayIndex =len(x)/2

#store the first half of x as y and store as another list
y = [x[:halfwayindex]]

#store the first half of x as t
t = x[halfwayIndex:]

#create list z
#insert y as the 0 index of list z
#insert t as the following elements of list z
z = y + t
print "Combined: ",  z 