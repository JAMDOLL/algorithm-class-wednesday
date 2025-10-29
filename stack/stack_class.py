# stack_class.py
# array로 구현한 stack 클래스
# 시간복잡도 : push O(1), pop O(1), peek O(1), is_empty O(1), is_full O(1), size O(1)

class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = item
            print(f"PUSH: {item!r} -> stack = {self.array[:self.top+1]}")
        else:
            raise OverflowError("Stack Overflow") #pass, exit(1)
        
    def pop(self):
        if not self.is_empty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            print(f"POP : {item!r} -> stack = {self.array[:self.top+1]}")
            return item
        else:
            raise IndexError("Stack Underflow") #pass, exit(1)

    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        return None

    def size(self):
        return self.top + 1
    
    # 연습 문제 1-2: 스택을 초기화하는 claer() 함수
    def claer(self):
        self.array = []
        self.top = -1
    
   # 연습 문제 1-3 가장 먼저 들어온 요소부터 순서대로 출력하는 display() 함수
    def display(self):
        for i in range(self.top+1): # 0 ~ self.top 까지
            print(self.array[i], end=" ") 
        print()

# 스택 클래스를 이용한 문자열 거꾸로 뒤집어 출력하기
def reverse_string(statement: str) -> str:
    print("\n[1] PUSH 단계 -----------------")
    st = ArrayStack(len(statement))
    for ch in statement:
        st.push(ch)

    print("\n[2] POP 단계 ------------------")
    out = []
    while not st.is_empty():
        out.append(st.pop())

    result = ''.join(out)
    print(f"\n[3] 최종 결과: {result}")
    return result
    

# 테스트 하기
def test_reverse():
    tests = [       
        ("racecar", "racecar"),   # 회문
        ("안녕하세요. 반갑습니다.", ".다니습갑반 .요세하녕안"),
        ("1234567890", "0987654321"),
    ]
    for s, expected in tests:
        got = reverse_string(s)
        assert got == expected, f"input={s!r}, got={got!r}"

if __name__ == "__main__":
    test_reverse()

# 연습 문제 1-6: 문자열 뒤집기를 순환 호출을 사용하여 구현
def printReverse(msg, len):
    if len > 0:
        print(msg[len-1], end="")
        printReverse(msg,len-1)
instr = "자료구조"
printReverse(instr, len(instr))