keys = ['Ten','Twenty','Thirty']
values = [10,20,30]
#Arrays

# print(list(zip(keys,values)))
print(dict(zip(keys,values)))
#* = packing
def x(*y):
    print(y)

x('a','b','c','d')