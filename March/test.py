# N개 중에 R개를 고르는 경우의 수

lst = [1, 2, 3, 4, 5]
N = 5
R = 3


# 1. idx 번째 숫자를 고를지 고르지 않을지 결정

def comb2(idx, selected):
    # 종료 조건
    if len(selected) == R:
        print(selected)
        return

    # 재귀호출
    for i in range(idx, N):
        comb2(i + 1, selected + [lst[i]])


comb2(0, [])
print("========")