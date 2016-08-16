package main

import (
	"fmt"

	"github.com/marioluan/abstract-data-types/golang/graph"
)

var (
	digraph *graph.Digraph
)

func init() {
	digraph = graph.NewDigraph()
}

func main() {
	nodeA := graph.Node("A")
	nodeB := graph.Node("B")
	edgeFromAToB := graph.Edge{Source: nodeA, Destination: nodeB}

	digraph.AddNode(nodeA)
	digraph.AddNode(nodeB)
	digraph.AddEdge(edgeFromAToB)

	fmt.Println(fmt.Sprintf("%+v", digraph))

	digraph.RemoveNode(nodeB)
	fmt.Println(fmt.Sprintf("%+v", digraph))

	digraph.AddNode(nodeB)
	fmt.Println(fmt.Sprintf("%+v", digraph))

	digraph.RemoveEdge(edgeFromAToB)
	fmt.Println(fmt.Sprintf("%+v", digraph))
}
