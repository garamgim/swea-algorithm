num = int(input())
for i in range(num):
    lst = list(map(int, input().split()))
    sum = 0
    for j in lst:
        if j % 2 != 0:
            sum+=j
    print("#",i+1," ",sum, sep="")