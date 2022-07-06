#!/bin/bash

ag 'func ' --ignore "*_test.go" | sed -e 's/([^()]*)//g' | awk '{print $2}' | sed -e 's/\([A-Z]\)/-\1/g' | sed -e "s/^-//" | awk -F '[-_.,:]' '{print $1}' | grep -v '{\|(\|\$\|`\|"\|/\|\[\|<\|}\||\|*\|#' | grep -v '[[:digit:]]' |  tr '[:upper:]' '[:lower:]' | sort -u > function_names.txt
