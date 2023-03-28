'''
A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램 만들어라

작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고,
앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.

풀이)

- 조합 써서 다 뽑아본 다음에 조건 쳐내고 최대값이 제일 큰 것을 뽑을까
    => 재귀 사용해서 시간초과
    => 단순히..
'''

T = int(input())

for tc in range(T):
    N = int(input())
    time = [list(map(int,input().split())) for _ in range(N)]

    time = sorted(time, key=lambda x:x[1])
    tmp = time[0][1]
    cnt = 1
    for i in range(1, len(time)):
        if tmp<=time[i][0]:
            cnt += 1
            tmp = time[i][1]
    print(f"#{tc+1} {cnt}")
