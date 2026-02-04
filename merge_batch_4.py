import os

def merge_batch():
    verbs_file = r'd:\German\verb_german\verbs.js'
    batch_file = r'd:\German\verb_german\batch_4_new.js'
    
    if not os.path.exists(batch_file):
        print(f"Error: {batch_file} not found")
        return

    with open(verbs_file, 'r', encoding='utf-8-sig') as f:
        content = f.read().strip()
    
    with open(batch_file, 'r', encoding='utf-8-sig') as f:
        batch_content = f.read().strip()

    # The content of verbs.js ends with };
    if content.endswith('};'):
        # Remove the closing };
        base_content = content[:-2].strip()
        
        # Ensure there's a comma if the last character isn't { or ,
        if not base_content.endswith('{') and not base_content.endswith(','):
            base_content += ','
            
        new_content = base_content + "\n" + batch_content + "\n};"
        
        with open(verbs_file, 'w', encoding='utf-8-sig') as f:
            f.write(new_content)
        print("Merge complete!")
    else:
        print("Error: verbs.js does not end with };")

if __name__ == "__main__":
    merge_batch()
