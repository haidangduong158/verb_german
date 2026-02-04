import os
import re

verbs_path = r'd:\German\verb_german\verbs.js'
batch_path = r'd:\German\verb_german\batch_3_new.js'

with open(verbs_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

with open(batch_path, 'r', encoding='utf-8-sig') as f:
    batch_content = f.read().strip()

# We expect the content to end with "};" or "}\n};"
# We want to replace the last "};" with ",\n" + batch_content + "\n};"

# Find the last closing brace of the main object
# The main object starts with window.VERB_DB = {
# and ends with };

# Use regex to find the last 2 characters which should be };
if content.strip().endswith('};'):
    # Remove the last };
    new_content = content.strip()[:-2].rstrip()
    # Ensure it ends with a comma if it doesn't already
    if not new_content.endswith(','):
        new_content += ','
    
    new_content += '\n' + batch_content + '\n};'
    
    with open(verbs_path, 'w', encoding='utf-8-sig') as f:
        f.write(new_content)
    print("SUCCESS: Merged Batch 3 into verbs.js")
else:
    print("ERROR: Could not find '};' at the end of verbs.js")
