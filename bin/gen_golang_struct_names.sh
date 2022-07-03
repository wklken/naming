#!/bin/bash

ag ' struct {' | grep type | awk '{print $2}' | grep -v '{\|(\|\$\|`\|"\|/' |  sort -u  > k8s_struct_naming.txt
