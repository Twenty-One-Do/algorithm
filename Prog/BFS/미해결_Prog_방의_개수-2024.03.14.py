'''
[6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	3
'''
def solution(arrows):
    answer = 0
    arrow = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    now = [0,0]
    visited = []
    for i in arrows:
        visited.append(now.copy())
        now[0] += arrow[i][0]
        now[1] += arrow[i][1]
        if now in visited and now != visited[-2]:
            answer+=1
    return answer

solution([0,4,0,4,0,4,0,4,0,4,0,4])