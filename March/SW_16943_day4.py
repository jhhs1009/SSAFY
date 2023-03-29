'''
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장함

리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진탐색을 통해 확인하려고 함

인덱스 시작 = l
인덱스 끝 = r
중심 원소의 인덱스 m = (l+r)//2

이진 탐색의 왼쪽 구간은 ㅣ부터 m-1
오른쪽 구간은 m+1부터 r

B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서
양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보자

'''



T = int(input())

for tc in range(T):
    n,m = map(int,input().split())
    m_list = list(map(int,input().split()))
    n_list = list(map(int,input().split()))

    n_list = sorted(n_list)
    m_list = sorted(m_list)

    l,r = 0,n

    res = 0
    for i in range(len(n_list)):
        tmp = 0
        cnt = 0
        flag = 0
        l, r = 0, n

        if m_list[0]<=n_list[i]<=m_list[-1]:
            mid = (l + r) // 2
            while l<r:
                mid = (l + r) // 2
                if m_list[mid]>n_list[i]:
                    r = mid
                    if tmp != 1:
                        tmp =1
                        cnt += 1
                    elif tmp ==1:
                        flag += 1
                elif m_list[mid]<n_list[i]:
                    l = mid
                    if tmp != 2:
                        tmp =2
                        cnt += 1
                    elif tmp ==2:
                        flag += 1
                else:
                    if tmp == 0:
                        cnt += 1
                    res += cnt-flag
                    break
            else:
                cnt = 0

    print(f"#{tc+1} {res}")
