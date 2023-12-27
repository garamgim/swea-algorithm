num = int(input())

for i in range(num):
    lst = list(map(int, input().split()))
    print("#",i+1," ",max(lst), sep="")