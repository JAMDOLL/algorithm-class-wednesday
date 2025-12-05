# ================ 알고리즘 설계 전략 : 억지 기법(bruteforce algorithm) ============================
# 1. 문자열 매칭 문제
def string_matching_bf(text, pattern):
    n = len(text) # 텍스트의 길이
    m = len(pattern) # 패턴의 길이

    for i in range(n-m+1): # 비교 가능한 마지막 위치는 n-m
        j = 0
        while j < m and pattern[j] == text[i+j]:
            j += 1 # 다음 문자로 이동
        if j == m: # 패턴의 모든 문자가 일치할 시
            return i # 매칭 성공, 일치하는 부분 문자열의 텍스트 시작 위치[i] 반환
    return - 1 # 매칭 실패


# 테스트
text = "HELLO WORLD"
pattern = "LO"
result = string_matching_bf(text, pattern)

if result != -1:
    print(f"{result} 위치에서 발견")
else:
    print("발견 실패")

print("=" * 50)


def string_matching_all_bf(text, pattern):
    n = len(text) # 텍스트의 길이
    m = len(pattern) # 패턴의 길이
    matches = [] # 매칭 위치를 기록

    for i in range(n-m+1): # 비교 가능한 마지막 위치는 n-m
        j = 0
        while j < m and pattern[j] == text[i+j]:
            j += 1 # 다음 문자로 이동
        if j == m: # 패턴의 모든 문자가 일치할 시
            matches.append(i) # 일치하는 부분 문자열의 텍스트 시작 위치[i] 추가
    return matches


# 테스트 2
text = "010101010101010101010101"
pattern = "1010"
result = string_matching_all_bf(text, pattern)

if result != None:
    print(f"{result} 위치에서 발견")
else:
    print("발견 실패")

print("=" * 50)

# ============================================================================
# 2. 0/1 배낭 채우기 문제
def knapsack01_bf(wgt, val, W):
    # wgt : 물건 무게 리스트, val : 물건 가치 리스트
    # W : 배낭 최대 무게

    n = len(wgt) # 물건의 개수
    bestVal = 0  # 최대 가치 초기화
    bestSet = [] # 최대 가치를 제공하는 부분집합 조합 기록
    count = 0    # 부분집합의 번호 표시

    # 0 ~ 2^n - 1 모든 부분집합 조합 탐색
    for i in range(2 ** n):
        count += 1
        # 1. 각 조합에 대해 2진수 비트 패턴 생성 -> 리스트에 역순으로 저장
        s = [0] *  n  # 비트 리스트 초기화
        tmp = i
        for j in range(n):
            s[j] = tmp % 2  # j 번째 비트
            tmp = tmp // 2  # 다음 비트 이동
        print(f"{i}: 조합의 비트 패턴(선택 여부): {s}")

        # 2. 현재 조합 {i}의 무게/가치 계산
        # s의 j번째 비트가 1이면 j번 물건 포함
        sumWgt = 0        # 현재 조합{i}의 무게 합
        sumVal = 0        # 현재 조합{i}의 가치 합
        chosen_items = [] # 선택된 물건 인덱스 저장

        for j in range(n):
            if s[j] == 1:
                sumWgt += wgt[j]
                sumVal += val[j]
                chosen_items.append(j)  # 선택된 j번째 물건의 인덱스 추가
        print("선택된 물건 인덱스:", chosen_items, " / 총 무게 =", sumWgt, " / 총 가치 =", sumVal)

        # 3. 배낭 무게 조건 만족하면 최대값 갱신
        if sumWgt <= W:
            print("배낭 용량 충족")
            if sumVal > bestVal:  # 현재 가치가 최대 가치보다 크면 갱신
                bestVal = sumVal
                bestSet = chosen_items[:]
                print("가치 최대값 갱신")
            else:
                print("가치 최대값 갱신 없음")
        else:
            print("배낭 용량 초과")

        print()
    return bestSet, bestVal

# 테스트
weight = [10,20,30,25,35]
value = [60,100,120,70,85]
W = 80
bestSet, bestVal = knapsack01_bf(weight, value, W)
print(f"최대 가치: {bestVal}일 때 선택된 물건 인덱스: {bestSet}")
print("=" * 50)

# ==================================================================================================
# ================ 알고리즘 설계 전략 : 탐욕적 알고리즘(greedy algorithm) ============================
# 1. 거스름돈 동전 최소화 문제
def coin_change_greedy(coins, amount):
    # 1) 탐욕기법 정의: 큰 단위부터 사용하기 위해 정렬 - 액면가가 높은 것부터 내림차순 정렬
    coins.sort(reverse=True)  # 0(n log n)

    # 2) 탐욕적 거스름돈 계산
    result = []      # (동전 단위, 사용 개수) 기록
    total_count = 0  # 동전의 총 개수
    remain = amount  # 남은 금액

    for coin in coins:
        cnt = remain // coin  # 해당 동전을 최대한 사용한 개수
        result.append((coin,cnt))
        total_count += cnt    # 총 동전 사용 개수 갱신
        remain -= coin * cnt  # 남은 금액 갱신

    if remain == 0:
        return total_count, result
    else:
        return -1, []


# 테스트
coins = [500, 100, 50, 10, 5, 1]
# 하기 동전시스템은 greedy 알고리즘이 최적해를 보장 못함
# coins = [500, 100, 50, 10, 5, 1]  # 실제 최적해는 동전 3개 사용: (500,1), (60,2)
amount = 620
total_count, result = coin_change_greedy(coins, amount)

if result != None:
    print(f"사용된 동전의 종류: {result}\n총 동전의 개수: {total_count}")
else:
    print("발견 실패")
print("=" * 50)


#===============================================================================
# 2. 분할 가능한(Fractional) 배낭 채우기 문제
# - 그리디 알고리즘: 항상 최적해 보장
def fracknapsack_greedy(weights, values, W):
    # 반환: (최대 가치, 가방에 채운 물건 기록)
    n = len(weights)
    # --- 1단계: 단위 무게당 가격 비율 ratio 생성
    items = []  # 물건: 비율, 무게, 가치, 인덱스
    for i in range(n):
        items.append((values[i]/weights[i], weights[i], values[i], i))

    # --- 2단계: 단위 무게당 가격의 내림차순 정렬: O(n log n)
    items.sort(reverse=True, key=lambda x : x[0])  # 비율 기준으로 내림차순 정렬

    # --- 3단계: Greedy 채우기
    bestVal = 0
    bag_with_items = []  # 가방에 넣을 물건 기록

    for ratio, wgt, val, idx in items:  # 비율이 높은 순서로 물건 선택
        if W <= 0:    # 가방이 꽉 찬 경우
            break
        if W >= wgt:  # 물건을 통채로 넣는 경우 
            W -= wgt
            bestVal += val
            bag_with_items.append(("full", idx, wgt, val))
        else:         # W < wgt - 통채로 넣을 수 없으니 분할해서 일부를 넣는 경우
            fraction = W / wgt
            bestVal += val * fraction
            bag_with_items.append(("part", idx, wgt, val*fraction))
            W = 0     # 가방이 꽉 찬 경우
            break
    return (bestVal, bag_with_items)


# 테스트
weights = [12,10,8]
values = [120,80,60]
W = 18

bestVal, bag_with_items = fracknapsack_greedy(weights, values, W)
print(f"테스트 데이터: 최대 가치 = {bestVal}, 가방에 넣은 물건 기록 = {bag_with_items}")