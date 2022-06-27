# juju-lnav

A script to look at logs from multiple Juju units

## Description

The `juju-lnav` command is a helper script to call `lnav` (needs to be installed
via package or snap) on multiple machines, applications, or units. For example,
          
```console
$ ./tools/juju-lnav octavia:/var/log/octavia/*.log{,1}
```

Will open the current and the first rotated log files from all of the `octavia`
units.

Likewise

```console
$ ./tools/juju-lnav octavia:/var/log/octavia/*.log \
    nova-cloud-controller:/var/log/nova/*.log
```

Will load the logs on all `octavia` and all `nova-cloud-controller` units.

For more information on how to use `lnav` please visit lnav.org.
