import json
from util import format_args

snippets = {}
luaGlobals = ["exports"]

def add_snippet(name, arguments):
    arguments_formatted = format_args(arguments)

    snippets[name] = {
        "prefix": name,
        "body": [
            "{0}({1})".format(name, arguments_formatted)
        ]
    }
    luaGlobals.append(name)

def gen_file():
    return json.dumps(snippets, indent=4)

def gen_global_file():
    return json.dumps(luaGlobals, indent=4)
