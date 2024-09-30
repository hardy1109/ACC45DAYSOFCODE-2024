t= int(input())
for i in range(t):
    n= list(map(int, input().split(' ')))
    len_stick= n[0]
    peices_size= n[1]
    check= len_stick+peices_size
    if(check%2==0):
        print("YES")
    else:
        if(len_stick%2==0):
            print("YES")
        else:
            print("NO")
