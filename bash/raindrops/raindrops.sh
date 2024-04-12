#!/usr/bin/env bash
main () {
   out=""
   if [ $(($1 % 3)) -eq 0 ]
   then
      out="${out}Pling"
   fi
   if [ $(($1 % 5)) -eq 0 ]
   then
      out="${out}Plang"
   fi
   if [ $(($1 % 7)) -eq 0 ]  
   then
      out="${out}Plong"
   fi
   if [ "${out}" == "" ]
   then
      out=$1
   fi
   echo "${out}"
}

main "$@"