#!/usr/bin/env bash

main() {
    echo "$@" | sed -E "s/([a-z\'])[a-z\']*[^a-z\']*/\U\1/gi"
}

main "$@"
