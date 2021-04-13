from node import Node


def setup_question(input_graph):
    nodes = dict((chr(i + 114), []) for i in range(8))

    nodes['r'] = ['s', 'v']
    nodes['s'] = ['r', 'w']
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
    def start(self, node_source, node_destination):
        source = destination = None
        # Loop for retrieving source and destination objects
        for node in self.nodes:
            if node.label == node_source:
                source = node
            if node.label == node_destination:
                destination = node

        if type(source) == Node and type(destination) == Node:

            source.value = 0
            queue = [source]
            visited = set()

            print(f"INDO DE {source} PROCURANDO POR {destination}")
            while len(queue):
                print("-------------------------------------------------")
                print([f'{str(i)}({i.value})' for i in queue], 'fila')
                print([f'{str(i)}({i.value})' for i in visited], 'visitado')

                actual_node = queue[0]
                queue = queue[1:]

                # Search ended
                if actual_node == destination:
                    print("-----------------------FIM-----------------------")
                    print([f'{str(i)}({i.value})' for i in visited], 'visitado')
                    return True

                if actual_node in visited:
                    continue

                visited.add(actual_node)

                # Loop through current node "children"
                for child in actual_node.connections:
                    print(str(actual_node), '->', str(child))

                    if child not in visited:
                        child.value = actual_node.value + 1

                    queue.append(child)
            print("-----------------------FIM-----------------------")
            print([f'{str(i)}({i.value})' for i in visited], 'visitado')

        return False


g = Graph()
setup_question(g)

print(g.start('s', 'y'))
apple = 5 + 3
