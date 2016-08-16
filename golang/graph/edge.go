package graph

// Edge is the unit which connects two Node instances.
type Edge struct {
	Source      Node
	Destination Node
}

func NullEdge() Edge {
	var nilEdge Edge

	return nilEdge
}
