import os
import yaml
import hashlib
import uuid
from multiprocessing import Pool, cpu_count, Manager

def process_file(root, file, progress_queue):
    file_path = os.path.join(root, file)
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        file_md5 = hashlib.md5()
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            file_md5.update(chunk)
        file_md5 = file_md5.hexdigest()
    file_info = {
        'id': str(uuid.uuid4()),
        'filename': file,
        'file_size': file_size,
        'md5sum': file_md5,
        'belongs_to_container': "alspacdcs:74fcdd8a-fec5-4ef2-9dd1-3bc16b418640"
    }
    progress_queue.put(file_info)
    return file_info

def get_file_info(directory):
    file_info = []
    count = 0
    total_files = sum([len(files) for r, d, files in os.walk(directory)])
    with Manager() as manager, Pool(processes=cpu_count()) as pool:
        progress_queue = manager.Queue()
        for root, dirs, files in os.walk(directory):
            results = pool.starmap(process_file, [(root, file, progress_queue) for file in files])
            file_info.extend(results)
            count += len(results)
            while not progress_queue.empty():
                progress_file = progress_queue.get()
                print(f'Processed {progress_file["filename"]}')
        print(f'Processed {count} of {total_files} files')
    return file_info

def write_to_yaml(file_info, yaml_file):
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(file_info, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

#        yaml.dump(file_info, f, default_flow_style=False, allow_unicode=True, sort_keys=['id', 'filename', 'file_size', 'md5sum', 'belongs_to_container'])

directory = '/mnt/storage/private/alspacdata/datasets/dataset_wgs_hiseq_g1/freeze/out/data'
file_info = get_file_info(directory)
write_to_yaml(file_info, 'file_info_hiseq3.yaml')
