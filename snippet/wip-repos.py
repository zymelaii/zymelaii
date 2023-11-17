GRAPHQL_TEMPLATE = '''
query {{
    viewer {{
        repositories(
            first: {:d},
            orderBy: {{
                field: PUSHED_AT,
                direction: DESC
            }}
        ) {{
            nodes {{
                name
                owner {{
                    login
                }}
                description
            }}
        }}
    }}
}}
'''

TEMPLATES = {
    'title': "⏳ **What I've Been Working On Lately**",
    'repo': "- 📌 _**{repo}**_ ⣿ [{intro}](https://github.com/{owner}/{repo}) ⣿",
    'repo-without-intro': "- 📌 _**{repo}**_ [🚪](https://github.com/{owner}/{repo})",
    'none': "> 😏 Nothing to contribute for now, this looks pretty cool!",
}

def fetch(token: str, total: int):
    import requests, json
    gql = GRAPHQL_TEMPLATE.format(total)
    resp = requests.request(
        'post',
        "https://api.github.com/graphql",
        headers={
            'Authorization': f'bearer {token}',
        },
        data=json.dumps({'query': gql}),
    )
    resp.encoding = 'utf-8'
    return resp.json()

def generate(token: str, total: int):
    resp = fetch(token, total)
    results = resp['data']['viewer']['repositories']['nodes']
    for result in results:
        intro = (result['description'] or '').strip()
        result['repo'] = result['name']
        result['owner'] = result['owner']['login']
        result['intro'] = intro if len(intro) > 0 else None
    select = lambda e: 'repo-without-intro' if e['intro'] is None else 'repo'
    items = map(lambda e: TEMPLATES[select(e)].format(**e), results)
    body = '\n'.join(items) if len(results) > 0 else TEMPLATES['none']
    content = f"{TEMPLATES['title']}\n\n{body}\n"
    return content

def snippet_path():
    import os
    file = os.path.splitext(os.path.basename(__file__))[0]
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, file)
    return path

if __name__ == '__main__':
    import sys
    token = sys.argv[1]
    total = int(sys.argv[2])
    try:
        content = generate(token, total)
        with open(snippet_path(), 'w', encoding='utf-8') as f:
            f.write(content)
    except:
        pass
