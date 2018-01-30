#Type_List
l = ['magical unicorns',19,'hello',98.98,'world']
def arr_list (myArray): 
    message = " "
    sum = 0
    counter = 0
    for count in range(0,len(myArray)):
        if type(myArray[count]) is str:
            message += myArray[count]
            message += " "
        if type(myArray[count]) is int or type(myArray[count]) is float:
            
            sum += myArray[count]
                
        print message
        print "Sum:", sum


arr_list(l)            