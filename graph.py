class Node:
    def __init__(self, label: str):
        self.label = label
        self.value = float("inf")
        self.connections = []

    def __str__(self):
        return f"[{self.label}]"


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, new_node: Node):
        if new_node in self.nodes:
            return

        self.nodes.append(new_node)

    # Método já printa a fila em cada iteração e mostra o valor
    def start(self, node_source: str):
        max_distance = 0
        source = None
        for node in self.nodes:
            if node.label == node_source:
                source = node

        # Verificar se ambos foram encontrados, senão retornar que não existe no grafo
        if type(source) == Node:

            source.value = 0
            queue = [source]
            visited = set()

            while len(queue):
                actual_node = queue[0]
                queue = queue[1:]

                if actual_node in visited:
                    continue

                visited.add(actual_node)

                for child in actual_node.connections:
                    child.value = min(child.value, actual_node.value + 1)

                    if child not in queue and child not in visited:
                        queue.append(child)
                        max_distance = max(actual_node.value, child.value)

            return max_distance

        return -1

    def reset_values(self):
        for i in self.nodes:
            i.value = float("inf")

    def find_diameter(self):
        diameter = 0

        for i in self.nodes:
            diameter = max(diameter, self.start(i.label))
            self.reset_values()

        print(f'Diâmetro: {diameter}')


def setup_question(input_graph: Graph):
    nodes = dict((chr(i + 114), []) for i in range(8))

    nodes['r'] = ['s', 'v']
    nodes['s'] = ['w', 'r']
    nodes['t'] = ['u', 'w', 'x']
    nodes['u'] = ['t', 'x', 'y']
    nodes['v'] = ['r']
    nodes['w'] = ['s', 't', 'x']
    nodes['x'] = ['t', 'u', 'w', 'y']
    nodes['y'] = ['u', 'x']

    all_nodes = dict((node, Node(node)) for node in nodes)

    for node in all_nodes:
        all_nodes[node].connections = [all_nodes[c] for c in nodes[node]]
        input_graph.add_node(all_nodes[node])


g = Graph()
setup_question(g)

g.find_diameter()
