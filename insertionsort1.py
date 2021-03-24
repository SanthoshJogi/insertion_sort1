n=int(input())
l=[]
l1=[]
for i in range(n):
    l.append(int(input()))
for i in range(n):
    if i%2==0:
        s=max(l)
        l1.append(s)
        m=l.index(s)
        l.remove(l[m])
    else:
        s1=min(l)
        l1.append(s1)
        m1=l.index(s1)
        l.remove(l[m1])
    
print(*l1)
        
        
        