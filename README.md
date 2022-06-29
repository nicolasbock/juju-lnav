# `juju-lnav`

A script to look at logs from multiple Juju units

[![Lint](https://github.com/nicolasbock/juju-lnav/actions/workflows/lint.yml/badge.svg)](https://github.com/nicolasbock/juju-lnav/actions/workflows/lint.yml)
[![Launchpad](https://img.shields.io/badge/Launchpad-PPA-yellowgreen)](https://launchpad.net/~nicolasbock/+archive/ubuntu/juju-lnav)

## Description

The `juju-lnav` command displays multiple log files from multiple machines in
one view. For example,
          
```console
$ ./tools/juju-lnav octavia:/var/log/octavia/*.log{,1}
```

will open the current and the first rotated log files from all of the `octavia`
units.

Likewise

```console
$ ./tools/juju-lnav octavia:/var/log/octavia/*.log \
    nova-cloud-controller:/var/log/nova/*.log
```

Will load the logs on all `octavia` and all `nova-cloud-controller` units.

Using the included `logfile-locations.conf` file, it is also possible to load
the default log files for known applications, e.g.

```console
$ juju-lnav octavia
```

Will load all of the standard `octavia` log files. This includes potentially
rotated log files such as `/var/log/octavia/octavia-worker.log.1`.

## Installation

The script is a shell script and requires `bash`.

In order to install the script do one of the following:

1. Clone this repository or download the script itself
2. Install the [Debian package](https://launchpad.net/~nicolasbock/+archive/ubuntu/juju-lnav)

## Dependencies

The `lnav` log viewer needs to be installed separately either via snap

```console
$ sudo snap install lnav
```

The snap needs to be connected to the `ssh-keys` interface:

```console
$ sudo snap connect lnav:ssh-keys
```

or via package

```console
$ sudo apt install lnav
```

For more information on how to use `lnav` please visit
[lnav.org](https://lnav.org).
