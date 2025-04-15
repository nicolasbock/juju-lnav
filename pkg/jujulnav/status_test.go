package jujulnav

import (
	"bytes"
	"net"
	"os"
	"os/exec"
	"testing"
)

// MockCmd is a custom exec.Cmd struct for mocking
type MockCmd struct {
	Stdout *bytes.Buffer
}

func (m *MockCmd) CombinedOutput() ([]byte, error) {
	return m.Stdout.Bytes(), nil
}
func TestNewStatusWithInvalidJSON(t *testing.T) {
	execCommand = func(name string, args ...string) *exec.Cmd {
		return &exec.Cmd{
			Stdout: bytes.NewBufferString("invalid json"),
		}
	}

	// Call NewStatus and expect an error
	_, err := NewStatus()
	if err == nil {
		t.Fatalf("expected an error, got nil")
	}

	// Restore execCommand to its original state
	execCommand = exec.Command
}
func TestNewStatusWithError(t *testing.T) {
	execCommand = func(name string, args ...string) *exec.Cmd {
		return &exec.Cmd{
			CombinedOutput: (&MockCmd{
				Err: fmt.Errorf("mock error"),
			}).CombinedOutput,
		}
	}

	// Call NewStatus and expect an error
	_, err := NewStatus()
	if err == nil {
		t.Fatalf("expected an error, got nil")
	}

	// Restore execCommand to its original state
	execCommand = exec.Command
}

func TestNewStatus(t *testing.T) {
	testdata, err := os.ReadFile("../../testdata/juju-status.json")
	if err != nil {
		t.Fatalf("failed to read file: %v", err)
	}

	execCommand = func(name string, args ...string) *exec.Cmd {
		return &exec.Cmd{
			Stdout: bytes.NewBuffer(testdata),
		}
	}

	// Call NewStatus and check the result
	status, err := NewStatus()
	if err != nil {
		t.Fatalf("expected no error, got %v", err)
	}
	if status.Machines == nil {
		t.Fatalf("expected Machines to be initialized, got nil")
	}
	if len(status.Machines) != 2 {
		t.Fatalf("expected 2 machines, got %d", len(status.Machines))
	}
	if !status.Machines[1][0].Equal(net.ParseIP("192.168.1.1")) {
		t.Fatalf("expected IP 192.168.1.1, got %v", status.Machines[1][0])
	}
	if !status.Machines[2][0].Equal(net.ParseIP("192.168.1.2")) {
		t.Fatalf("expected IP 192.168.1.2, got %v", status.Machines[2][0])
	}
	if !status.Machines[2][1].Equal(net.ParseIP("192.168.1.3")) {
		t.Fatalf("expected IP 192.168.1.3, got %v", status.Machines[2][1])
	}

	// Restore execCommand to its original state
	execCommand = exec.Command
}
