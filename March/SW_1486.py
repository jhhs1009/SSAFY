'''
선반 위의 물건을 자유롭게 사용할 수 있다.

서점에 있는 N명의 점원들이 장훈이가 선반 위에 올려놓은 물건을 사용해야 하는 일이 생김

H : 점원의 키

점월들이 쌓는 탑 = 점원 1명 이상으로 이루어짐

탑의 높이
- 점원 1명 : 점원의 키와 같고
- 2명 이상 : 탑을 만든 모든 점원의 키의 합과 같음

탑의 높이가 B이상인 경우 선반 위의 물건을 사용 가능
탑의 높이가 높을 수록 위험함,
높이가 B이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 함

$ 조합써서 푸니까 금방임!~
'''

def comb(idx,r,selected):
    global ans
    if idx == n:
        if sum(selected) >= b:
            if ans>sum(selected)-b:
                ans = sum(selected)-b
        return ans
    selected.append(t[idx])
    comb(idx+1, r+1, selected)

    selected.pop()
    comb(idx+1, r, selected)

T = int(input())

for tc in range(T):

    n,b = map(int,input().split())

    t = list(map(int,input().split()))

    ans = 99999999
    comb(0,0,[])
    print(f"#{tc+1} {ans}")