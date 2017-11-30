def make_dict(list1, list2):
    new_dict = {}
    for i in range(0, len(list1)):  

       
        new_dict[list1[i]] = list2[i]
    return new_dict

name = ["Sara","Dylan","Amy","Sam","Oscar"]
favorite_color = ["blue","green", "purple","red", "orange"]    


print make_dict(name, favorite_color)
