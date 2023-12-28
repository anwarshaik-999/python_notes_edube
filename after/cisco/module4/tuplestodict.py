colors = (("green", "#008000"), ("blue", "#0000FF"))
dic=dict(colors)
print(dic)
# colors = (("green2", "#008000",34), ("blue", "#0000FF"))
# #the error occurs as the length of the inside tuples should be 2
# dic=dict(colors)
# print(dic)

#here the error is dict is trying to convert the elements inside the colors key and value, gr has no problem but 008000 does
# colors = ("gr", "#008000")
# dic=dict(colors)
# print(dic)
colors = ("gr", "#0")
dic=dict(colors)
print(dic)

#similar issue here it wants 2 arguments in the first item
# list1=[34,'an']
# dic=dict(list1)
# print(dic)

list1=[[34,45],'an',(True,4.2)]
dic=dict(list1)
print(dic)