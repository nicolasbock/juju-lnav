# `juju-lnav`

A script to look at logs from multiple Juju units

[![Lint](https://github.com/nicolasbock/juju-lnav/actions/workflows/lint.yml/badge.svg)](https://github.com/nicolasbock/juju-lnav/actions/workflows/lint.yml)
[![Launchpad](https://img.shields.io/badge/Launchpad-PPA-yellowgreen)](https://launchpad.net/~nicolasbock/+archive/ubuntu/juju-lnav)

[![Get it from the Snap Store](https://snapcraft.io/en/light/install.svg)](https://snapcraft.io/juju-lnav)

## Description

The `juju-lnav` command displays multiple log files from multiple machines in one view. It uses the `lnav` log file viewer, [lnav.org](https://lnav.org), which needs to be installed separately. For example,

For example, after installing `lnav`,

```console
sudo snap install lnav
sudo snap connect juju-lnav:juju-bin juju
```

running

```console
juju-lnav octavia:/var/log/octavia/*.log{,1}
```

will open the current and the first rotated log files from all of the `octavia` units.

Likewise

```console
juju-lnav octavia:/var/log/octavia/*.log \
  nova-cloud-controller:/var/log/nova
```

Will load the logs on all `octavia` ending in `.log` and all files on `nova-cloud-controller` units.

## Installation

The script is a shell script and requires `bash`.

In order to install the script do one of the following:

1. Clone this repository or download the script itself
2. Install the [Debian package](https://launchpad.net/~nicolasbock/+archive/ubuntu/juju-lnav)

## Dependencies

The `lnav` log viewer needs to be installed separately either via snap

```console
sudo snap install lnav
```

The snap needs to be connected to the `ssh-keys` interface:

```console
sudo snap connect lnav:ssh-keys
```

or via package

```console
sudo apt install lnav
```

For more information on how to use `lnav` please visit [lnav.org](https://lnav.org).
