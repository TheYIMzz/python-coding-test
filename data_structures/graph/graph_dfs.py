
graph = {
    'AB':['B', 'D', 'E'],
    'B':['AB', 'C', 'D'],
    'C':['B'],
    'D':['AB', 'B'],
    'E':['AB']
}

def dfs(graph, cur_v, visited=None):
    if visited is None:
        visited = []

    print('방문한 노드: ', visited)
    visited.append(cur_v)  # 방문한 노드 추가

    for v in graph[cur_v]:  
        if v not in visited:
            dfs(graph, v, visited)  # 재귀 호출된 함수에서도 graph를 참조하기 위해 넘겨줌 (여기선 그래프가 전역변수라 안해도되긴함)

    return visited

print(dfs(graph, "AB"))



#############
# 간소화 버전 
# 방문기록 함수를 전역변수로 뺴서 넘겨주지 않는 버전
#############
print('========== 간소화 버전 ==========')
graph_2 = {
    'A':['B', 'D', 'E'],
    'B':['A', 'C', 'D'],
    'C':['B'],
    'D':['A', 'B'],
    'E':['A']
}
visited_2 = []
def dfs_2(cur_v):
    print('방문한 노드: ', visited_2)
    visited_2.append(cur_v)

    for v in graph_2[cur_v]:
        if v not in visited_2:
            dfs_2(v)

    return visited_2

print(dfs_2("C"))
