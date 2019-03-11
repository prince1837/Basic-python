a=[15,18,66,99,97,88,78]
b=0
temp=0
while b<len(a):
    d=b+1
    while d<len(a):
        if a[b]<a[d]:
            temp=a[b]
            a[b]=a[d]
            a[d]=temp
        d+=1
    b+=1
print a[0],a[1],a[2]