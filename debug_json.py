import json
import sys

def find_error():
    try:
        with open('d:/German/verb_german/verbs.js', 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        json_str = content.strip()
        if json_str.startswith('window.VERB_DB ='):
            json_str = json_str[len('window.VERB_DB ='):].strip()
        if json_str.endswith(';'):
            json_str = json_str[:-1].strip()
        
        try:
            json.loads(json_str)
            print("VALID")
        except json.JSONDecodeError as e:
            print(f"Error at line {e.lineno}, col {e.colno}")
            lines = json_str.splitlines()
            start = max(0, e.lineno - 5)
            end = min(len(lines), e.lineno + 5)
            for i in range(start, end):
                prefix = ">> " if i == e.lineno - 1 else "   "
                print(f"{prefix}{i+1}: {lines[i]}")
    except Exception as e:
        print(f"Generic error: {e}")

if __name__ == "__main__":
    find_error()
