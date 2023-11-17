#!/bin/sh

hint=$1
snippet=$2

line=`cat README.md | grep -n "$hint" -m 1 | awk -F: '{print $1}'`
sed -i "${line}i\\\\" README.md
line=$[$line-1]
sed -i "${line}r${snippet}" README.md
