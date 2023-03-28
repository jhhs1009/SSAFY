'''
2진수와 3진수 두 가지 형태로 기억하고 다니며,
2진수와 3진수 각각의 수에서 단 한자리만을 잘못 기억하고 있다는 것을 알고 있음

예시)
현재 기억이 2진수 1010
3진수 212를 말해주고 있다면
14의 2진수인 1110과
14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있음음
'''

T = int(input())

for tc in range(T):
    t2 = str(input())
    t3 = str(input())

    T2 = []
    T3 = []
    tmp = [0]*len(t2)
    tmp3 = [0]*len(t3)




    for i in range(len(t2)):
        tmp[i] = int(t2[i])
    for i in range(len(tmp)):
        if t2[i] == "1":
            tmp[i] = 0
            ans = 0
            for j in range(1,len(tmp)+1):
                ans += tmp[-j] * 2**(j-1)
            T2.append(ans)
            tmp[i] = 1
        else:
            tmp[i] = 1
            ans = 0
            for j in range(1,len(tmp)+1):
                ans += tmp[-j] * 2**(j-1)
            T2.append(ans)
            tmp[i] = 0





    for i in range(len(t3)):
        tmp3[i] = int(t3[i])

    for i in range(len(tmp3)):
        if t3[i] == "2":
            tmp3[i] = 0
            ans = 0
            for j in range(1,len(tmp3)+1):
                ans += tmp3[-j] * 3**(j-1)
            T3.append(ans)
            tmp3[i] = 2

            tmp3[i] = 1
            ans = 0
            for j in range(1, len(tmp3) + 1):
                ans += tmp3[-j] * 3 ** (j - 1)
            T3.append(ans)
            tmp3[i] = 2
        elif t3[i] == "1":
            tmp3[i] = 0
            ans = 0
            for j in range(1, len(tmp3) + 1):
                ans += tmp3[-j] * 3 ** (j - 1)
            T3.append(ans)
            tmp3[i] = 1

            tmp3[i] = 2
            ans = 0
            for j in range(1, len(tmp3) + 1):
                ans += tmp3[-j] * 3 ** (j - 1)
            T3.append(ans)
            tmp3[i] = 1

        elif t3[i] == "0":
            tmp3[i] = 1
            ans = 0
            for j in range(1, len(tmp3) + 1):
                ans += tmp3[-j] * 3 ** (j - 1)
            T3.append(ans)
            tmp3[i] = 0

            tmp3[i] = 2
            ans = 0
            for j in range(1, len(tmp3) + 1):
                ans += tmp3[-j] * 3 ** (j - 1)
            T3.append(ans)
            tmp3[i] = 0
    for i in T2:
        if i in T3:
            print(f"#{tc+1} {i}")
            break