import os

def merge_extra():
    verbs_file = r'd:\German\verb_german\verbs.js'
    extra_file = r'd:\German\verb_german\extra_verbs.js'
    
    with open(verbs_file, 'r', encoding='utf-8-sig') as f:
        content = f.read().strip()
    
    with open(extra_file, 'r', encoding='utf-8-sig') as f:
        extra_content = f.read().strip()

    if content.endswith('};'):
        base_content = content[:-2].strip()
        if not base_content.endswith('{') and not base_content.endswith(','):
            base_content += ','
        new_content = base_content + "\n" + extra_content + "\n};"
        with open(verbs_file, 'w', encoding='utf-8-sig') as f:
            f.write(new_content)
        print("Merge check completed.")
    else:
        print("Error: verbs.js format unexpected.")

if __name__ == "__main__":
    merge_extra()
