package main

import (
	"flag"
	"fmt"

	"github.com/nicolasbock/juju-lnav/pkg/jujulnav"
)

var version = ""

func main() {
	fmt.Printf("juju-lnav-%s\n", version)

	status := jujulnav.NewStatus()

	debug := flag.Bool("debug", false, "Print debug information")
	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(), "Usage of %s:\n", flag.CommandLine.Name())
		flag.PrintDefaults()
	}
	flag.Parse()

	if *debug {
		fmt.Println("Debug mode")
	}

	fmt.Printf("Machines: %v\n", status.Machines)
}
