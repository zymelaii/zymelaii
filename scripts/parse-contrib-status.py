#!/bin/python3

import json, sys

if __name__ == '__main__':
    jsonfile = sys.argv[1]
    with open(jsonfile, 'r') as f:
        resp = json.loads(f.read())
        nodes = resp['data']['viewer']['repositories']['nodes']
        nodes = list(map(lambda e: (e['name'], e['owner']['login'], e['pushedAt']), nodes))
        repos = nodes[:3]
        for (name, owner, pushedAt) in repos:
            print(f"{name} {owner} {pushedAt}")
