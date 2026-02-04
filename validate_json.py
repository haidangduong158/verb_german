import json
import sys

try:
    with open('d:/German/verb_german/verbs.js', 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Remove JS prefix and suffix
    json_str = content.strip()
    if json_str.startswith('window.VERB_DB ='):
        json_str = json_str[len('window.VERB_DB ='):].strip()
    if json_str.endswith(';'):
        json_str = json_str[:-1].strip()
    
    json.loads(json_str)
    print("SUCCESS")
except json.JSONDecodeError as e:
    print(f"ERROR: {e.msg} at line {e.lineno} column {e.colno}")
    # Print the context
    lines = json_str.splitlines()
    start = max(0, e.lineno - 3)
    end = min(len(lines), e.lineno + 2)
    for i in range(start, end):
        prefix = ">> " if i == e.lineno - 1 else "   "
        print(f"{prefix}{i+1}: {lines[i]}")
except Exception as e:
    print(f"OTHER ERROR: {str(e)}")
