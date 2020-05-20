MAX_INT = 2147483647
# Solution by Dijkstra

class Graph():
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
    
    def add_edge(self, father, child, distance):
        self.edges.setdefault(father, [])
        self.edges[father].append(child)
        self.distances[(father, child)] = distance

def dijkstra(graph, init_node):
    # Mapping
    visited = {init_node: 0}
    current_node = init_node
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        curr_weight = visited[min_node]

        for edge in graph.edges[min_node]
            weight = curr_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    return visited, path

def shortest_path(graph, init_node, goal_node):

    distances, paths = dijkstra(graph, init_node)

    route = [goal_node]

    if not paths.get(goal_node):
        return None
    
    while goal_node != init_node:
        route.append(paths[goal_node])
        goal_node = paths[goal_node]

    route.reverse()
    return route

# The problem part
def cal_next_node(a, b, current_node):
    return (a * current_node + b) % 1000

def build_distance(params):
    distances = {}

    for param in params:
        a = param[0]
        b = param[1]
        param_dist = param[2]

        for i in range(0, 1000):
            curr_node = i
            next_node = cal_next_node(a,b,curr_node)
            
            # the distance between nodes 
            distance = distances.get((curr_node, next_node), MAX_INT)
            if distance == MAX_INT or distance > param_dist:
                distances[(curr_node, next_node)] = param_dist
    return distances

def parse_input():
    start, goal = raw_input().rstrip().split(" ")
    k = int(raw_input().rstrip())

    paths = []
    for i in range(k):
        A, B, C = raw_input().rstrip().split(" ")
        paths.append([int(A), int(B), int(C)])
    
    return int(start), int(goal), paths


# process the input
s, f, path = parse_input()

distances = build_distance(path)

graph = Graph()
# Range from the problem definition
graph.nodes = set(range(0, 1000))

for key, value in distances.items():
    graph.add_edge(key[0], key[1], value)

paths = shortest_path(graph, s, f)

if paths:
    smallest_dist = 0
    for i in range(len(paths)-1):
        father = paths[i]
        child = paths[i+1]
        if father and child:
            smallest_dist += graph.distances.get((father, child))
    print(smallest_dist)
else:
    print('-1')
