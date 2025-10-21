import os
import re
import sys
from pathlib import Path

def extract_python_code(text):
    """Extract Python code from markdown code blocks."""
    pattern = r'```python\n(.*?)\n```'
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

def main():
    # Check if parent directory was provided as argument
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <parent_directory> [output_folder_name]")
        sys.exit(1)
    
    parent_dir = sys.argv[1]
    
    if not os.path.isdir(parent_dir):
        print(f"Error: Directory '{parent_dir}' does not exist.")
        sys.exit(1)
    
    # Get the output folder name from argument or use default
    if len(sys.argv) >= 3:
        output_folder_name = sys.argv[2]
    else:
        output_folder_name = input("Enter the name for the output folder: ").strip()
    
    if not output_folder_name:
        print("Error: Output folder name cannot be empty.")
        return
    
    # Create the output folder
    output_folder = os.path.join(parent_dir, output_folder_name)
    os.makedirs(output_folder, exist_ok=True)
    print(f"Created output folder: {output_folder}")
    
    # Process each ID folder
    id_folders = [d for d in os.listdir(parent_dir) 
                  if os.path.isdir(os.path.join(parent_dir, d)) and d != output_folder_name]
    
    if not id_folders:
        print("No ID folders found.")
        return
    
    processed_count = 0
    
    for folder_id in sorted(id_folders):
        folder_path = os.path.join(parent_dir, folder_id)
        output_file_path = os.path.join(folder_path, 'output.txt')
        
        # Check if output.txt exists
        if not os.path.isfile(output_file_path):
            print(f"Warning: output.txt not found in {folder_id}")
            continue
        
        try:
            # Read the output.txt file
            with open(output_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract Python code blocks
            python_codes = extract_python_code(content)
            
            if not python_codes:
                print(f"Warning: No Python code block found in {folder_id}/output.txt")
                continue
            
            # Use the first Python code block found
            code = python_codes[0]
            
            # Create the patched file
            patched_filename = f"{folder_id}_patched.py"
            patched_filepath = os.path.join(output_folder, patched_filename)
            
            with open(patched_filepath, 'w', encoding='utf-8') as f:
                f.write(code)
            
            print(f"✓ Extracted and saved: {patched_filename}")
            processed_count += 1
            
        except Exception as e:
            print(f"Error processing {folder_id}: {str(e)}")
    
    print(f"\nCompleted! Processed {processed_count} folders.")
    print(f"All patched files saved to: {output_folder}")

if __name__ == "__main__":
    main()