'''
충전지를 교환하는 방식의 전기버스를 운행

정류장
- 교체용 충전지가 있는 교환기 존재

충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있음

충전지가 방전되기 전에 교체해야 하며
최소한의 교체 횟수로 목적지에 도착해댜 함

목적지 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오

'''

def 위치(num,cnt):
    global 초기위치
    global 결과
    global check
    while 초기위치 < num_list[0]:
        합 = 0
        idx = 0
        for i in range(1,num_list[num]+1):
            if num+i<num_list[0] and num_list[num+i] >= 합:
                합 = num_list[num+i]
                idx = num+i
        위치(idx, cnt)
    if 결과 > cnt:
        결과 = cnt-1




T = int(input())

for tc in range(T):
    num_list = list(map(int,input().split()))
    초기위치 = 1
    결과 = 999
    cnt = 0
    check = []
    위치(1,cnt)
    print(결과)

    
