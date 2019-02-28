#!/bin/sh

FILE1=$1
FILE2=$2
echo podipouet
cat $FILE1
echo -n 1111 > $FILE2
>&2 echo "error"

