#!/bin/bash

ag 'func ' | sed -e 's/([^()]*)//g' | awk '{print $2}' | sed -e 's/\([A-Z]\)/-\1/g' | sed -e "s/^-//" | awk -F '[-_.,:]' '{print $1}' |  grep -v '{\|(\|\$\|`\|"\|/' |  tr '[:upper:]' '[:lower:]' | sort -u > function_names.txt
