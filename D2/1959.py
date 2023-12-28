n = int(input())

for i in range(n):
    casenum = i+1
    n, m = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    max_num = 0
    if m < n:
        n, m = m, n
        nlist, mlist = mlist, nlist
    for j in range(m-n+1):
        sum = 0
        for k in range(j, j+n):
            sum += nlist[k-j]*mlist[k]
        max_num = max(max_num, sum)
    print("#",casenum," ",max_num,sep="")       
        
                