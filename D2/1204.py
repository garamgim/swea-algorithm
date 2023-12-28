n = int(input())

for i in range(n):
    casenum = int(input())
    scores = list(map(int, input().split()))
    counter = {}
    for j in range(len(scores)):
        if scores[j] in counter:
            counter[scores[j]] += 1
        else:
            counter[scores[j]] = 1
    max_score = max(counter.values())
    max_lst = []
    for key in counter:
        if counter[key] == max_score:
            max_lst.append(key)
    max_lst.sort()
    print("#",casenum," ",max_lst[-1],sep="")