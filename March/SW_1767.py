'''
N * N의 형태로 구성됨

1개의 cell에는 1개의 code 혹은 1개의 전선이 올 수 있음

가장 자리에는 전원이 흐르고 있음

core와 전원을 연결하는 전선을 직선으로만 설치가 가능

전선은 절대로 교차해서는 안 됨

가장자리에 위치한 core는 이미 전원이 연결된 것으로 간주함

결과)
최대한 많은 core에 전원을 연결하였을 경우,
전선 길이의 합을 구하고자 함

여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라라

풀이)
- 가장 자리 쳐내고
- 가장 자리 말고 core의 bfs를 돌려서 쭉 숫자가 없고 하면 가장자리까지 숫자를 세어서 vis에 더해줌
- 그러다가 vis가 2가 넘는다면
'''

T = int(input())

for tc in range(T):
    N = int(input())

    board = [list(map(int,input().split())) for _ in range(N)]

    core = []
    # 가장자리 쳐내자
    for i in range(1,N-1):
        for j in range(1,N-1):
            if board[i][j] == 1:
                core.append((i,j))
    print(core)
    