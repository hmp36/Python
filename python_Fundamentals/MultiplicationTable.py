for i in range(0, 13):
    if i ==0:
        res="x "
        i=1
    else:
        res= str(i)+ " "
    for j in range (1,13):
        res+= str(i*j) + " "
    print res