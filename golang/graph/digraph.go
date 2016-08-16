package graph

import "fmt"

const (
	sourceNodeDoesNotExist = "source node `%s` does not exist"
	emptyStr               = ""
)

// Digraph implements Graph and represents a directed graph.
type Digraph struct {
	nodes map[Node]Node
	edges map[Node][]Edge
}

// NewDigraph initializes and returns a new instance of Digraph.
func NewDigraph() *Digraph {
	n := map[Node]Node{}
	e := map[Node][]Edge{}

	return &Digraph{nodes: n, edges: e}
}

// AddNode implements Graph.AddNode.
func (d *Digraph) AddNode(node Node) {
	d.nodes[node] = node

	// initializes a new edge array if it is empty.
	if d.edges[node] == nil {
		d.edges[node] = []Edge{}
	}
}

// RemoveNode implements Graph.RemoveNode.
func (d *Digraph) RemoveNode(node Node) {
	delete(d.nodes, node)
	delete(d.edges, node)
}

// AddEdge implements Graph.AddEdge.
func (d *Digraph) AddEdge(edge Edge) error {

	// tests for existance of edge.Source
	if d.edges[edge.Source] == nil {
		return fmt.Errorf(sourceNodeDoesNotExist, edge.Source)
	}

	// if the edge already exist, returns
	for _, innerEdge := range d.edges[edge.Source] {
		if innerEdge.Destination == edge.Destination {
			return nil
		}
	}

	// pushes the edge to the list of edges
	d.edges[edge.Source] = append(d.edges[edge.Source], edge)

	return nil
}

// RemoveEdge implements Graph.RemoveEdge.
func (d *Digraph) RemoveEdge(edge Edge) {

	// finds and removes the edge from the list of edges
	for i, innerEdge := range d.edges[edge.Source] {
		if innerEdge.Destination == edge.Destination {
			d.edges[edge.Source][i] = NullEdge()
		}
	}
}
