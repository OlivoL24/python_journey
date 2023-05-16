# Script to find duplicate files based on md5 hash

import os
import hashlib
import argparse

def find_duplicate_photos(folder):
    file_hash = {}
    photo_extentions = ['.jpg', '.png', '.jpeg', '.gif']
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            for ext in photo_extentions:
                if filename.endswith(ext):
                    filepath = os.path.join(dirpath, filename)
                    # print(filepath)
                    with open(filepath, 'rb') as f:
                        file_content = f.read()
                    file_hash_value = hashlib.md5(file_content).hexdigest()
                    if file_hash_value in file_hash:
                        file_hash[file_hash_value].append(filepath)
                    else:
                        file_hash[file_hash_value] = [filepath]
    return [file_list for file_list in file_hash.values() if len(file_list) > 1]

def parse_args():
    parser = argparse.ArgumentParser(description="Find duplicate files in a folder")
    parser.add_argument('-f',"--folder", help='Folder to search for duplicates')
    args = parser.parse_args()
    return args.folder

if __name__ == '__main__':
    folder = parse_args() # Change to the folder you want to check for duplicates
    print(folder)
    duplicates = find_duplicate_photos(folder)
    if duplicates:
        print("Duplicate files:")
        for file_list in duplicates:
            print('\n'.join(file_list))
            print()
    else:
        print("No duplicate files found.")

