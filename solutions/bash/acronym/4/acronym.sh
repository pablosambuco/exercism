#!/usr/bin/env bash

main() {
    str="${*//[^a-zA-Z\']/ }"
    for word in ${str}; do acronym="${acronym}${word:0:1}"; done
    echo "${acronym^^}"
}

main "$@"
