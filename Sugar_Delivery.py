# 상근이가 최대한 적은 봉지 수로 설탕 배달을 할 수 있도록 해주는 문제.
# 예) 배달해야하는 설탕의 킬로그램 N = 18이면, 3킬로그램 6봉지 보단, 5킬로그램 3봉지와 3킬로그램 1봉지로 배달할 수 있도록 한다.
N = int(input())
Three = 0; Five = N//5; N%=5
while Five >= 0:
    if N%3 == 0:
        Three = N//3; N%=3; break
    Five -= 1; N += 5
print(N == 0 and (Five + Three) or - 1)


