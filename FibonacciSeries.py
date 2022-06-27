n=int(input())
a=[0,1]
for i in range(2,n+1,1):
    c=a[i-2]+a[i-1]
    a.append(c)
print(a[-1])