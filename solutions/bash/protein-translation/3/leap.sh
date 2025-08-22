#!/bin/bash

main () {
   year=$1
   by4=$((year % 4))
   by100=$((year % 100))
   by400=$((year % 400))
   if [ $by4 -eq 0 ] && [ $by100 -ne 0 ] || [ $by400 -eq 0 ]
      then echo "true"
      else echo "false"
   fi
}
if [[ $* =~ ^[0-9]+$ ]]
then
   main "$@"
else
   echo "Usage: leap.sh <year>"
   exit 1
fi
