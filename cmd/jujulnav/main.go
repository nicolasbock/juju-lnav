package main

import (
	"flag"
	"fmt"
	"os"
	"os/exec"

	"github.com/nicolasbock/juju-lnav/pkg/jujulnav"
)

var version = ""

func isCommandInstalled(command string) bool {
	_, err := exec.LookPath(command)
	return err == nil
}

func main() {
	fmt.Printf("juju-lnav-%s\n", version)

	debug := flag.Bool("debug", false, "Print debug information")
	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(), "Usage of %s:\n", flag.CommandLine.Name())
		flag.PrintDefaults()
	}
	flag.Parse()

	if *debug {
		fmt.Println("Debug mode")
	}

	if !isCommandInstalled("juju") {
		fmt.Fprintln(os.Stderr, `Please install juju with

sudo snap install juju

And rerun this script.`)
		os.Exit(1)
	}

	if !isCommandInstalled("lnav") {
		fmt.Fprintln(os.Stderr, `Please install lnav with

sudo snap install lnav

And rerun this script.`)
		os.Exit(1)
	}

	status, err := jujulnav.NewStatus()
	if err != nil {
		os.Exit(1)
	}

	fmt.Printf("Machines: %v\n", status.Machines)
}
