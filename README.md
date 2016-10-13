# A10ctl

a10ctl is a small script to manage servers within A10 lb partitions. The
initial intend for this was to use it for automating deployments of core
components by managing the A10 for seamless upgrades.

Currenly we support:
 * Listing all servers
 * Enabling a server
 * Disabling a server
 * Backing up running conf

## Install

There are a few different ways you can install t:
* Use setuptools: `pip install git+ssh://git@github.com/fim/a10ctl.git`
* Download the zipfile from [github](https://github.com/fim/a10ctl.git) page and install it.
* Checkout the source: `git clone git://git@github.com/fim/a10ctl.git` and install it yourself.

## Usage
*All examples assume you have already setup your api key!*

List all servers:

```sh
$ a10ctl -H a10.example.com -u admin -p foobar list
```

Mark server as inactive:

```sh
$ a10ctl -H a10.example.com -u admin -p foobar down server-name
```

Mark a server as active:

```sh
$ a10ctl -H a10.example.com -u admin -p foobar up server-name
```

Check statistics for a single server

```sh
$ a10ctl -H a10.example.com -u admin -p foobar stats server-name
```

Backup running conf:

```sh
$ a10ctl -H a10.example.com -u admin -p foobar backup
```

Use conf files to pass arguments:

```sh
$ a10ctl -c conf/test.conf list
```
