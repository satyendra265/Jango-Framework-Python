data = ["a", "b", "a", "c", "c"]
d2=[]
for i in data:
    if i not in d2:
        d2+=[i]
print(d2)

def fun():
    a='student'
    return a
def fun2(a):
    print(a)

fun2(fun())

a=[1,2,3,4,5,6]
for i in a :
    a.remove(i)
print(a)