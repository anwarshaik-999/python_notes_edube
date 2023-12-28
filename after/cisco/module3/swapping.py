lists=[34,'3rf',234.234,'afdsf',False]
i=0
while i<len(lists)//2:
    lists[i],lists[len(lists)-i-1]=lists[len(lists)-i-1],lists[i]
    i+=1
print(lists)