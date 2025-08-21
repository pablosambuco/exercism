#!/bin/bash

main () {
   year=$1
   by4=$(expr ${year} % 4)
   by100=$(expr ${year} % 100)
   by400=$(expr ${year} % 400)
   if [ ${by4} -eq 0 -a ${by100} -ne 0 -o ${by400} -eq 0 ]
      then echo "true"
      else echo "false"
   fi
}
if [[ $@ =~ ^[0-9]+$ ]]
then
   main "$@"
else
   echo "Usage: leap.sh <year>"
   exit 1
fi
