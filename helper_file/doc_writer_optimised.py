import os
from posixpath import splitext
import pysam
import yaml
import hashlib
import uuid
import argparse
from operator import itemgetter
from natsort import natsorted
from multiprocessing import Pool, cpu_count, Manager
from bgen_reader import open_bgen
import pysam

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='Directory of files you wish to use the doc writer on.', required=True)
    parser.add_argument('-o', '--output', help='Output path you wish the helper file to be saved at. Please do not include the file name as this is generated.', required=True)
    return parser.parse_args()


def process_file(root, file, progress_queue):
    file_path = os.path.join(root, file)
    file_extension = os.path.splitext(file)[1]
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
        'id': f'alspacdcs:{uuid.uuid4()}',
        'name': file,
        'md5sum': file_md5,
        'filesize': human_readable_size(file_size),
        'filetype': file_extension
    }
    
    # if bgen file add number of variants and number of samples
    if file_extension == '.bgen':
        with open_bgen(file_path, verbose=False) as bgen: 
            num_samples = bgen.nsamples
            num_variants = bgen.nvariants
            
        # update file info dict
        file_info.update({'number_of_variants': num_variants,
                          'number_of_participants': num_samples})

    elif file_extension in ['.vcf', '.vcf.gz']:
        with pysam.VariantFile(file_path) as vcf:
            num_samples = len(vcf.header.samples)
            num_variants = sum(1 for _ in vcf)

        # update file info dict
        file_info.update({'number_of_variants': num_variants,
                          'number_of_participants': num_samples})

    elif file_extension == '.sample':
        num_samples = sum(1 for _ in open(file_path)) - 2
    
        # update file info dict
        file_info.update({'number_of_participants': num_samples})
    
    progress_queue.put(file_info)
    return file_info


def human_readable_size(size, decimal_places=1):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f}{unit}"


def get_file_info(directory):
    file_info = []
    count = 0
    total_files = sum([len(files) for r, d, files in os.walk(directory)])
    with Manager() as manager, Pool(processes=cpu_count()) as pool:
        progress_queue = manager.Queue()
        
        # iterate over files in directory
        for root, dirs, files in os.walk(directory):
            results = pool.starmap(process_file, [(root, file, progress_queue) for file in files])
            file_info.extend(results)
            count += len(results)
            # while not progress_queue.empty():
            #     progress_file = progress_queue.get()
            #     #print(f'Processed {progress_file["filename"]}')
        print(f'Processed {count} of {total_files} files')
    file_info = natsorted(file_info, key=itemgetter(*['name']))
    return sorted(file_info, key=itemgetter('filetype'))

def write_to_yaml(file_info, yaml_file):
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(file_info, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


if __name__ == '__main__':
    
    opts = init()
    directory = opts.directory
    file_info = get_file_info(directory)
    write_to_yaml(file_info, f'{opts.output}/helper.yaml')
