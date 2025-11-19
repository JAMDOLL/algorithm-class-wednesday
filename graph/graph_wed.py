#===========================================
# Graph 관련 알고리즘
#===========================================
# 1. 깊이 우선 탐색 (DFS) - 인접행렬 기반 재귀 구현
def DFS(vtx, adj, s, visited):
    print(vtx[s], end = ' ') # 현재 정점 출력
    visited[s] = True # 현재 정점 방문 표시

    # 모든 정점에 대해 검사
    for v in range(len(vtx)):
        if adj[s][v] != 0 and not visited[v] : # 간선이 있고, 방문하지 않은  경우
            DFS(vtx, adj, v, visited) # 그 정점으로 이동하여 DFS 재귀 호출

# -------------------------------
# 테스트 코드
# -------------------------------
if __name__ == "__main__":
    # 정점 리스트
    vtx = ['U','V','W','X','Y']
    # 인접 행렬 
    edge = [
        [0,1,1,0,0], # U -> V, W
        [1,0,1,1,0], # V -> U, W, X
        [1,1,0,0,1], # W -> U, V, Y
        [0,1,0,0,0], # X -> V
        [0,0,1,0,0] # Y -> W
    ]

    print('DFS(출발: U) : ', end="")
    visited = [False] * len(vtx)   # 방문 여부 리스트 초기화
    DFS(vtx, edge, 0, visited)     # U(인덱스 0)에서 시작


# 2. 너비 우선 탐색 (BFS) - 인접 리스트 사용
from collections import deque
def BFS_AL(vtx, adj, s, visited):
    n = len(vtx) # 정점의 개수
    q = deque() # 큐 생성

    q.append(s) # 시작 정점을 큐에 삽입
    visited[s] = True # 방문 표시

    while q:
        s = q.popleft() # 큐의 맨 앞 정점을 꺼냄
        print(vtx[s], end=" ")

        # vtx[s]에 인접한 정점들 검사
        for v in alist[s]:
            if visited[v] == False:
                q.append(v)
                visited[v] = True

# -------------------------------
# 테스트 코드
# -------------------------------
if __name__ == "__main__":
    # 정점 리스트
    vtx = ['U','V','W','X','Y']
    # 인접 리스트 
    alist = [
        [1,2], # U -> V, W
        [0,2,3], # V -> U, W, X
        [0,1,4], # W -> U, V, Y
        [1], # X -> V
        [2] # Y -> W
    ]

    print()
    print('BFS_AL(출발: U) : ', end="")
    visited = [False] * len(vtx) # 방문 여부 리스트 초기화
    BFS_AL(vtx, alist, 0, visited)  # 시작점 U는 인덱스 0


# 3. DFS를 이용한 신장트리 생성 (인접행렬 방식) => 숙제
def ST_DFS(vtx, adj, s, visited):
    visited[s] = True

    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                print("(", vtx[s], vtx[v], ")", end=" ")
                ST_DFS(vtx, adj, v, visited)
    
# -------------------------------
# 테스트 코드
# -------------------------------
if __name__ == "__main__":
    # 정점 리스트
    vtx = ['U','V','W','X','Y']
    # 인접 행렬 
    adj = [
        [0, 1, 0, 0, 0],  # U
        [1, 0, 1, 0, 0],  # V
        [0, 1, 0, 1, 0],  # W
        [0, 0, 1, 0, 1],  # X
        [0, 0, 0, 1, 0]   # Y
    ]

    print()
    print("ST_DFS_AM : ", end="")
    visited = [False] * len(vtx)
    ST_DFS(vtx, adj, 0, visited)   # U에서 시작


# 4. Prim 알고리즘 (인접행렬 방식)
def MSTPrim_greedy(vertex, adj, INF = 999):
    n = len(vertex)
    dist = [INF] * n # 각 정점까지의 최소 거리
    selected = [False] * n # MST의 정점 포함 여부
    dist[0] = 0 # 시작 정점 거리 = 0

    # 내부 함수
    def getMinVertex(dist, selected):
        # MST에 포함되지 않은 인접 정점 중 최소 dist를 가진 정점 반환
        minv = -1 # 최소 거리 정점 인덱스
        mindist = INF # 최소 거리 값

        for v in range(len(dist)): # 모든 정점에 대해 검사
            if not selected[v] and dist[v] < mindist: # 아직 MST에 포함되지 않은 정점이 기존 거리보다 짧으면
                mindist = dist[v] # 최소 거리 갱신
                minv = v # 최소 거리 정점 인덱스
        return minv
    
    print("\n정점 추가 순서:")
    for _ in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True # MST에 포함
        print(vertex[u], "(", dist[u], ")", end=" ")

        for v in range(n):
            if adj[u][v] != INF and not selected[v]:
                if adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]
            print("|", vertex[u], "-", vertex[v], "=>", dist[v], end="")
        print(":", dist)
    
    print("\n최종 dist 배열:", dist)
    print("MST 총 최소 비용:", sum(dist))


# ---------------------------------------------------
# 테스트 코드
# ---------------------------------------------------
if __name__ == "__main__":
    # 정점 리스트
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # 인접 가중치 행렬 
    adj = [
        # A   B    C    D    E    F    G
        [ 0,  25, 999, 12, 999, 999, 999],  # A
        [25,   0, 10, 999, 15, 999, 999],   # B
        [999, 10,  0, 999, 999, 16, 999],   # C
        [12, 999, 999, 0, 17, 999, 37],     # D
        [999, 15, 999, 17, 0, 14, 19],      # E
        [999, 999, 16, 999, 14, 0, 42],     # F
        [999, 999, 999, 37, 19, 42, 0]      # G
    ]

    MSTPrim_greedy(vertex, adj)