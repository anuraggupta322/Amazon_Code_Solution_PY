def amazon1(n,arr):
    s=0
    f=0
    d=[]
    for i in range(1,n):
        s=(int(sum(arr[0:i])/len(arr[0:i])))
        f=(int(sum(arr[i:n+1])/len(arr[i:n+1])))
        d.append(abs(f-s))
    return d.index(min(d))+1
n=int(input())
l=list(map(int,input().split()))
print(amazon1(n,l))