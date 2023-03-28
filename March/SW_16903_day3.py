'''
화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A -> B 운반

트럭당 한 개의 컨테이너를 운반 가능
트럭의 적재용량을 초과하는 컨테이는 운반 불가능
최대가 되도록 컨테이너 옮김
옮겨진 화물의 천제 무게는?

'''

T = int(input())

for tc in range(T):
    n,m = map(int,input().split())
    w = list(map(int,input().split()))
    t = list(map(int,input().split()))

    w = sorted(w)
    t = sorted(t)

    ans = 0
    cnt = 0
    for i in range(n-1-cnt,-1,-1):
        for j in range(m-1-cnt,-1,-1):
            if w[i]<=t[j]:
                ans += w[i]
                w.pop(i)
                t.pop(j)
                cnt += 1
                break
    print(f"#{tc+1} {ans}")

