import re
import os

verbs_path = r'd:\German\verb_german\verbs.js'
keys_path = r'd:\German\verb_german\existing_keys.txt'

with open(verbs_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Match top level keys: "verb": {
all_keys = re.findall(r'"([^"]+)": {', content)
excluded = {'present', 'praet', 'ich', 'du', 'er', 'wir', 'ihr', 'sie'}
keys = [k for k in all_keys if k not in excluded]

with open(keys_path, 'w', encoding='utf-8-sig') as f:
    f.write('\n'.join(sorted(keys)))

print(f"Updated keys file with {len(keys)} verbs.")
