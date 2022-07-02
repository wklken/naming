#!/bin/bash

add_part_separator() {
    echo "" >> README.md
    echo "------------------------------------" >> README.md
    echo "" >> README.md
}


cat readme_header.md > README.md
add_part_separator
cat bool_names.md >> README.md
add_part_separator
cat loop_names.md >> README.md
add_part_separator

GO_INTERFACE_COUNT=(wc -l golang_interface_names.md)
echo "## Golang interface name $GO_INTERFACE_COUNT" >> README.md
cat golang_interface_names.md >> README.md
add_part_separator
cat antonym_synonym_verb_ajd.md >> README.md
