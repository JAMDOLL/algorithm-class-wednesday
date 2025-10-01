# singly_linked_list.py
#=========================================================
# 코드 3.1: 단순연결구조를 위한 Node 클래스
"""
1. 단순 연결 구조를 위한 Node 클래스
2. 각 노드는 데이터 필드(data)와 다음 노드를 가리키는 링크 필드(link)를 가짐
3. append(node): 현재 노드 뒤에 주어진 노드를 연결
4. popNext(): 현재 노드의 다음 노드를 리스트에서 제거하고, 그 노드를 반환
"""
# 단순연결구조를 위한 Node 클래스
class Node:
    def __init__(self,elem,link=None):
        self.data = elem # 데이터 필드
        self.link = link # 다음 노드를 가리키는 주소값을 저장(링크) 필드
    
    # 노드 기반 삽입 연산
    def append(self,new): # 현재 노드(self) 뒤에 주어진 새 노드(new)를 연결
        if new is not None:
            new.link = self.link # new의 다음 노드는 현재 노드(self)의 다음 노드로 수정
            self.link = new # 현재 노드(self)의 다음 노드를 new로 수정

    # 노드 기반 삭제 연산
    def popNext(self):
        delete = self.link
        if delete is not None:
            self.link = delete.link
            delete.link = None
        return delete


# 코드 3.2: 단순연결리스트 클래스
"""
1. 단순 연결 리스트 구조를 관리하는 클래스
2. head: 리스트의 첫 번째 노드를 가리키는 포인터
3. 주요 메서드:
   - isEmpty(): 리스트가 비어있는지 확인
   - isFull(): 리스트가 가득 찼는지 확인
   - getNode(pos): 특정 위치의 노드를 반환
   - getEntry(pos): 특정 위치의 노드 데이터를 반환
   - replace(pos, elem): 특정 위치의 노드 데이터를 변경
   - size(): 리스트의 크기를 반환
   - display(msg): 리스트의 내용을 출력
   - insert(pos, elem): 특정 위치에 새 노드를 삽입
   - delete(pos): 특정 위치의 노드를 삭제
   - find(elem): 특정 데이터를 가진 노드를 검색
"""
# 단순연결리스트 클래스

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self): 
        return self.head == None # self.head가 None 이면 공백 상태
    
    def is_full(self):
        return False # 연결 리스트는 포화 상태 X
    
    def getNode(self,pos): # pos 기반 연산
        # pos 위치에 있는 노드를 반환
        # pos는 리스트의 인덱스 0부터 고려
        if pos < 0 : return None # pos는 유효하지 않은 위치
        if self.head == None: # 리스트가 빈 상태
            return None
        else:
            ptr = self.head
            for i in range(pos):
                if ptr == None: # pos가 리스트보다 크기가 큰 경우(유효하지 않은 위치)
                    return None
                ptr = ptr.link
            return ptr

    def getEntry(self,pos): 
        # 리스트의 pos 위치에 있는 노드를 찾아 데이터 값을 변환
        node = self.getNode(pos) # getNode()를 사용해 해당 위치의 노드를 찾음
        if node == None: # 해당 노드가 없는 경우
            return None # None 반환
        else:
            return node.data # 있는 경우 노드의 데이터 반환
        
    def insert(self,pos,elem): # 인덱스 기반 연산 
        if pos < 0:
            raise ValueError("잘못된 위치 값입니다.")
        new = Node(elem) # 1. 새 노드 생성
        before = self.getNode(pos-1) # 2. pos -1 위치의 노드 탐색
        # 3. before 노드의 위치에 따라 구분
        if before == None:
            if pos == 0: # a. 머리 노드로 삽입
                new.link = self.head
                self.head = new
                return
            else: # b. pos가 리스트 범위 밖에 있음
                raise IndexError("삽입할 위치가 유효하지 않습니다.")
        else: # c. 중간 노드로 삽입
            before.append(new)

    def delete(self,pos): # 인덱스 기반 연산
        # pos 위치에서 해당 노드 삭제 연산
        if pos < 0:
            raise ValueError("잘못된 위치 값입니다.")
        before = self.getNode(pos-1) # 1. 삭제 노드 이전의 노드 탐색
        # 2. before 노드의 위치에 따라 구분
        if before == None:
            if pos == 0: # a. 머리 노드로 삭제
                delete = self.head
                self.head = delete.link
                delete.link = None # 연결 해제
                return delete
            else: # b. pos가 리스트 범위 밖에 있음
                raise IndexError("삽입할 위치가 유효하지 않습니다.")
        else: # c. 중간 노드로 삭제
            return before.popNext()

    def size(self):
        # 리스트의 전체 노드 개수
        if self.head == None: # 현재 리스트가 공백 상태면
            return 0
        else:
            ptr = self.head
            count = 0
            while ptr != None: # ptr이 None이 아닐때까지
                ptr = ptr.link
                count += 1
            return count
    
    def display(self,msg="LinkedList:"):
        # 리스트의 내용을 출력
        print(msg, end=" ")
        if self.head == None: # 현재 리스트가 공백 상태면
            return None
        else:
            ptr = self.head
            while ptr != None: # ptr이 None이 아닐때까지
                print(ptr.data,end=" -> ")
                ptr = ptr.link
            print("None")
    
    def replace(self,pos,elem): # 인덱스 기반의 연산
        # 리스트 pos 위치에 있는 노드의 데이터 필드를 수정
        node = self.getNode(pos)
        if node != None: # 해당 노드가 있는 경우
            node.data = elem


 
# 연습문제2: 어떤 요소를 찾아 위치를 반환하는 함수를 정의하기 : 리스트에 없으면 -1 반환, 있으면 그 위치를 정수로 반환

    
   
#=========================================================
# 테스트 프로그래램
#=========================================================
def test_code_3_3():
    #1. 연결 리스트 생성
    ll = LinkedList()
    ll.display("연결리스트(초기): ")      # 출력: LinkedList: None

    #2. 노드 삽입
    ll.insert(0, 10) # 첫 번째 위치에 10 삽입
    ll.display("첫 번째 위치에 10 삽입")

    ll.insert(0, 20)  # 첫 번째 위치에 20 삽입
    ll.display("첫 번째 위치에 20 삽입")

    ll.insert(1, 30)  # 두 번째 위치에 30 삽입
    ll.display("두 번째 위치에 30 삽입")

    ll.insert(ll.size(), 40)  # 마지막 위치에 40 삽입
    ll.display("마지막 위치에 40 삽입")

    ll.insert(2, 50)  # 세 번째 위치에 50 삽입
    ll.display("세 번째 위치에 50 삽입")
    ll.display("연결리스트(삽입x5): ")  

    ll.replace(2,90) # 세 번째 위치의 노드 데이터를 90으로 변경
    ll.display("연결리스트(교체X1-> 90으로 변경): ")    

    # 3.노드 삭제
    ll.delete(2)      # 세 번째 노드 삭제
    ll.display("세 번째 노드 삭제")

    ll.delete(3)      # 네 번째 노드 삭제
    ll.display("네 번째 노드 삭제")

    ll.delete(0)      # 첫 번째 노드 삭제
    ll.display("첫 번째 노드 삭제")
    ll.display("연결리스트(삭제x3): "   )      



if __name__ == "__main__" :
    test_code_3_3()  
    # test()
    # quiz_2()


