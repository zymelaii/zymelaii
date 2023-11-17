def get_patch_list(schema: str) -> list:
    import os, json
    curdir = os.path.dirname(__file__)
    patch_file = os.path.join(curdir, '..', 'template', f'{schema}.patch-list')
    patch_file = os.path.abspath(patch_file)
    if not os.path.exists(patch_file):
        return []
    with open(patch_file, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def apply(patch_list: list):
    import importlib
    patch_snippet = importlib.import_module('patch-snippet')
    for patch in patch_list:
        patch_snippet.apply_snippet(**patch)

if __name__ == '__main__':
    import sys
    schema = sys.argv[1]
    try:
        patch_list = get_patch_list(schema)
        apply(patch_list)
    except:
        pass
