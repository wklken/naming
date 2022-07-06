#!/bin/bash

ag ' struct {' --ignore "*_test.go" | grep type | awk '{print $2}' | grep -v '{\|(\|\$\|`\|"\|/\|\[\|<\|}' | grep -v '[[:digit:]]' |  sort -u  > golang_struct_names.txt
