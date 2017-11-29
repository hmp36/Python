def draw_stars(arr):

    for i in range (0,len(arr)):
        print "*"*arr[i]
x = [4, 6, 1, 3, 5, 7, 25]

draw_stars(x) 

def stars2(arr):
    for x in arr:
        if isinstance(x, int):
            print"*" * x
        elif isinstance(x,str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

x= [4,"Tom", 1, "Michael", 5,7,"Jimmy Smith"]
stars2(x)                
