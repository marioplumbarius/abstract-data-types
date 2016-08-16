package graph

// Graph abstract data type specification.
type Graph interface {
	// AddNode adds the node to the graph, if it is not there.
	AddNode(node Node)

	// AddEdge adds the edge to the graph, if it is not there.
	// Returns an error if edge.source does not exist.
	AddEdge(edge Edge) error

	// RemoveNode removes the node from the graph, if it is there.
	RemoveNode(node Node)

	// RemoveEdge removes the edge from the graph, if it is there.
	RemoveEdge(edge Edge)
}
