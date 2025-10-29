# ExpressionTree.py
from binary_tree_Wed import BTNode

# 1. 모스코드 결정트리
# ===== 모스 코드 테이블 (A~Z) =====
MORSE_TABLE = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]

# 2. 인코드: 영문자 A ~ Z 그리고 공백 문자 -> 모스 부호 변환
def encode(ch):
    ch = ch.upper()
    if ch == ' ':
        return '/'
    elif 'A' <= ch <= 'Z':
        idx = ord(ch) - ord('A') # ord(ch): 문자를 ASCII 코드값으로 변환
        # 'C'의 인덱스는 ord('C') - ord('A') = 67 - 65 = 2
        # MORSE_TABLE[2][1] = -... 반환
        return MORSE_TABLE[idx][1]
    else: 
        return '?' # 미지원 문자

# 3. 디코드: 결정트리로 모스 부호 -> 해당 문자로 변환
def decode(root,code):
    # 선형 구조 대신 계층 구조인 트리 사용: 효율적 방식
    # 파라미터: root는 결정트리
    if code == '/': # 공백 반환
        return ' '
    node = root # 결정트리의 루트에서 시작
    for c in code: # 모스 부호 문자열(',' / '-')에 대하여 반복 순회(처리)
        if c == '.': # '.' 은 왼쪽 서브트리로 이동
            node = node.left
        if c == '-': # '-' 은 오른쪽 서브트리로 이동
            node = node.right
        if node == None: # 존재하지 않는 경로는 미지원 문자
            return '?'
    
    if node and node.data:
        return node.data # 찾은 문자 반환
    else:
        return '?'
    
# 4. 결정 트리 생성
def make_morse_tree():
    root = BTNode(None, None, None) # 빈 노드 생성(루트 초기화)
    for ch, code in MORSE_TABLE: # 모스 부호 테이블의 각 튜플(문자, 부호)에 대해 반복 순회(처리)
        cur = root # 루트부터 시작
        for c in code:
            if c == '.': 
                if cur.left is None: # 왼쪽 자식이 없다면 새 노드 생성
                    cur.left = BTNode(None, None, None)
                cur = cur.left # 왼쪽으로 이동
            else:
                if cur.right is None: # 오른쪽 자식이 없다면 새 노드 생성
                    cur.right = BTNode(None, None, None) 
                cur = cur.right # 오른쪽으로 이동
        # 경로를 모두 따라간 끝 노드에 문자(A-Z) 저장
        cur.data = ch
    return root # 완성된 모스 부호 결정 트리 반환


#===================================================
# 테스트 프로그램 : 결정 트리(이진 트리) 기반 모스 코드 트리
#===================================================   

if __name__ == "__main__":
    morseCodeTree = make_morse_tree()
    s = input("입력 문장 : ").strip() # GAMEOVER, DATA

    mlist = [ ]
    for ch in s:
      code = encode(ch) 
      mlist.append(code)
    print("Morse Code:", mlist)

    print("Decoding: ", end='')
    for code in mlist:
        print(decode(morseCodeTree, code), end='')
    print()
   
#==================================================
# 테스트 프로그램 코드 4.17: 수식 트리 생성 및 순회 및 평가
#=====================================================  
# if __name__ == "__main__":
#     # (1+3) * (4/2)
#     # expr = ['1', '3', '+', '4', '2', '/', '*']
#     str = input("입력(후위표기): ")
#     expr = str.split()
#     print("토큰분리(expr): ", expr)

#     root = buildTree(expr)
#     print("트리 루트:", root)

#     preorder(root)
#     print()
#     inorder(root)
#     print()
#     postorder(root)
#     print()
#     print("수식 트리 값 평가:", evaluate(root))             

#=============================
# 테스트 프로그램 QUIZ p.150 
#=============================
# if __name__ == "__main__":
#     # Construct the expression tree for expr = 2 1 3 + * 8 4 / -
#     # Tree structure:
#     # 트리 구조:
#     #        -
#     #      /   \
#     #     *      /
#     #    / \   /  \
#     #   2   +  8   4
#     #      / \
#     #     1  3
#     # 중위식: (2 * (1 + 3)) - (8 / 4)
#     postfix_expr = ['2', '1', '3', '+', '*', '8', '4', '/', '-']
#     root = buildTree(postfix_expr)  # 수식 트리 생성
#     print(root)
#     result = evaluate(root)         # 평가
#     print("평가 결과 =", result)    # 예상 결과: 6.0

