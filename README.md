# `juju-lnav`

A script to look at logs from multiple Juju units

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

## Dependencies

The `lnav` log viewer needs to be installed separately either via snap

```console
$ sudo snap install lnav
```

or via package

```console
$ sudo apt install lnav
```

For more information on how to use `lnav` please visit lnav.org.
