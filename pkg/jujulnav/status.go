package jujulnav

type Status struct {
	Machines []int
}

func NewStatus() Status {
	return Status{}
}
