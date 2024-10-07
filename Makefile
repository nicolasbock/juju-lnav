.PHONY: juju-lnav-go
version := $(shell git describe --tags --always --dirty)

juju-lnav-go:
	go build -v -o $@ -ldflags "-X main.version=$(version)" ./cmd/jujulnav

.PHONY: image
image: build
	docker build --file build/Dockerfile --tag juju-lnav .
