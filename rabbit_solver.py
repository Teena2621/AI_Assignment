from collections import deque

def is_goal(state):
    return state == "AAA_BBB"

def get_neighbors(state):
    moves = []
    s = list(state)
    
    for i in range(len(s)):
        if s[i] == '_':
            
            if i > 0 and s[i - 1] == 'B':
                temp = s[:]
                temp[i], temp[i - 1] = temp[i - 1], temp[i]
                moves.append("".join(temp))
            
            
            if i > 1 and s[i - 2] == 'B' and s[i - 1] == 'A':
                temp = s[:]
                temp[i], temp[i - 2] = temp[i - 2], temp[i]
                moves.append("".join(temp))

            
            if i < len(s) - 1 and s[i + 1] == 'A':
                temp = s[:]
                temp[i], temp[i + 1] = temp[i + 1], temp[i]
                moves.append("".join(temp))

            
            if i < len(s) - 2 and s[i + 2] == 'A' and s[i + 1] == 'B':
                temp = s[:]
                temp[i], temp[i + 2] = temp[i + 2], temp[i]
                moves.append("".join(temp))
                
    return moves

# Breadth First Search
def bfs(start):
    q = deque([[start]])
    visited = set()

    while q:
        path = q.popleft()
        state = path[-1]

        if is_goal(state):
            return path
        
        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                q.append(path + [next_state])

# Depth First Search
def dfs(start):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        state = path[-1]

        if is_goal(state):
            return path
        
        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                stack.append(path + [next_state])


initial = "BBB_AAA"
bfs_path = bfs(initial)
dfs_path = dfs(initial)


print("BFS Output Path:")
for i, state in enumerate(bfs_path):
    print(f"Step {i}: {state}")

print("\nDFS Output Path:")
for i, state in enumerate(dfs_path):
    print(f"Step {i}: {state}")
