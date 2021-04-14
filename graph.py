# Biblioteca para desenho
import networkx as nx
import matplotlib.pyplot as plt


# Método para visualizar
def visualizarGrafo(arr):
    G = nx.Graph()
    G.add_edges_from(arr)
    nx.draw_networkx(G)
    plt.show()


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

    def __str__(self):
        return 'Graph: \n{}'.format(
            '\n'.join([f'{existing_node.label} - {existing_node.connections}' for existing_node in self.nodes]))

    # Método já printa a fila em cada iteração e mostra o valor
    def start(self, node_source: str):
        generated_tree = []
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
                print(' - '.join([f'{str(i)}({i.value})' for i in queue]))

                actual_node = queue[0]
                queue = queue[1:]

                if actual_node in visited:
                    continue

                visited.add(actual_node)

                for child in actual_node.connections:
                    child.value = min(child.value, actual_node.value + 1)

                    if child not in queue and child not in visited:
                        queue.append(child)

                        if [actual_node, child] not in generated_tree and [child, actual_node] not in generated_tree:
                            generated_tree.append([actual_node, child])

            visualizarGrafo(generated_tree)


def setup_question(input_graph: Graph):
    nodes = dict((chr(i + 114), []) for i in range(8))
    # nodes = dict((str(i+1), []) for i in range(7))

    nodes['r'] = ['s', 'v']
    nodes['s'] = ['w', 'r']
    nodes['t'] = ['u', 'w', 'x']
    nodes['u'] = ['t', 'x', 'y']
    nodes['v'] = ['r']
    nodes['w'] = ['s', 't', 'x']
    nodes['x'] = ['t', 'u', 'w', 'y']
    nodes['y'] = ['u', 'x']

    # nodes['1'] = ['2', '3']
    # nodes['2'] = ['1', '4', '6']
    # nodes['3'] = ['1', '4']
    # nodes['4'] = ['1', '3', '2', '7']
    # nodes['5'] = ['6', '7']
    # nodes['6'] = ['2', '5', '7']
    # nodes['7'] = ['4', '5', '6']

    all_nodes = dict((node, Node(node)) for node in nodes)

    for node in all_nodes:
        all_nodes[node].connections = [all_nodes[c] for c in nodes[node]]
        input_graph.add_node(all_nodes[node])


g = Graph()
setup_question(g)

# Teste dos slides (Aula 05 - p. 18) - OK
g.start('t')
