#!/bin/sh

msg=$1
git config --global user.name 'github-actions[bot]'
git config --global user.email '41898282+github-actions[bot]@users.noreply.github.com'
git add README.md
if [ ! -e README.md ]; then exit; fi
git add README.md
if [ ! "`git status -s`" ]; then exit; fi
git commit -m "$msg" --allow-empty
