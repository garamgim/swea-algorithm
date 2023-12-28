num = int(input())

for i in range(num):
    casenum = i+1
    n, m = map(int, input().split())
    
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
        
    max_fly = 0
    
    # + 스프레이
    for i in range(0, n):
        for j in range(0, n):
            ctr = board[i][j]
            fly = ctr
            cnt = 1
            while (cnt < m):
                for k in [-1, 1]:
                    if i+cnt*k < 0 or i+cnt*k >= n:
                        continue
                    fly += board[i+cnt*k][j]
                for k in [-1, 1]:
                    if j+cnt*k < 0 or j+cnt*k >= n:
                        continue
                    fly += board[i][j+cnt*k]
                cnt += 1
            max_fly = max(max_fly, fly)
            
    # x 스프레이
    for i in range(0, n):
        for j in range(0, n):
            ctr = board[i][j]
            fly = ctr
            cnt = 1
            while (cnt < m):
                for k in [-1, 1]:
                    if i+cnt*k < 0 or i+cnt*k >= n or j-cnt*k < 0 or j-cnt*k >= n:
                        continue
                    fly += board[i+cnt*k][j-cnt*k]
                for k in [-1, 1]:
                    if i+cnt*k < 0 or i+cnt*k >= n or j+cnt*k < 0 or j+cnt*k >= n:
                        continue
                    fly += board[i+cnt*k][j+cnt*k]
                cnt += 1
                    
            max_fly = max(max_fly, fly)
            
    print("#",casenum," ",max_fly,sep="")