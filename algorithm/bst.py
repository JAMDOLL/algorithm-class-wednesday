# ==============================================================
# 이진 탐색 트리 (Binary Search Tree) 구현 + 성능 테스트
# ==============================================================
import random, time
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"  

# 1. 노드 클래스 정의
class BSTNode:
    def __init__(self,key,value):
        self.key = key # 키 (노드 비교 기준)
        self.value = value # 값 (저장 데이터)
        self.left = None # 왼쪽 자식 노드
        self.right = None # 오른쪽 자식 노드

    # 출력 시 보기 좋은 형식으로 표시(튜플 형태)
    def _repr_(self):
        return f"({self.key!r},{self.value!r})"

# 2. 키(key)값으로 노드를 찾는 탐색 (순환구조)
def search_bst(n,key):
    # key 값으로 노드를 찾는 순환 탐색: 사전에서 키를 찾는 것 -> 알파벳 순서로 바로 찾아감
    if n is None:
        return None
    elif key == n.key: # 키가 일치할 시
        return n # 해당 노드 반환
    elif key < n.key:
        return search_bst(n.left, key) # 왼쪽 서브트리로 재귀 탐색
    else:
        return search_bst(n.right, key) # 오른쪽 서브트리로 재귀 탐색

# 3. 값(value)으로 노드를 찾는 탐색 (전위 순회 기반)
def search_value_bst(n, value):
    # value 값으로 노드를 찾는 전위 순회 탐색: 사전에서 뜻을 찾는 것 -> 모든 단어의 뜻을 전부 읽어봄
    if n is None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left,value)
    if res is not None: # 왼쪽에서 찾으면 바로 반환
        return res
    else: # 왼쪽에서 못 찾았으면 오른쪽 서브트리 탐색
        return search_value_bst(n.right,value)

# 4. 삽입 연산 (순환 구조)
def insert_bst(root,node):
    # BST(root)에 노드(node) 삽입
    # (1) 현재 서브트리가 비어있으면 새 노드가 그 서브트리의 루트가 됨
    if root is None:
        return node
    # (2) 동일한 키가 이미 있다면 중복 삽입을 허용하지 않으므로 기존 노드 그대로 반환
    if node.key == root.key:
        return root
    # (3) 삽입할 키가 현재 루트의 키보다 작으면 왼쪽 서브트리로 재귀 삽입
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    # (4) 크면 오른쪽 서브트리로 재귀 삽입
    else:
        root.right = insert_bst(root.right, node)
    # (5) 변경된 서브트리를 연결한 후 최종적으로 루트를 반환
    return root

# 5. 삭제 연산
def delete_bst(root,key):
    # BST(root)에 노드(node) 삭제
    if root is None:
        return root # 삭제할 노드 없음
    # (1) 삭제할 노드가 왼쪽 서브트리에 있는지 검사
    if key < root.key:
        root.left = delete_bst(root.left,key)
    # (2) 삭제할 노드가 오른쪽 서브트리에 있는지 검사
    elif key > root.key:
        root.right = delete_bst(root.right,key)
    # (3) 삭제할 노드를 찾음
    else:
        # case 1,2:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # case 3:
        succ = root.right # 후계자 설정
        # 오른쪽 서브트리에서 가장 왼쪽 노드가 후계자(최솟값)
        while succ.left is not None:
            succ = succ.left
        # (4) 후계자의 키와 값을 현재 삭제할 노드로 복사
        root.key = succ.key
        root.value = succ.value
        # (5) 원래 BST트리의 후계자 노드를 재귀적으로 찾아 삭제
        root.right = delete_bst(root.right,key)
    return root
        
# 6. 순회 함수
def preorder(n): # n : BSTNode
    if n is not None:
        print(f'({n.key}:{n.value})', end=' ')
        preorder(n.left)
        preorder(n.right)

