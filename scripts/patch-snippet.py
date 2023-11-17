PROFILE = 'README.md'

def locate_by_hint(hint: str) -> int:
    with open(PROFILE, 'r', encoding='utf-8') as f:
        for (line, text) in enumerate(f.readlines()):
            if text.find(hint) != -1:
                return line
    return -1

def fetch_snippet_content(snippet: str) -> str | None:
    import os
    dyn_snippet = os.path.join('snippet', snippet)
    if os.path.exists(dyn_snippet):
        with open(dyn_snippet, 'r', encoding='utf-8') as f:
            return f.read()
    static_snippet = os.path.join('snippet', f'{snippet}.static')
    if os.path.exists(static_snippet):
        with open(static_snippet, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def patch_snippet(line: int, snippet: str, patch_before: bool) -> None:
    content = fetch_snippet_content(snippet)
    if content is None:
        return
    f = open(PROFILE, 'r', encoding='utf-8')
    rows = f.readlines()
    rows.insert(line - 1 if patch_before else line + 1, content)
    f.close()
    with open(PROFILE, 'w', encoding='utf-8') as f:
        f.write(''.join(rows))

def apply_snippet(hint: str, snippet: str, patch_before: bool) -> None:
    line = locate_by_hint(hint)
    if line != -1:
        patch_snippet(line, snippet, patch_before)

if __name__ == '__main__':
    import sys
    hint = sys.argv[1]
    snippet = sys.argv[2]
    patch_before = sys.argv[3].strip().lower() == 'true'
    try:
        apply_snippet(hint, snippet, patch_before)
    except:
        pass
