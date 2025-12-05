# =======================================================================
# 알고리즘 설계 전략: 분할과 정복(DC: Divide & Conquer)
# =======================================================================

# 1. k번째 작은 수 찾는 문제(kth smallest selection problem)
# - 최소 정복으로 설계, 퀵 정렬의 분할 함수 이용, 재귀 함수로 처리
# (1). 분할 함수
def partition(A, left, right):
    pivot = A[left]
    i = left + 1
    j = right

    while True:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i > j:
            break
        A[i], A[j] = A[j], A[i]
    A[left], A[j] = A[j], A[left]
    return j

# (2). 축소 정복
def quick_select(A, left, right, k):
    if left == right: # 재귀함수 호출 종료
        return A[left]
    pos = partition(A, left, right) # 피벗을 배열 A의 첫 번째 요소로 설정
    if k + left == pos + 1:  # case 1. 피벗이 k 번째인 경우
        return A[pos]
    elif k + left < pos + 1: # case 2. k 번째 작은 수가 왼쪽에 있는 경우
        return quick_select(A, left, pos-1, k)
    else:  # case 3. k 번째 작은 수가 오른쪽에 있는 경우
        return quick_select(A, pos+1, right, k-(pos+1-left))
    

# 테스트
A = [7,2,1,8,6,3,5,4,0]
k = 3
print(quick_select(A, 0, len(A)-1, k)) # 3 번째로 작은 수 찾기
print("=" * 50)


# 1-2. 병합정렬(MergeSort) 문제
# 오름차순으로 정렬
# (1). 병합함수(merge)
def merge(A, left, mid, right):
    # 1. 임시 리스트 생성
    sorted_list = [0] * (right - left + 1)
    # 2. 두 부분 리스트의 시작 인덱스
    i = left
    j = mid + 1
    k = 0
    # 3. 두 정렬 리스트를 비교하여 임시 리스트에 기록
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted_list[k] = A[i]
            i += 1
            k += 1
        else:
            sorted_list[k] = A[j]
            j += 1
            k += 1
    # 4-1. 왼쪽 부분 리스트의 요소가 남아 있는 경우 임시 리스트에 모두 복사
    while i <= mid:
        sorted_list[k] = A[i]
        i += 1
        k += 1
    # 4-2. 오른쪽 부분 리스트의 요소가 남아 있는 경우 임시 리스트에 모두 복사
    while j <= right:
        sorted_list[k] = A[j]
        j += 1
        k += 1
    # 5. 임시 리스트의 결과를 원래 리스트 A에 덮어쓰기
    for t in range(k):
        A[left + t] = sorted_list[t]


# (2). 병합정렬 함수
def merge_sort(A, left, right):
    if left < right: # 항목이 두 개 이상인 경우에만 분할
        mid = (left + right) // 2
        merge_sort(A, left, mid) # 왼쪽 서브 리스트 병합정렬
        merge_sort(A, mid+1, right) # 오른쪽 서브 리스트 병합정렬
        merge(A, left, mid, right) # 정렬된 두 개의 부분 리스트를 병합


# 테스트
A = [38,27,43,3,8,82,10]
print("정렬 전:",A)
merge_sort(A, 0, len(A)-1)
print("정렬 후:", A)
print("=" * 50)



# ========================================================================
# 알고리즘 설계 전략: 동적 계획법(DP: Dynamic Programming)
# ========================================================================
# 1. 피보나치 수열 문제(fibonacci sequence)
# 1-1. 메모이제이션 방식(top-down, 하향식): 주어진 문제를 작은 문제로 해결해 나가는 방식
# (1). 전역 변수로 DP 1차원 배열로 구현
mem = [None] * 11
# 피보나치 수 계산
def fib_dp_mem(n):
    if mem[n] == None:
        if n < 2:  # 재귀함수 호출 종료
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    
    return mem[n]


# 테스트
print("n = 6 -> fib(6):", fib_dp_mem(6))
print("mem =", mem[:7]) # 결과 수열 출력
print("=" * 50)


# 1-2. 테이블화 방식(bottom-up, 상향식): 작은 문제부터 해결하여 주어진 문제를 해결
# 테이블: 지역 변수로 생성 + 반복문 처리
def fib_dp_tab(n):
    # 1. 테이블: 1차원 리스트
    table = [None] * (n+1)
    table[0] = 0
    table[1] = 1
    # 2. n >= 2 이상인 경우
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table

table = fib_dp_tab(6)
print("fib(6) -->", table[6])
print("fib.seq ->", table[:7])


# =============================================================================
# 프로그래밍 문제: 계단 오르는 방법의 수 계산하기 - 피보나치 수열 점화식 이용
# =============================================================================
