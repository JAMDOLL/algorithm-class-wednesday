# binary_tree.py
#=========================================================================
# 이진 트리를 위한 노드 클래스
# - 연결된 구조로 표현
#=========================================================================

class BTNode:
	def __init__(self,elem,left=None,right=None):
		self.data = elem # 노드의 데이터
		self.left = left # 노드의 왼쪽 자식 링크
		self.right = right # 노드의 오른쪽 자식 링크

	def __repr__(self): # 트리의 노드 객체를 문자열 표현 - print 함수 호출
 		return f"BTNode({self.data !r},{self.left !r},{self.right !r})"
	
#========================================================================
# BTNode 클래스 외부에서 사용할 이진 트리의 연산 함수
# - root: 현재 노드를 나타냄. 보통 트리의 루트(root) 노드부터 시작.
# - root는 이진 트리의 노드 객체이며, .left, .right 속성을 통해 왼쪽과 오른쪽 자식 노드에 접근
#=======================================================================

def print_data(data): # 데이터 출력 함수
	if data is not None:
		print(data, end=" ")

def is_leaf(node): # 노드가 None이 아니고, 왼쪽 오른쪽 자식 노드가 모두 None일 경우 -> 단말노드
	if node is None:
		return False
	return node.left is None and node.right is None

def print_leaf_nodes(node): # 이진트리의 단말 노드만 출력
	# 재귀적 정의: 노드가 None이면 종료, 단말 노드라면 출력, 아니면 왼쪽과 오른쪽 서브트리의 단말 노드를 출력
	if node is None:
		return
	if is_leaf(node):
		print(f"{node.data} is a leaf node") # 단말 노드 출력 후 종료
		return
	# 리프 노드가 아니면 재귀 호출
	print_leaf_nodes(node.left) # 왼쪽 서브트리의 단말 노드 출력
	print_leaf_nodes(node.right) # 오른쪽 서브트리의 단말 노드 출력

def preorder(node): # 전위 순회: 루트 -> 왼쪽 -> 오른쪽 서브트리 순회
	# ex) 노드의 레벨 계산
	if node is None:
		return
	print_data(node.data) # 현재 노드의 데이터 방문(출력)
	preorder(node.left)
	preorder(node.right)

def inorder(node): # 중위 순회: 왼쪽 -> 루트 -> 오른쪽 서브트리 순회
	# ex) 이진 탐색트리에서 노드를 오름차순으로 정렬
	if node is None:
		return
	inorder(node.left)
	print_data(node.data) # 현재 노드의 데이터 방문(출력)
	inorder(node.right)

def postorder(node): # 후위 순회: 왼쪽 -> 오른쪽 -> 루트 순회
	# ex) 폴더의 용량 계산, 수식트리 계산
	if node is None:
		return
	postorder(node.left)
	postorder(node.right)
	print_data(node.data) # 현재 노드의 데이터 방문(출력)

def levelorder(root): # 레벨 순으로 노드 방문 (루트 레벨 =1, 아래로 내려갈수록 레벨 증가)
	# ex) 너비 우선 탐색, 최단 경로 탐색
	# 파이썬 모듈 큐 이용
	from collections import deque # 큐 연산: 삽입(append), 추출(popleft)
	if root is None:
		return
	q = deque() # 큐 생성 -> q
	q.append(root) # 큐에 루트 노드 삽입
	while q: # 큐가 공백이 될 때까지 반복
		node = q.popleft()
		print_data(node.data) # 트리의 노드 방문(출력) - 큐에서 나오는 순서가 방문 순서
		if node.left: # 왼쪽 자식 노드가 존재하면
			q.append(node.left)
		if node.right: # 오른쪽 자식 노드가 존재하면
			q.append(node.right)

def count_nodes(root): # 이진트리의 총 노드 개수
	# 재귀적 정의: 트리가 비어 있으면 0, 아니면 왼쪽/오른쪽 서브트리의 노드 수 + 1(자기 자신)
	if root is None:
		return 0
	return count_nodes(root.left) + count_nodes(root.right) + 1

def count_leaves(node): # 이진트리의 단말 노드 수
	# 재귀적 정의: 트리가 비어 있으면 0, 단말 노드면 1, 왼쪽/오른쪽 서브트리의 총 단말 노드 수
	if node is None:
		return 0
	if is_leaf(node):
		return 1
	return count_leaves(node.left) + count_leaves(node.right)

def tree_height(root): # 이진트리의 높이 계산
	# 재귀적 정의: 트리가 비어 있으면 0, 아니면 왼쪽/오른쪽 서브트리의 높이 중 큰 값 + 1(자기 자신)
	if root is None:
		return 0 
	left_h = tree_height(root.left)
	right_h = tree_height(root.right)
	return max(left_h, right_h) + 1

