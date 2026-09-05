#!/usr/bin/env python3
"""Report actual compiler diagnostics from the current tool response only."""
import json
import os
import re
import shlex
import sys


def feedback(payload):
    value = payload.get('tool_input') or {}
    command = value if isinstance(value, str) else value.get('command', value.get('cmd', ''))
    try:
        lexer = shlex.shlex(command, posix=True, punctuation_chars=';&|')
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError:
        return None
    start = True
    compiled = False
    for token in tokens:
        if token in {';', '&&', '||', '|'}:
            start = True
        elif start:
            compiled |= os.path.basename(token) in {'latexmk','pdflatex','xelatex','lualatex'}
            start = False
    if not compiled:
        return None
    response = payload.get('tool_response', payload.get('tool_output', {}))
    text = response if isinstance(response, str) else '\n'.join(str(response.get(k,'')) for k in ('output','stdout','stderr'))
    lines = [line for line in text.splitlines() if re.search(r'Undefined control sequence|(?:Reference|Citation).*undefined|cannot find image|File .*not found|Fatal error|Overfull.*hbox',line)]
    if not lines:
        return None
    message = 'Compiler diagnostics from this invocation:\n' + '\n'.join(dict.fromkeys(lines[:8]))
    if os.getenv('CURSOR_PLUGIN_ROOT'):
        return {'additional_context':message}
    return {'hookSpecificOutput':{'hookEventName':'PostToolUse','additionalContext':message}}


if __name__ == '__main__':
    try:
        result = feedback(json.load(sys.stdin))
        if result:
            print(json.dumps(result,ensure_ascii=False))
    except (ValueError, TypeError, AttributeError):
        pass
