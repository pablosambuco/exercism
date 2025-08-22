#!/usr/bin/env bash

declare -A scores
scores["A"]=1
scores["B"]=3
scores["C"]=3
scores["D"]=2
scores["E"]=1
scores["F"]=4
scores["G"]=2
scores["H"]=4
scores["I"]=1
scores["J"]=8
scores["K"]=5
scores["L"]=1
scores["M"]=3
scores["N"]=1
scores["O"]=1
scores["P"]=3
scores["Q"]=10
scores["R"]=1
scores["S"]=1
scores["T"]=1
scores["U"]=1
scores["V"]=4
scores["W"]=4
scores["X"]=8
scores["Y"]=4
scores["Z"]=10

main() {
    word="${1^^}"
    length=${#word}
    value=0
    for ((i = 0; i < length; i++)); do
        char="${word:i:1}"
        value=$((value + ${scores[${char}]}))
    done
    echo ${value}
}

main "$@"
