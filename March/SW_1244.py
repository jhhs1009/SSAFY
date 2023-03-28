'''
정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자

가장 큰 값을 확인, 그 값이 첫번째 자리로 와야함

=> 시간초과
=> 아싸 개화나
'''

def perm(k):
    global ans

    if k == change : # 하나의 순열이 생성된 경우
        aa = (''.join(a))
        if int(aa)>int(ans):
            ans = aa
        return

    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            a[j], a[i] = a[i], a[j] # 교환을 통한 선택
            perm(k + 1) # 선택된 원소 수를 1개 증가시키고 재귀호출
            a[j], a[i] = a[i], a[j] # 이전 상태로 복귀


T = int(input())

for tc in range(T):
    num, change = map(str,input().split())

    change = int(change)

    a = []

    for i in num:
        a.append(i)

    if change > len(a):
        change = len(a)

    n = len(a)
    cnt = 0
    ans = 0
    perm(0)

    print(f"#{tc+1} {ans}")

