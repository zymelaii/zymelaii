#!/bin/sh

PAT="$1"
REPO_NUM="$2"
URL="https://api.github.com/graphql"
GRAPHQL="query { viewer { repositories(first: $REPO_NUM, orderBy: {field: PUSHED_AT, direction: DESC}) { nodes { name owner { login } pushedAt } } } }"

curl $URL -H "Authorization: bearer $PAT" -X POST -d "{ \"query\": \"$GRAPHQL\" }" -s
