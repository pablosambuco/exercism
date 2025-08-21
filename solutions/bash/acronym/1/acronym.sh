#!/usr/bin/env bash

is_valid_char() {
    local chr="$1"
    if [[ ${chr} =~ [a-zA-Z\'] ]]; then
        echo true
    else
        echo false
    fi
}

main() {
    str="${@}"
    len=${#str}
    acronym=""

    i=0
    valid_current="false"
    while [ ${i} -lt ${len} ]; do

        chr=${str:${i}:1}
        valid_prev=${valid_current}
        valid_current=$(is_valid_char "${chr}")
        if [ "${valid_current}" == "true" ] && [ "${valid_prev}" == "false" ]; then
            acronym=${acronym}${chr^}
        fi
        i=$((i + 1))
    done
    echo ${acronym}
}

main "$@"
