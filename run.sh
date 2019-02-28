#!/bin/sh

DATA=data
find "$DATA" -name '*.in' -print0 | xargs -t -0 -I{} sh -c 'cat {} | ./main.py | ./scorer.py'
