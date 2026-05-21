'''Given a graph (directed/undirected), check whether a path exists 
between a given source and destination using DFS.
Print "Yes Path Exists" or "No Such Path Exists".
Time Complexity: O(V + E)'''

def dfs(adj, visited, current, dest):
    if current == dest:
        return True

    visited[current] = True

    for i in range(len(adj)):
        if adj[current][i] == 1 and not visited[i]:
            if dfs(adj, visited, i, dest):
                return True

    return False


n = int(input())  # number of vertices
adj = []

for _ in range(n):
    adj.append(list(map(int, input().split())))

src = int(input())
dest = int(input())

visited = [False] * n

if dfs(adj, visited, src, dest):
    print("Yes Path Exists")
else:
    print("No Such Path Exists")