# 7. 출력 함수
def print_node(msg, n): # n: BSTNode
    if n is None:
        print(msg, "탐색 실패")
    else:
        print(msg, f"({n.key}:{n.value})")

def print_tree(msg, r): # r: 트리의 루트 노드
    print(msg, end='')
    preorder(r)
    print()

# 8. 기본 테스트　
if __name__ == "__main__":
    # 샘플 데이터: (key, value) 형식
    data = [
        (6, "여섯"),  # key=6
        (8, "여덟"),  # key=8
        (2, "둘"),    # key=2
        (4, "넷"),    # key=4
        (7, "일곱"),  # key=7
        (5, "다섯"),  # key=5
        (1, "하나"),  # key=1
        (9, "아홉"),  # key=9
        (3, "셋"),    # key=3
        (0, "영")     # key=0
    ]

    root = None # 루트를 초기화
    for key, value in data: # 각 항목으로 BSTNode 생성 후 트리에 삽입 (중복 키는 insert_bst에서 무시)
        root = insert_bst(root, BSTNode(key, value))

    print_tree("현재 트리 전위순회:", root)

    # 키로 탐색
    n = search_bst(root, 3)
    print_node("srch 3:", n)

    n = search_bst(root, 8)
    print_node("srch 8:", n)

    n = search_bst(root, 0)
    print_node("srch 0:", n)

    n = search_bst(root, 10)
    print_node("srch 10:", n)

    # 값으로 탐색
    n = search_value_bst(root, "둘")
    print_node("search value '둘':", n)
    n = search_value_bst(root, "열")
    print_node("search value '열':", n)

    # 키 노드 삭제 후 전위순회 출력
    root = delete_bst(root, 7)
    print_tree("키=7 삭제 후 트리:", root)

    root = delete_bst(root, 8)
    print_tree("키=8 삭제 후 트리:", root)

    root = delete_bst(root, 2)
    print_tree("키=2 삭제 후 트리:", root)

    root = delete_bst(root, 6)
    print_tree("키=6 삭제 후 트리:", root)

# --------------------------------------------------------------
# 9. 성능 테스트 (삽입/탐색 속도) , 정의 : 숙제
def bst_perf_graph＿test(sizes):
    insert_times = [] # 각 크기 n마다 삽입 총 시간을 저장
    search_times = [] # 각 크기 n마다 탐색 1회 평균 시간을 저장

    for n in sizes: # 랜덤 키 생성
        keys = random.sample(range(n*10), n)
    
        # 삽입 시간 측정
        root = None
        start = time.time()
        for k in keys:
            root = insert_bst(root, BSTNode(k,k))
        end = time.time()
        insert_ms = (end-start) * 1000.0
        insert_times.append(insert_ms)

        # 탐색 시간 측정(평균)
        num_searches = min(1000,n) # 최대 1000번까지만 실행
        search_keys = random.choices(keys, k = num_searches) # 존재하는 키들만 사용

        start = time.time()
        for k in search_keys:
            _ = search_bst(root, k)
        end = time.time()

        avg_search_ms = (end-start) * 1000.0 / num_searches
        search_times.append(avg_search_ms)

        print(f"n={n:6d} 삽입: {insert_ms:8.3f} ms, 탐색 평균: {avg_search_ms:8.6f} ms")

    return insert_times, search_times


if __name__ == "__main__":
    sizes = [1000, 2000, 5000, 10000, 20000]
    # 그래프 시각화: bst_perf_graph_test 호출 후 결과 플롯
    insert_times, search_times = bst_perf_graph_test(sizes)

    plt.figure(figsize=(8,5))
    plt.plot(sizes, insert_times, 'o-', color='seagreen', label='삽입 총시간 (ms)')
    plt.plot(sizes, search_times, 'o-', color='orange', label='탐색 1회 평균 (ms)')
    plt.title("BST 삽입/탐색 성능")
    plt.xlabel("노드 수 (n)")
    plt.ylabel("시간 (ms)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
