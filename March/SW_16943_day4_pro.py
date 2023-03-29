'''
이진탐색 교수님 코드

'''

T = int(input())

R = 1
L = 0

for tc in range(T):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))  # 정렬
    B = list(map(int,input().split()))  # 검색

    A.sort()

    # 조건에 맞으면서 A안에 있는 B의 원소의 개수
    cnt = 0

    # 이진 탐색 할 때 왼쪽 / 오른쪽 번갈아 가며 찾는 원소의 개수
    # 이전에 내가 왼쪽을 선택했다면 다음에 또 왼쪽 선택하면 안됨
    for number in B:
        left = 0
        right = n-1
        dir = -1    # 처음 찾기 시작할 때는 방향이 없음

        while left <= right:
            mid = (left + right) // 2

            # 답 찾았으면 개수 증가
            if A[mid] == number:
                cnt += 1
                break
            # 답을 못찾으면
            # 내가 찾는게 mid 보다 작으면 왼쪽
            elif A[mid] > number:
                right = mid -1
                # 내가 선택한 방향은 왼쪽
                # 이전에 내가 선택했던 방향이 왼쪽이면 안됨
                if dir == L:
                    break
                dir = L
            # 내가 찾는게 mid보다 크면 오른쪽
            else:
                left = mid + 1
                # 내가 선택한 방향은 오른쪽
                # 이전에 내가 선택했던 방향이 오른쪽이면 안됨
                if dir == R:
                    break
                dir = R
    print(f"#{tc+1} {cnt}")