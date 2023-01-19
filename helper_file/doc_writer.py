import os
import yaml
import hashlib

def get_file_info(directory):
    file_info = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            with open(file_path, 'rb') as f:
                file_md5 = hashlib.md5(f.read()).hexdigest()
            file_info.append({
                'filename': file,
                'file_location': file_path,
                'file_size': file_size,
                'md5sum': file_md5
            })
    return file_info

def write_to_yaml(file_info, yaml_file):
    with open(yaml_file, 'w') as f:
        yaml.dump(file_info, f)

directory = '/Users/sn0550/Documents/linkml-tests'
file_info = get_file_info(directory)
write_to_yaml(file_info, 'file_info.yml')
