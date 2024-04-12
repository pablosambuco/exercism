#!/usr/bin/env bash

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    echo "This library of functions should be sourced into another script" >&2
    exit 4
fi
bash_version=$((10 * BASH_VERSINFO[0] + BASH_VERSINFO[1]))
if (( bash_version < 43 )); then
    echo "This library requires at least bash version 4.3" >&2
    return 4
fi

# Due to inherent bash limitations around word splitting and globbing,
# functions that are intended to *return a list* are instead required to
# receive a nameref parameter, the name of an array variable that will be
# populated in the list function.
# See the filter, map and reverse functions.

# Also note that nameref parameters cannot have the same name as the
# name of the variable in the calling scope.


# Append some elements to the given list.
list::append () {
    local -n __array=$1
    shift
    __array=( "${__array[@]}" "$@" )
}

# Return only the list elements that pass the given function.
list::filter () {
    local __function=$1
    local -n __array=$2
    local -n __output=$3
    for element in ${__array[@]}
    do
        ${__function} ${element} && __output=( "${__output[@]}" "${element}" )
    done
}

# Transform the list elements, using the given function,
# into a new list.
list::map () {
    local __function=$1
    local -n __array=$2
    local -n __output=$3
    for element in ${__array[@]}
    do
        new_value=$(${__function} ${element})
       __output=( "${__output[@]}" "${new_value}" )
    done
}

# Left-fold the list using the function and the initial value.
list::foldl () {
    local __function=$1
    local __value=$2
    local -n __array=$3
    for element in ${__array[@]}
    do
        __value=$(${__function} "${__value}" "${element}")
    done
    echo "${__value}"
}

# Right-fold the list using the function and the initial value.
list::foldr () {
    local __function=$1
    local __value=$2
    local -n __array=$3
    list::fold "${__function} ${__value} $(list::reverse __array)"
}

# Return the list reversed
list::reverse () {
    set -o noglob
    local -n __array=$1
    local -n __output=$2
    for element in ${__array[@]}
    do
        __output=( "${element}" "${__output[@]}")
    done
}
