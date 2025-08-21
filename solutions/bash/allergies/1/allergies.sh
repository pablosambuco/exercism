#!/usr/bin/env bash

main () {
    declare -a ALLERGIES=(
        [1]="eggs"
        [2]="peanuts"
        [4]="shellfish"
        [8]="strawberries"
        [16]="tomatoes"
        [32]="chocolate"
        [64]="pollen"
        [128]="cats"
    )

    declare -a output=()

    param="$1"
    operation="$2"
    allergy="$3"

    found_allergy=false
    for value in ${!ALLERGIES[@]}
    do 
        if [[ $((value & param)) -gt 0 ]]
        then 
            case "${operation}" in
                list)
                    output+=("${ALLERGIES[${value}]}")
                ;;
                allergic_to)
                    if [[ "${ALLERGIES[${value}]}" == "${allergy}" ]]
                    then
                        found_allergy=true
                        break
                    fi
                ;;
            esac
        fi
    done
    
    case "${operation}" in 
        list)
            echo "${output[@]}"
        ;;
        allergic_to)
            echo "${found_allergy}"
        ;;
    esac
}

main "$@"

