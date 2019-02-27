#!/bin/sh

DATA=data-practice
find "$DATA" -name '*.in' -print0 | xargs -t -0 -i sh -c 'cat {} | ./main.py'
