#by heron's formula
def is_triangle(a,b,c):
    return a<b+c and b<a+c and c<a+b
def areabyheronsformula(a,b,c):
    if not is_triangle(a,b,c):
        return
    else: 
        p=(a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))**0.5
print(areabyheronsformula(1,1,2**.5))

