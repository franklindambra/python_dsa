import collections


class Graph:

    def __init__(self):
        self.adj = collections.defaultdict(set)
        self.num_nodes = 0
        self.num_edges = 0

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = set()
            self.num_nodes += 1
            print(f"Node '{node}' added")
        else:
            print(f"Node '{node}' already exists")

    def add_edge(self, node1, node2):

        if node1 not in self.adj:
            self.add_node(node1)
        if node2 not in self.adj:
            self.add_node(node2)

        if node2 not in self.adj[node1]:
            self.adj[node1].add(node2)
            self.adj[node2].add(node1)
            self.num_edges += 1
            print(f"Edge between '{node1}' and {node2}")
        else:
            print(f"edge between '{node1}' and '{node2}' already exists")

    def display_graph(self):
        print("\n--- Graph Adjacency List ---")
        for node, neighbors in self.adj.items():
            #.items() unpacks the dict, for each entry creates a tuple i.ie {"A": {"B", "C", "E"}, "B": {"A", "D"}, ...} -> [("A", {"B", "C", "E"}), ("B", {"A", "D"}), ...]
            neighbor_list = sorted(list(neighbors))
            print(f"Node {node}: => {neighbor_list}")
        print(f"\nTotal Nodes: {self.num_nodes}, Total Edges: {self.num_edges}")

    def remove_node(self, node_to_remove):

        if node_to_remove in self.adj:
            for neighbor in list(self.adj[node_to_remove]):
                self.adj[neighbor].remove(node_to_remove)
                self.num_edges -= 1

            del self.adj[node_to_remove]
            self.num_nodes -= 1
            print(f"Node '{node_to_remove}' and its edges removed")
        else:
            print(f"Node '{node_to_remove}' not found")

    def get_neighbors(self, node):
        return self.adj.get(node)








if __name__ == "__main__":
    # Create a new graph instance
    g = Graph()

    # Add some nodes
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_node("E")

    # Add edges to connect them
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "E")
    g.add_edge("E", "A") # Adding an existing node/edge check

    # Display the current state of the graph
    g.display_graph()

    # Check neighbors
    print("\nNeighbors of 'A':", g.get_neighbors("A"))

    # Remove a node and display the updated graph
    g.remove_node("C")
    g.display_graph()

    # Attempt to add a node that already exists
    g.add_node("B")
