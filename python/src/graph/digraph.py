from edge import Edge

class Digraph():
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        
        self.nodes.append(node)
        self.edges[node] = []

    def addEdge(self, edge):
        if (edge.src not in self.nodes) or (edge.dest not in self.nodes):
            return ValueError("Edge contains unkown nodes.")
        
        self.edges[edge.src].append(edge.dest)
    
    def childenOf(self, node):
        return self.edges[node]

    def __str__(self):
        response = ""
        for src in self.edges:
            for dest in self.edges[src]:
                response += "" + str(src) + "->" + str(dest) + "\n"

        return response