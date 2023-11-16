#!/bin/sh

git config --global user.name $COMMITTER_NAME
git config --global user.email $COMMITTER_EMAIL
git add README.md
if [ ! -e README.md ]; then exit; fi
git add README.md
if [ ! "`git status -s`" ]; then exit; fi
git commit -m "chore: auto deploy" --allow-empty
git push
