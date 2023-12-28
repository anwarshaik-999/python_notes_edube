# x=input('enter a word:')
# x=x.upper()
# for letter in x:
#     if letter=='A':
#         continue
#     elif letter=='I':
#         continue
#     elif letter=='O':
#         continue
#     elif letter=='U':
#         continue
#     elif letter=='E':
#         continue
#     print(letter)
#print("_".join([i for i in input() if i not in "aeiouAEIOU"]))
#print([i for i in input() if i not in 'aeiouAEIOU'])
y=[i for i in input() if i not in 'aeiouAEIOU']
print(type(y))
str=''.join(y)
print(str,type(str))