def count_edges(root): # 이진 트리의 총 간선(엣지, 연결된 링크) 수 구하기
	# 간선의 수 = 노드의 수 -1
	nodes = count_nodes(root) # 노드의 수
	return max(0, nodes-1) # 노드가 0인 경우 음수가 되지 않게 0 반환

def full_binary_tree_nodes(k): # 높이가 k인 포화 이진트리의 노드 개수(루트 레벨=1)
	return 2 ** k - 1

def min_nodes_in_binary_tree(k): # 높이가 k인 이진트리의 최소 노드 개수(루트 레벨=1)
	# 최소 노드는 경사 이진트리 노드 수와 동일
	if k >= 1:
		return k
	else:
		return 0
	
def max_nodes_in_binary_tree(k): # 높이가 k인 이진트리의 최대 노드 개수(루트 레벨=1)
	return full_binary_tree_nodes(k)

def count_none_links(root): # 이진트리에서 노드의 개수가 n개라면 연결되지 않은 링크 수 구하기
	# 재귀적 정의: 노드가 None이면 1, 아니면 왼쪽/오른쪽 서브트리의 연결되지 않은 링크 수 합
	# 비재귀적 정의: 연결되지 않은 링크 수 = 2n - (n - 1) = n + 1
	if root is None:
		return 1
	return count_none_links(root.left) + count_none_links(root.right)
	# return count_nodes(root) + 1 # 비재귀적 정의

#============================================================================
# 예시 트리 구조:
#      A
#    /   \
#   B     C

if __name__ == "__main__":
	# 단말 노드 생성
	left_c = BTNode("B")
	right_c = BTNode("C")
	root = BTNode("A",left_c, right_c)
	print(root) # BTNode('A', BTNode('B', None, None), BTNode('C', None, None))
	print(root.data) # A
	print(root.left.data) # B
	print(root.right.data) # C

#========================================================================
# 테스트 프로그램 : QUIZ (p.127)
#============================================================================
# 예시 트리 생성
#       A
#      / \
#     B   C
#    /   / 
#   D   E 
#  / \
# F  G
# 링크 표현법으로 이진트리 표현
if __name__ == "__main__":
	# 리프 노드 생성
	F = BTNode('F')
	G = BTNode('G')
	E = BTNode('E')
	# 중간 노드 생성
	D = BTNode('D', F, G)
	B = BTNode('B', D)
	C = BTNode('C', E)
	# 루트 노드 생성
	root = BTNode('A', B, C)

	print("노드의 수:", count_nodes(root))
	print("간선의 수:", count_edges(root))
	print("트리의 높이:", tree_height(root))
	print_leaf_nodes(root)
	print("연결되지않은 링크 수:", count_none_links(root))	
	# print("배열 표현:", bitree_to_array(root) )
	print("링크 표현:", root)
	print("높이 5인 포화이진트리의 노드 수:", full_binary_tree_nodes(5))
	print("높이 5인 이진트리의 최소 노드 수:", min_nodes_in_binary_tree(5))
	print("높이 5인 이진트리의 최대 노드 수:", max_nodes_in_binary_tree(5))	

#========================================================================
# 테스트 프로그램 : 코드 4.8 p.136
#========================================================================
# 예시 트리 생성
#       A
#      /  \
#     B     C
#    / \   / 
#   D   E  F
# 링크 표현법으로 이진트리 생성 : 단말 노드 -> 루트

if __name__ == "__main__":
	D = BTNode('D')
	E = BTNode('E')
	B = BTNode('B',D, E)
	F = BTNode('F')
	C = BTNode('C', F)
	root = BTNode('A', B, C)

	print("\n전위순회:", end=" ")
	preorder(root)
	print("\n후위순회:", end=" ")
	postorder(root)
	print("\n중위순회:", end=" ")
	inorder(root)
	print("\n레벨순회:", end=" ")
	levelorder(root)
	print()
	print("노드의 개수:", count_nodes(root))
	print("트리의 높이:", tree_height(root))
	print("단일 노드 수:",count_leaves(root))
	print("간선의 수:", count_edges(root))
	# print("배열 표현:", bitree_to_array(root))
	print("높이 5인 포화이진트리의 노드 수:", full_binary_tree_nodes(5))
	print("높이 5인 이진트리의 최소 노드 수:", min_nodes_in_binary_tree(5))
	print("높이 5인 이진트리의 최대 노드 수:", max_nodes_in_binary_tree(5))	
	print("연결되지않은 링크 수:", count_none_links(root))


	
