#!/bin/bash

ag ' interface {' | grep type | awk '{print $2}' | sort -u | xargs -n 1   | sed -e 's/\([A-Z]\)/-\1/g' | awk -F'-' '{print $NF}' | tr '[:upper:]' '[:lower:]' | sort -u |  grep -E 'er$|or$|able$' > golang_interface_name.txt
