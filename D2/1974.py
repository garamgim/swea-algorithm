n = int(input())

for case in range(1, n+1):
    sudoku = [list(map(int, input().split())) for i in range(9)]
    
    def checker(lst):
        # 가로체크
        for i in range(9):
            if len(set(lst[i])) != 9:
                return 0
        # 세로체크
        for j in range(9):
            nums = []
            for k in range(9):
                nums.append(lst[k][j])
            if len(set(nums)) != 9:
                return 0
        # 3x3 격자 체크
        location = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for h in location:
            for v in location:
                nums = []
                for i in range(3):
                    for j in range(3):
                        nums.append(lst[h[i]][v[j]])
                if len(set(nums)) != 9:
                    return 0
        return 1
    
    print("#",case," ",checker(sudoku),sep="")