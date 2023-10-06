from typing import Optional, Type


class DirectedGraph:

    # DirectedGraph : {
    #     nodes: {
    #         '1': Node(1),
    #         '2': Node(2),
    #         '3': Node(3)
    #     }
    # }

    # The nodes are stored in a dict instead of a list to improve speed of retrieval.


    def __init__(self) -> None:
        self.nodes = dict()
        self.start_node = None
    
    def add_node(self, node):
        if not self.start_node:
            self.start_node = node
        self.nodes[node.label] = node
    
    def has_node(self, label):
        if self.nodes.get(label) :
            return True
        return False

    def get_node(self, label):
        return self.nodes.get(label)

    def __repr__(self) -> str:
        return str(self.nodes.items())

class Node:

    def __init__(self, label) -> None:
        self.label = label
        self.outbounds = []
        self.inbounds = []
    

    def add_outbound(self, node):
        self.outbounds.append(node.label)
        node.inbounds.append(self.label)

    def add_inbound(self, node):
        self.inbounds.append(node.label)
    
    def __repr__(self) -> str:
        return str(f'{self.label} -> {self.outbounds}')


def read_nodes_into_graph(s: str):


    node_labels = s.split(' -> ')
    graph = DirectedGraph()
    if len(node_labels) < 1:
        raise Exception('Graph is empty')
    
    node = Node(node_labels[0])
    graph.add_node(node)

    for i in range(len(node_labels) - 1):
        label = node_labels[i]
        current_node = graph.get_node(label)
        next_label = node_labels[i+1]
        if graph.has_node(next_label):
            next_node = graph.get_node(next_label)
        else:
            next_node = Node(next_label)
            graph.add_node(next_node)

        current_node.add_outbound(next_node)
    return graph


    
    # return node_labels

def identify_router(graph: Type[DirectedGraph]):
    
    counts = dict()
    max_count = 0

    identified_routers = []
    
    # record outbounds and inbounds
    for k, v in graph.nodes.items():
        counts[k] = counts.get(k, 0) + len(v.outbounds)

        count = len(v.inbounds) + len(v.outbounds)
        counts[k] = count

        if count > max_count:
            max_count = count
    

    # check for max connections
    for k, v in counts.items():
        if v == max_count:
            identified_routers.append(k)


    return ','.join(identified_routers)
    




if __name__ == '__main__':
    graph = read_nodes_into_graph('1 -> 2 -> 3 -> 5 -> 2 -> 1')
    r = identify_router(graph)
    print('response', r)