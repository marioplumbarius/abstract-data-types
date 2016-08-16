package graph

// WeightedEdge is the unit which connects two Node instances and computes a weight to this connection.
type WeightedEdge struct {
	Edge

	Weight uint
}
