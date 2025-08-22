#!/usr/bin/env bash

declare -A translation=(
    ["UUU"]="Phenylalanine"
    ["AUG"]="Methionine"
    ["UUC"]="Phenylalanine"
    ["UUA"]="Leucine"
    ["UUG"]="Leucine"
    ["UCU"]="Serine"
    ["UCC"]="Serine"
    ["UCA"]="Serine"
    ["UCG"]="Serine"
    ["UAU"]="Tyrosine"
    ["UAC"]="Tyrosine"
    ["UGU"]="Cysteine"
    ["UGC"]="Cysteine"
    ["UGG"]="Tryptophan"
    ["UAA"]="STOP"
    ["UAG"]="STOP"
    ["UGA"]="STOP"
)

main () {
    strand="$1"
    codon=""
    aminoacids=()
    length=${#strand}
    for ((i = 0; i < length; i++)); do
        char="${strand:i:1}"
        codon=${codon}${char}
        if [ ${#codon} -eq 3 ]
        then
            # If the codon is not in the known translations, fail
            if [ -z "${translation[${codon}]}" ]
            then
                echo "Invalid codon"
                exit 1
            fi
            aminoacid=${translation[${codon}]}
            if [ "${aminoacid}" == "STOP" ]
            then
                break
            fi
            # Append to the results list
            aminoacids+=("${aminoacid}")
            codon=""
        fi
    done
    # If the loop ended and there is a codon of unknown length, then fail
    if [ "${#codon}" -ne 3 ] && [ "${#codon}" -ne 0 ]
    then
        echo "Invalid codon"
        exit 1
    fi
    echo "${aminoacids[*]}"
}

# call main with all of the positional arguments
main "$@"
