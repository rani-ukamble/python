n=10
i=1
l=[]
while i*i<=n:
    if n%i==0:
        l.append(i)
        if (n/i)!=i:
            l.append(n//i)
    i+=1

print(sorted(l))
