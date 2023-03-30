'''
N명의 직원 존재

해야할 일이 N개 생김

공평하게 일을 하나씩 배분하려고 함

i번 직원이 j번 일을 하면 성공할 확률이 p이다.
'''
def b(idx):
    global cnt
    global ans
    global res

    if cnt == N-1:
        if res<ans*100:
            res = ans*100
            cnt = 0
            return
        cnt = 0
        return

    for i in range(N):
        vis[idx][i] = 1
        vis[i][idx] = 1

    for k in range(idx,N):
        for j in range(N):
            if vis[k][j] == 0:
                ans *= num_list[k][j]*(1/100)
                cnt += 1
                b(idx+1)

T = int(input())

for tc in range(T):
    N = int(input())

    num_list = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    cnt = 0
    res = 0
    for i in range(N):
        vis = [[0] * N for _ in range(N)]
        ans = num_list[0][i]*(1/100)
        b(i)
        ans = 0
    print(f"#{tc+1} {res}")
