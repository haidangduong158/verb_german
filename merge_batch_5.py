import json
import os

def merge():
    main_file = r'd:\German\verb_german\verbs.js'
    new_file = r'd:\German\verb_german\batch_5_new.js'
    
    if not os.path.exists(main_file):
        print(f"Error: {main_file} not found")
        return

    with open(main_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract existing JSON part
    start_idx = content.find('{', content.find('=') + 1)
    end_idx = content.rfind('}')
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not find JSON object in verbs.js")
        return
        
    json_str = content[start_idx:end_idx+1]
    db = json.loads(json_str)
    
    # Read batch 5 content
    with open(new_file, 'r', encoding='utf-8') as f:
        # Batch 5 is a list of "key": {val}, separated by newlines or commas
        # We'll wrap it in braces to make it valid JSON
        batch_content = f.read().strip()
        # Add braces if they aren't there
        if not batch_content.startswith('{'):
            batch_content = '{' + batch_content + '}'
        
        # Clean trailing commas if any
        if batch_content.endswith(',}'):
            batch_content = batch_content[:-2] + '}'
            
        new_data = json.loads(batch_content)
    
    # Merge
    added_count = 0
    duplicate_count = 0
    for key, value in new_data.items():
        if key not in db:
            db[key] = value
            added_count += 1
        else:
            duplicate_count += 1
            
    # Write back
    new_json_str = json.dumps(db, indent=4, ensure_ascii=False)
    final_content = f"window.VERB_DB = {new_json_str};"
    
    with open(main_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print(f"Merge complete. Added: {added_count}, Duplicates ignored: {duplicate_count}")
    print(f"New total: {len(db)}")

if __name__ == "__main__":
    merge()
