#!/bin/bash

TMP_FILE=".readme.md"



add_part_separator() {
    echo "" >> ${TMP_FILE}
    echo "------------------------------------" >> ${TMP_FILE}
    echo "" >> ${TMP_FILE}
}


# cat readme_header.md > ${TMP_FILE}
# add_part_separator
cat bool_names.md >> ${TMP_FILE}
add_part_separator
cat loop_names.md >> ${TMP_FILE}
add_part_separator

GO_INTERFACE_COUNT=(wc -l golang_interface_names.md)
echo "## Golang interface name $GO_INTERFACE_COUNT" >> ${TMP_FILE}
cat golang_interface_names.md >> ${TMP_FILE}
add_part_separator
cat antonym_synonym_verb_ajd.md >> ${TMP_FILE}


cat readme_header.md > README.md

./gh-md-toc ${TMP_FILE} >> README.md
cat ${TMP_FILE} >> README.md

rm ${TMP_FILE}
