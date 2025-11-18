# 도서 관리 프로그램 (단순 연결 리스트)

# 단순 연결 리스트를 위한 노드 클래스
class Node:
    def __init__(self,elem,next=None):
        self.data = elem
        self.link = next
    def append(self,new): # 현재 노드 다음에 new 노드 삽입
        if new is not None:
            new.link = self.link
            self.link = new
    def popNext(self): # 현재 노드의 다음 노드를 삭제하고 반환
        deleted_node = self.link
        if deleted_node is not None: self.link = deleted_node.link
        return deleted_node
    
# Book 클래스(책 정보 저장)
class Book:
    def __init__(self,book_id,title,author,year):
        self.book_id = book_id # 책 번호(중복 x)
        self.title = title # 책 제목(중복 x)
        self.author = author # 저자
        self.year = year # 출판 연도

    def __repr__(self): # 책 정보 출력 형식
        return f"[책 번호: {self.book_id}, 책 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]"
    
# LinkedList 클래스(단순 연결 리스트 구조)
class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head is None

    def append(self,book): # 맨 뒤에 Book 추가
        new = Node(book)
        if self.isEmpty(): # 첫 번째 노드인 경우
            self.head = new
            return
        ptr = self.head
        while ptr.link is not None: # 마지막 노드까지 이동
            ptr = ptr.link
        ptr.append(new) # 마지막 노드 뒤에 new 연결
    
    def find_by_title(self,title): # 책 제목으로 리스트에서 도서 찾기, Book or None
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data
            ptr = ptr.link
        return None
    
    def find_pos_by_title(self,title): # 책 제목으로 리스트에서 도서의 위치(pos) 찾기
        pos = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return pos
            ptr = ptr.link
            pos += 1
        return -1 # 없으면 -1
    
    def remove_by_title(self,title): # 책 제목으로 도서 삭제
        if self.isEmpty():
            return False
        if self.head.data.title == title: # 머리 노드가 삭제 대상인 경우
            self.head = self.head.link
            return True
        before = self.head
        while before is not None and before.link is not None:
            if before.link.data.title == title: # before.link의 title이 일치할 경우 before.popNext()로 다음 노드를 삭제함
                before.popNext()
                return True
            before = before.link
        return False

    def exists_title(self,title): # 책 제목 중복 확인, 중복이면 True
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return True
            ptr = ptr.link
        return False

    def exists_id(self,book_id): # 책 번호 중복 확인, 중복이면 True
        ptr = self.head
        while ptr is not None:
            if ptr.data.book_id == book_id:
                return True
            ptr = ptr.link
        return False
    
    def display(self): # 전체 도서 출력
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        print("=== 전체 등록 도서 목록 ===")
        ptr = self.head
        while ptr is not None:
            print(repr(ptr.data))
            ptr = ptr.link

# BookManagement 클래스(메뉴, 기능)
class BookManagement:
    def __init__(self):
        self.book_list = LinkedList()
    
    def add_book(self,book_id,title,author,year): # 도서 추가 기능
        # 중복 검사 - 책 번호, 책 제목 중복일시 오류
        if self.book_list.exists_id(book_id):
            print(f"책 번호 '{book_id}'는 이미 존재합니다.")
            return
        if self.book_list.exists_title(title):
            print(f"책 제목 '{title}'은 이미 존재합니다.")
            return
        self.book_list.append(Book(book_id,title,author,year))
        print(f"도서 '{title}'가 추가되었습니다.")

    def remove_book(self,title): # 도서 삭제 기능(책 제목으로 삭제)
        delete = self.book_list.remove_by_title(title) # 삭제 결과 True or False
        if delete:
            print(f"책 제목 '{title}'의 도서가 삭제되었습니다.")
        else:
            print(f"삭제 실패: 책 제목 '{title}'을 찾을 수 없습니다.")

    def search_book(self,title): # 도서 조회 기능(책 제목으로 조회)
        book = self.book_list.find_by_title(title)
        if book is None:
            print(f"조회 실패: 책 제목 '{title}'을 찾을 수 없습니다.")
        else:
            print(repr(book))

    def display_books(self): # 리스트의 모든 도서 출력
        self.book_list.display()

    def menu(self): # 메뉴 출력
        print()
        print("=== 도서 관리 프로그램 ===")
        print("1. 도서 추가")
        print("2. 도서 삭제 (책 제목으로 삭제)")
        print("3. 도서 조회 (책 제목으로 조회)")
        print("4. 전체 도서 목록 출력")
        print("5. 종료")

    def run(self): # 프로그램 실행
        while True:
            self.menu()
            choice = input("메뉴를 선택하세요: ")

            if choice == '1':
                # 도서 추가
                # 사용자가 숫자가 아닌 값을 입력하면, 프로그램이 종료되지 않고 오류 메세지 출력
                # 책 번호와 출판 연도만 포함
                try:
                    book_id = int(input("책 번호를 입력하세요: "))
                except ValueError:
                    print("잘못된 입력입니다. 정수를 입력해주세요.")
                    continue
                
                title = input("책 제목을 입력하세요: ")
                author = input("저자를 입력하세요: ")
                
                try:
                    year = int(input("출판 연도를 입력하세요: "))
                except ValueError:
                    print("잘못된 입력입니다. 정수를 입력하세요.")
                    continue

                # 입력 값을 도서 추가 함수에 전달    
                self.add_book(book_id,title,author,year)
            
            elif choice == '2': # 도서 삭제(책 제목)
                title = input("삭제할 책 제목을 입력하세요: ")
                self.remove_book(title)
            
            elif choice == '3': # 도서 조회(책 제목)
                title = input("조회할 책 제목을 입력하세요: ")
                self.search_book(title)

            elif choice== '4': # 전체 도서 목록 출력
                self.display_books()

            elif choice == '5': # 프로그램 종료
                print("프로그램을 종료합니다.")
                break
            
            else: # 1~5 이외의 값 입력 시
                print("잘못된 선택입니다. 1~5중에서 선택하세요.")


# ============================================
# 프로그램 실행
# ============================================
if __name__ == "__main__":
    program = BookManagement()
    program.run()
    
