def check_butterflies(n, pairs):
    from collections import deque

    graph = [[] for _ in range(n)]
    for i, j, t in pairs:
        graph[i].append((j, t))
        graph[j].append((i, t))

    color = [None] * n

    for start in range(n):
        if color[start] is not None:
            continue

        color[start] = 0
        q = deque([start])

        while q:
            u = q.popleft()
            for v, t in graph[u]:
                if t == 'same':
                    expected = color[u]
                else:  # different
                    expected = 1 - color[u]

                if color[v] is None:
                    color[v] = expected
                    q.append(v)
                elif color[v] != expected:
                    return False  # противоречие
    return True



n = 4
pairs = [
    (0, 1, 'same'),
    (1, 2, 'different'),
    (2, 3, 'same'),
    (0, 3, 'different')
]

print(check_butterflies(n, pairs))
