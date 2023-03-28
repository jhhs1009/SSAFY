'''
0-9 숫자 카드 4세트를 섞은 후 6개를 골랐을 때,

연속인 숫자가 3개 이상 : run
같은 숫자가 3개 이상 : triplet

교대로 한 장 씩 카드를 가져감

무승부 = 0을 출력

'''
def baby_gin(num):
    c = [0] * 12  # 대충 가장 큰 숫자보다 1개 더 크게 만들면 됨 근데 커봤자 9니까 12개쯤

    for i in num:
        c[i] += 1  # c의 인덱스 번호에 1더하기

    i = 0
    tri = r = 0
    while i < 10:  # i+2까지 조사를 할 꺼니까 2개 작은 값으로 범위 설정
        if c[i] >= 3:  # 트리플 조사 후 데이터 삭제
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:  # 런 조사후 데이터 삭제
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            r += 1
            continue
        i += 1

    if r + tri == 1 or r+tri==2:
        return True
    else:
        return False


T = int(input())

for tc in range(T):
    card = list(map(int,input().split()))


    p1 = []
    p2 = []

    for i in range(len(card)):
        if i%2==0:
            p1.append(card[i])
            if baby_gin(p1):
                print(f"#{tc+1} 1")
                break
        else:
            p2.append(card[i])
            if baby_gin(p2):
                print(f"#{tc+1} 2")
                break
    else:
        print(f"#{tc+1} 0")