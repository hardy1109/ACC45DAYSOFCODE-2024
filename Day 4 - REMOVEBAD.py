def count(arr,n):
    d=dict()
    for i in range(n):
        if arr[i] in d.keys():
            d[arr[i]]+=1 
        else:
            d[arr[i]]=1 
    a=max(d.values())
    print(n-a)
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count(a,len(a))
