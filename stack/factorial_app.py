# 프로그래밍 과제 1: 반복/재귀로 n! 계산기 만들기 (인터랙티브 콘솔)
# 작성자: 20190535_김재민
# 작성일: 2024-09-19
# 요구사항 요약
#  - factorial_iter(n): 반복문, n<0이면 ValueError
#  - factorial_rec(n): 재귀, n<0이면 ValueError
#  - run_with_time(func, n): (결과, 경과시간초) 반환. 예외 전파.
#  - 메뉴 1/2/3/4/q 구현, 입력 검증(정수·음수)
#  - 테스트 데이터: [0,1,2,3,5,10,15,20,30,50,100]

import time

# 반복문 팩토리얼
def factorial_iter(n):
    if n < 0:
        raise ValueError("0 이상의 정수만 입력해주세요.")
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# 재귀 팩토리얼
def factorial_rec(n):
    if n < 0:
        raise ValueError("0 이상의 정수만 입력하세요.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n-1)

# 실행 시간 측정
def run_with_time(func,n):
    start = time.perf_counter() # 시작 시간 기록
    result = func(n)
    end = time.perf_counter() # 끝난 시간 기록
    return result, end - start # 끝난 시간 - 시작 시간 = 실행 시간

# 메뉴 설정
def main():
    while True:
        print("================ Factorial Tester ================")
        print("1) 반복법으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        choice = input("선택: ")
        
        if choice == 'q':
            print("종료합니다.")
            break

        elif choice in ["1","2","3"]:
            # 정수 입력
            try:
                n = int(input("n 값(정수, 0 이상): "))
                if n < 0 :
                    print("0 이상의 정수를 입력하세요.")
                    continue
            except ValueError:
                print("정수만 입력하세요.")
                continue

            if choice == "1":
                # 반복문 실행
                print(f"[반복] {n}! = {factorial_iter(n)}")
            
            elif choice == "2":
                # 재귀 실행
                try:
                    print(f"[재귀] {n}! = {factorial_rec(n)}")
                except RecursionError:
                    print("입력값이 너무 커서 재귀 계산이 불가능합니다.")

            else: # choice == "3"
                i_val, i_t = run_with_time(factorial_iter,n)
                r_val, r_t = run_with_time(factorial_rec, n)
                print(f"[반복] {n}! = {i_val}")
                print(f"[재귀] {n}! = {r_val}")
                print("결과 일치 여부:", "일치" if i_val == r_val else "불일치")
                print(f"[반복] 시간: {i_t:.6f} s | [재귀] 시간: {r_t:.6f} s") # 소수점 6자리 고정, 자동 지수 표기가 되기 때문

        elif choice == "4":
            test_data = [0,1,2,3,5,10,15,20,30,50,100]
            print("[테스트 데이터 실행]")
            for i in test_data:
                i_val, i_t = run_with_time(factorial_iter, i)
                r_val, r_t = run_with_time(factorial_rec, i)
                tf = (i_val == r_val)
                print(f"n = {i} | same = {tf} | iter = {i_t:.6f}s, rec = {r_t:.6f}s")
                print(f" {i}! = {i_val}")
        
        else:
            print("메뉴에서 1,2,3,4,q 중 선택해주세요.")

if __name__ == "__main__":
    main()