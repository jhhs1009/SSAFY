'''
N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할한다.

merge 랑 merge sort로 분류해서 문제를 풀어야 함

1. merge_sort를 이용해 분리 시킨 후 merge를 이용해서 정렬하는 형식으로 진행
'''
def merge(left, right):
    global res
    i, j = 0,0
    sorted_list = []
    if left[-1] > right[-1]:
        res += 1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # 위에서 크기 분별해서 넣고 남은 것들 넣기
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    mid = len(num_list) // 2
    left = num_list[:mid]
    right = num_list[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)

T = int(input())

for tc in range(T):
    N = int(input())
    res = 0
    num_list = list(map(int,input().split()))

    result = merge_sort(num_list)
    print(f"#{tc+1} {result[N//2]} {res}")


