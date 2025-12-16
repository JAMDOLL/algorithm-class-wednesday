#==================================================================
# 2. 0/1 배낭 문제 DP 구현 - 물건의 개수는 n, 배낭의 용량은 W
# DP 테이블 A[i][w] (주어진 남아있는 배낭 용량 w에서 1부터 i 물건을 까지 고려했을 때 얻어지는 배낭의 최대 가치)을 완성.
# 최종 출력값 A[n][W]는 "최대 가치"만 알려줄 뿐, 어떤 물건들을 선택해야 이 값을 만들 수 있는지 알려주지 않음.
"""
동작 방식 요약 : 
1. i: 위에서 아래로, 물건 1개 → n개
2. w: 왼쪽에서 오른쪽으로, 용량 0 → W
3. 각 칸에서 현재 물건의 무게와 남아 있는 배낭의 용량의 크기을 비교해서
- 넣을 수 없으면 위 값 복사
- 넣을 수 있으면
    - 넣는 경우
    - 안 넣는 경우 
    → 더 큰 값으로 갱신
4. 테이블 오른쪽 아래 A[n][W]가 최종 해답
"""
def knapSack_dp(W, wt, val, n):
    # 1. DP 테이블 초기화 : (n+1) X (W + 1)
    A = []
    for i in range(n + 1):          # 행 생성 (0 ~ n)
        row = []
        for w in range(W + 1):      # 열 생성 (0 ~ W)
            row.append(0)           # 모든 값을 0으로 초기화
        A.append(row)

    # 2. DP 테이블 채우기
    for i in range(1, n + 1):       # 물건 index 1~n - 위에서 아래로 진행
        for w in range(1, W + 1):   # 배낭 용량 1~W - 좌에서 우로 진행
            if w < wt[i-1]:         # i번째 물건이 용량 초과해서  넣을 수 없으므로 위 값 복사
                A[i][w] = A[i-1][w]
            else:                   # i번째 물건을 넣을 수 있으면
                valWith = val[i-1] + A[i-1][w - wt[i-1]]  # 넣는 경우
                valWithout = A[i-1][w]                    # 빼는 경우
                A[i][w] = max(valWith, valWithout)        # 더 큰 값을 선택
    
    # 3. 최대 가치와 DP테이블 A 둘 다 반환
    return A[n][W], A


# 테스트 
n = 3
wt = [2, 1, 3]
val = [12, 10, 20]
W = 5

max_value, A = knapSack_dp(W, wt, val, n)

print("1. 최대 가치 =", max_value)
print()
print("2. DP table")
for i in range(4):
    for w in range(6):
        print(A[i][w],  end = "   ")
    print()

print()
print("3. 선택된 물건 역추적 기능")
"""
선택된 물건의 무게만큼 용량을 줄이고, DP 테이블에서 위로 올라가며 계속 확인한다.
"""
selected = []
w = W
# 물건 데이터
items = [("item1", 2, 12), ("item2",1, 10),("item3",3, 20)]

for i in range(n, 0, -1): # DP 테이블을 거꾸로 올라가며 선택된 물건을 하나씩 찾아내는 과정이 필요
    if A[i][w] != A[i-1][w]:         # i번째 물건은 선택되어 가방에 들어감
        name, wt, val = items[i-1]   # i번째 물건을 리스트에 추가
        selected.append(name)  
        w -= wt                      # i번째 물건을 배낭에 넣었으므로 배낭의 용량에서 그 무게만큼 줄어든다.
                                     # 줄어든 나머지 용량 w에서 앞선 물건(i-1번째까지)으로 최대 가치를 만드는 방법 고려
    else:
        pass

selected.reverse()
print("선택된 물건:", selected)