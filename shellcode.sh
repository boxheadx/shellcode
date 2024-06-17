#!/bin/bash

hexdump -X $1 | grep 0001000 -A$2 | sed -e 's/^\w*//g' | sed -e 's\00\\g' | tr -d '\n' | sed -e 's/\  /\\x/g'
