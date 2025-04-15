package jujulnav

import (
	"encoding/json"
	"fmt"
	"net"
	"os"
	"os/exec"
	"strconv"
	"strings"
)

// The `juju status` object.
type Status struct {
	rawJSON  map[string]interface{}
	Machines map[int][]net.IP
}

// CommandRunner is a function type that matches the signature of exec.Command
type CommandRunner func(name string, arg ...string) *exec.Cmd

// Variable to allow mocking exec.Command in tests
var execCommand CommandRunner = exec.Command

// NewStatus creates and initializes a new Juju Status object. Note that this
// function calls the `juju` command and will fail if `juju status` returns an
// error. After successfully running `juju status`, the Status struct will be
// populated with some information on the current model.
func NewStatus() (Status, error) {
	status := Status{}
	out, err := execCommand("juju", "status", "--format", "json").CombinedOutput()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %s\n", err)
		fmt.Fprintln(os.Stderr, strings.TrimSpace(string(out)))
		return status, err
	}
	err = json.Unmarshal(out, &status.rawJSON)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %s\n", err)
		return status, err
	}
	status.parseMachines()
	return status, nil
}

func (s *Status) parseMachines() {
	if machines, ok := s.rawJSON["machines"]; ok {
		if s.Machines == nil {
			s.Machines = map[int][]net.IP{}
		}
		for machine_id, machine_details := range machines.(map[string]interface{}) {
			id, err := strconv.ParseInt(machine_id, 10, 64)
			if err != nil {
				fmt.Fprintf(os.Stderr, "Error parsing machine id: %s\n", err)
				return
			}
			s.Machines[int(id)] = []net.IP{}
			addresses := machine_details.(map[string]interface{})["ip-addresses"]
			for _, address := range addresses.([]interface{}) {
				IP := net.ParseIP(address.(string))
				s.Machines[int(id)] = append(s.Machines[int(id)], IP)
			}
		}
	}
}
