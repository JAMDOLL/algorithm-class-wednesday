# ==================================
# 예제: 리스트에서 최대값 찾는 문제
# 성능 분석기 비교연산과 이동연산 기준
# ==================================
def find_max(A):
    n = len(A) # 입력 크기
    move = 0 # 이동 연산 횟수
    cmp = 0 # 비교 연산 횟수

    max_val = A[0] # 최대값 초기화
    move += 1

    for i in range(1,n): # 1 ~ n-1까지
        cmp += 1
        if A[i] > max_val:
            max_val = A[i]
            move += 1
    return max_val, cmp, move

# ======================================================
# 정렬 알고리즘
# ======================================================
def selection_sort(arr): # 선택 정렬
    a = arr[:] # 원본 복사
    n = len(arr) # 입력 크기
    cmp = 0 # 비교 연산 횟수
    move = 0 # 이동 연산 횟수

    for i in range(n-1): # i 번째 위치에 최소값을 선택 배치
        min_idx = i # 최소값의 인덱스
        for j in range(i+1, n): # 미정렬 구간 탐색
            cmp += 1
            if a[j] < a[min_idx]: # 더 작은 값을 발견
                min_idx = j

        a[i],a[min_idx] = a[min_idx],a[i] # i 번째 위치와 최소값의 위치를 교환
        move += 3 # move가 3번인 이유:
        # tmp = a
        # a = b
        # b = tmp
    return a, cmp, move

def insertion_sort(arr): # 삽입 정렬
    a = arr[:] # 원본 복사
    n = len(arr) # 입력 크기
    cmp = 0 # 비교 연산
    move = 0 # 이동 연산

    for i in range(1,n): # 두 번째 요소부터 시작
        key = a[i] # 삽입할 요소
        move += 1

        # 삽입할 요소의 삽입 위치 찾기
        j = i-1
        while j >= 0:
            cmp += 1
            if a[j] > key:
                a[j+1]= a[j] # 뒤쪽으로 한 칸 이동
                move += 1
                j -= 1 # 왼쪽으로 한 칸 이동
            else:
                break
        a[j+1] = key # 삽입할 위치
        move += 1
    return a, cmp, move

# ==================================
# 테스트 실행
# ==================================
if __name__ == "__main__":
    data = [3,9,2,7,5,10,4]

    result, cmp_count, move_count = find_max(data)
    print(f"최대값: {result}, 비교 연산 횟수: {cmp_count}, 이동 연산 횟수: {move_count}")
    print()

    sorted_array, cmp_count, move_count = selection_sort(data)
    print(f"선택 정렬: {sorted_array}")
    print(f"비교 연산 횟수: {cmp_count}, 이동 연산 횟수: {move_count}")
    print()

    insert_sorted_array, cmp_count, move_count = insertion_sort(data)
    print(f"삽입 정렬: {insert_sorted_array}")
    print(f"비교 연산 횟수: {cmp_count}, 이동 연산 횟수: {move_count}")
    print()