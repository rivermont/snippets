from os import listdir
from shutil import copyfileobj

dir_ = ''  # Directory to copy files from
dest = ''  # Destination file

files = listdir(dir_)

with open(dest, 'w+', encoding='utf-8') as d:
    for file in files:
        with open(dir_ + file, encoding='utf-8', errors='ignore') as f:
            copyfileobj(f, d)
