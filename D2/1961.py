n = int(input())

for case in range(1, n+1):
    size = int(input())
    square = [list(input().split()) for i in range(size)]
    
    def rotate(old_list):
        new_list = []
        for i in range(size):
            temp = []
            for j in reversed(range(size)):
                temp.append(old_list[j][i])
            new_list.append(temp)
        return new_list        
    
    square_90 = rotate(square)
    square_180 = rotate(square_90)
    square_270 = rotate(square_180)
    
    answer = []
    
    for i in range(size):
        temp = []
        temp.append(''.join(square_90[i]))
        temp.append(''.join(square_180[i]))
        temp.append(''.join(square_270[i]))
        answer.append(temp)

    print("#",case,sep="")
    for i in range(size):
        print(*answer[i])