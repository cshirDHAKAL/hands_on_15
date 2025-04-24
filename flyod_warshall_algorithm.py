import numpy as np
import pandas as pd


def floyd_warshall_with_trace(vertices, edges):
    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}

    # Initialize distance matrix
    dist = np.full((n, n), float('inf'))
    np.fill_diagonal(dist, 0)

    # Add edge weights
    for u, v, w in edges:
        dist[index[u], index[v]] = w

    # Print D^(0)
    print_matrix(dist, vertices, k=0)

    # Floyd-Warshall algorithm with tracing
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        print_matrix(dist, vertices, k=k + 1)


def print_matrix(matrix, vertices, k):
    print(f"\nD^{k}:")
    df = pd.DataFrame(matrix, index=vertices, columns=vertices)
    df = df.replace(float('inf'), '∞')
    print(df)


# Define the graph from Figure 25.2
vertices = [1, 2, 3, 4, 5, 6]
edges = [
    (1, 2, 1),
    (1, 4, -4),
    (2, 3, 2),
    (2, 5, 7),
    (3, 6, 10),
    (4, 2, 2),
    (4, 5, -1),
    (5, 3, 5),
    (6, 3, -8),
    (6, 5, 3)
]

# Run the algorithm
floyd_warshall_with_trace(vertices, edges)
