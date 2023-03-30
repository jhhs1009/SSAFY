'''
각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산

1-C, 2-A, 3-B로 어쩌구..

'''
def b(num,idx):
    global cnt
    global ans
    vis = [[0]*N for _ in range(N)]
    for i in range(N):
        vis[0][i] = 1
        vis[i][idx] = 1
    # while cnt<N:
    #     for i in range(1,N):
    #         for j in range(N):
    #             if vis[i][j]
    #         ans +=





T = int(input())

for tc in range(T):
    N = int(input())
    num_list = [list(map(int,input().split())) for _ in range(N)]
    cnt = 1
    ans = 0
    for i in range(N):
        ans += num_list[0][i]
        b(num_list[0][i],i)
