import os
import yaml
import hashlib
import uuid

def get_file_info(directory):
    file_info = []
    count = 0
    total_files = sum([len(files) for r, d, files in os.walk(directory)])
    for root, dirs, files in os.walk(directory):
        for file in files:
            count += 1
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            with open(file_path, 'rb') as f:
                file_md5 = hashlib.md5(f.read()).hexdigest()
            file_info.append({
                'id': str(uuid.uuid4()),
                'filename': file,
                'file_location': file_path,
                'file_size': file_size,
                'md5sum': file_md5,
                'belongs_to_container': "alspacdcs:74fcdd8a-fec5-4ef2-9dd1-3bc16b418640"
                
            })
            print(f'Processed {count} of {total_files} files')
    return file_info

def write_to_yaml(file_info, yaml_file):
    with open(yaml_file, 'w') as f:
        yaml.dump(file_info, f)

directory = '/mnt/storage/private/alspacdata/datasets/dataset_cnv_550_g1/released/2015-11-09/data/raw/'
file_info = get_file_info(directory)
write_to_yaml(file_info, 'file_info.yaml')
