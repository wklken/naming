#!/bin/bash

ag -s '^package ' -G "\.go$" --nofilename | grep -v '//\|{{\|_test\|[0-9]' | sort -u | awk '{print $2}' | grep -v 'beego\|caddy\|chi\|dapr\|dgraph\|echo\|etcd\|gin\|go-micro\|go-zero\|go\|influxdb\|istio\|kubernetes\|logrus\|moby\|redis\|tidb' | sort -u
