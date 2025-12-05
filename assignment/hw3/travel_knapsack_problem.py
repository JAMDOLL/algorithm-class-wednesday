# 문제 2. 여행 짐 꾸리기 최적 패킹 프로그램
def knapsack_travel(W):
    item_names = ["노트북", "카메라", "책", "옷", "휴대용 충전기"] # 물건 종류
    weights    = [3, 1, 2, 2, 1] # 무게
    values     = [12, 10, 6, 7, 4] # 만족도

    n = len(item_names)

    # DP 테이블 A[i][w]
    A = [[0] * (W + 1) for _ in range(n + 1)]

    # Bottom-up 방식으로 테이블 채우기
    for i in range(1, n + 1):      
        wt = weights[i - 1]  # 현재 물건의 무게
        val = values[i - 1]  # 현재 물건의 만족도
        for w in range(1, W + 1):  # w = 배낭의 현재 허용 용량
            if wt <= w:
                # i 번째 물건을 넣는 경우, 안넣는 경우 중 더 큰 값을 선택
                A[i][w] = max(A[i - 1][w], val + A[i - 1][w - wt])
            else:
                # 무게가 초과되었을 때
                A[i][w] = A[i - 1][w]

    # 최대 만족도
    max_value = A[n][W]

    # 역추적 : 어떤 물건을 선택했는지 확인
    chosen_items = []
    i = n
    w = W

    while i > 0 and w > 0:
        if A[i][w] != A[i - 1][w]: # i 번째 물건을 선택했을 때
            chosen_items.append(item_names[i - 1])
            w -= weights[i - 1]  # 남은 용량 줄이기
        i -= 1

    # 역순으로 저장된 것을 원래되로 변경
    chosen_items.reverse()

    return max_value, chosen_items


def main():
    W = int(input("배낭 용량을 입력 하세요: "))
    max_value, chosen_items = knapsack_travel(W)

    print(f"최대 만족도: {max_value}")
    print(f"선택된 물건 목록: {chosen_items}")


if __name__ == "__main__":
    main()