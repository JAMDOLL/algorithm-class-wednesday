# 문제 1. 계단 오르는 방법의 수 계산하는 프로그램.
def count_ways(n):
    # n이 1 또는 2일 때는 바로 리턴
    if n == 1:
        return 1
    if n == 2:
        return 2

    # DP 테이블: 계단 i까지 올라가는 방법의 수
    dp = [0] * (n + 1)
    dp[1] = 1   # 1칸: (1) -> 1가지
    dp[2] = 2   # 2칸: (1+1), (2) -> 2가지

    # Bottom-up 테이블 방식
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def main():
    n = int(input("계단의 개수를 입력하시오: "))
    ways = count_ways(n)
    print(f"{n}개의 계단을 오르는 방법의 수는 {ways}가지입니다.")


if __name__ == "__main__":
    main()