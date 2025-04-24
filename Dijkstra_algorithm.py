import heapq
import networkx as nx

# Define the graph based on Figure 24.2
edges = [
    ('s', 't', 3),
    ('s', 'y', 5),
    ('s', 'z', 2),
    ('t', 'x', 6),
    ('t', 'y', 1),
    ('y', 't', 3),
    ('y', 'x', 4),
    ('y', 'z', 6),
    ('x', 'z', 2),
    ('z', 'x', 7)
]

# Create the graph
G = nx.DiGraph()
G.add_weighted_edges_from(edges)

# Dijkstra's algorithm with trace
def dijkstra_trace(graph, source):
    d = {v: float('inf') for v in graph.nodes}
    pi = {v: None for v in graph.nodes}
    d[source] = 0
    visited = set()
    pq = [(0, source)]

    trace = []

    while pq:
        dist_u, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        snapshot = {
            'visited': visited.copy(),
            'd': d.copy(),
            'pi': pi.copy()
        }
        trace.append(snapshot)

        for v in graph.neighbors(u):
            weight = graph[u][v]['weight']
            if d[v] > d[u] + weight:
                d[v] = d[u] + weight
                pi[v] = u
                heapq.heappush(pq, (d[v], v))

    return trace

# Function to print the trace nicely
def print_trace(trace, source_name):
    print(f"\nDijkstra's algorithm trace from source: {source_name}")
    for i, step in enumerate(trace):
        visited_str = ', '.join(sorted(step['visited']))
        d_str = ', '.join(f"{k}={v if v != float('inf') else '∞'}" for k, v in step['d'].items())
        pi_str = ', '.join(f"{k}={v}" for k, v in step['pi'].items())
        print(f"Step {i + 1}:")
        print(f"  S (visited): {{ {visited_str} }}")
        print(f"  d: {d_str}")
        print(f"  π: {pi_str}")
        print()

# Run for source 's' and 'z'
trace_from_s = dijkstra_trace(G, 's')
trace_from_z = dijkstra_trace(G, 'z')

# Output the traces
print_trace(trace_from_s, 's')
print_trace(trace_from_z, 'z')
