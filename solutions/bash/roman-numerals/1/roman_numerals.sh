#!/usr/bin/env bash

main () {
    number=$1
    for pair in 1000,M 900,CM 500,D 400,CD 100,C 90,XC 50,L 40,XL 10,X 9,IX 5,V 4,IV 1,I
    do 
        IFS=","
        set -- ${pair}
        value=$1
        repeat=$((number/value))
        while [[ ${repeat} -gt 0 ]]; do
            echo -n $2
            repeat=$((repeat-1))
        done
        number=$((number%value))
    done
}

main "$@"