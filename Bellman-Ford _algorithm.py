import networkx as nx

def bellman_ford_trace(graph, source, edge_order):
    d = {v: float('inf') for v in graph.nodes}
    pi = {v: None for v in graph.nodes}
    d[source] = 0

    trace = []

    for i in range(len(graph.nodes) - 1):
        for (u, v) in edge_order:
            if d[u] + graph[u][v]['weight'] < d[v]:
                d[v] = d[u] + graph[u][v]['weight']
                pi[v] = u
        # Save snapshot of current pass
        trace.append({
            'pass': i + 1,
            'd': d.copy(),
            'pi': pi.copy()
        })

    return trace

def print_trace(trace, source):
    print(f"\nBellman-Ford trace from source: {source}")
    for step in trace:
        d_str = ', '.join(f"{k}={v if v != float('inf') else '∞'}" for k, v in step['d'].items())
        pi_str = ', '.join(f"{k}={v}" for k, v in step['pi'].items())
        print(f"Pass {step['pass']}:")
        print(f"  d: {d_str}")
        print(f"  π: {pi_str}")
        print()

# Define the graph based on Figure 24.4
edges_original = [
    ('s', 't', 6),
    ('s', 'y', 7),
    ('t', 'x', 5),
    ('t', 'y', 8),
    ('t', 'z', -4),
    ('y', 't', -3),
    ('y', 'x', -2),
    ('y', 'z', 9),
    ('z', 's', 2),
    ('z', 'x', 7),
    ('x', 'z', 4)
]

# Edge order based on figure (as shown visually)
edge_order = [
    ('s', 't'), ('s', 'y'), ('t', 'x'), ('t', 'y'), ('t', 'z'),
    ('y', 't'), ('y', 'x'), ('y', 'z'), ('z', 's'), ('z', 'x'), ('x', 'z')
]

# Run 1: Use original graph, source = z
G1 = nx.DiGraph()
G1.add_weighted_edges_from(edges_original)
trace_z = bellman_ford_trace(G1, 'z', edge_order)
print_trace(trace_z, 'z')

# Run 2: Change weight of (z, x) to 4, source = s
edges_modified = [(u, v, 4 if (u == 'z' and v == 'x') else w) for (u, v, w) in edges_original]
G2 = nx.DiGraph()
G2.add_weighted_edges_from(edges_modified)
trace_s = bellman_ford_trace(G2, 's', edge_order)
print_trace(trace_s, 's')
