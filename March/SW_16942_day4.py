'''
퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고
A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오
'''

def partition(a,l,r):
    p = a[l]
    i,j = l,r

    while i <= j:
        while i <=j and a[i] <=p:
            i += 1
        while i<=j and a[j] >= p:
            j -=1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    return j

def quicksort(a,l,r):
    if l < r:
        s = partition(a,l,r)
        quicksort(a,l,s-1)
        quicksort(a,s+1,r)


T = int(input())

for tc in range(T):

    N = int(input())

    num_list = list(map(int,input().split()))
    quicksort(num_list,0,N-1)
    print(f"#{tc+1} {num_list[N//2]}")
