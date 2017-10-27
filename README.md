# snippets
Short bits of code that do simple tasks.

## Python 3

### Copy Files
[`cat.py`](https://github.com/rivermont/snippets/blob/master/cat.py)<br>
A simple script to concatenate all files in a directory into a single file.

    from os import listdir
    from shutil import copyfileobj

    dir_ = ''  # Directory to copy files from
    dest = ''  # Destination file

    files = listdir(dir_)

    with open(dest, 'w+', encoding='utf-8') as d:
        for file in files:
            with open(dir_ + file, encoding='utf-8', errors='ignore') as f:
                copyfileobj(f, d)


### Update pip
[`update-pip.py`](https://github.com/rivermont/snippets/blob/master/update-pip.py)<br>
A script to update all outdated pip packages.

    import pip
    from subprocess import call

    for dist in pip.get_installed_distributions():
        call("pip install --upgrade " + dist.project_name, shell=True)

### Zip Files
[`zip.py`](https://github.com/rivermont/snippets/blob/master/zip.py)
Zips all files in `dir_` into `out_file_name`.

    import shutil
    from os import makedirs


    def zip_files(out_file_name, dir_):
        """
        Creates a .zip file in the current directory containing all contents of dir_, then clears dir_.
        """
        shutil.make_archive(str(out_file_name), 'zip', dir_)
        shutil.rmtree(dir_)
        makedirs(dir_[:-1])



## Bash

### Update pip
[`update-pip.sh`](https://github.com/rivermont/snippets/blob/master/update-pip.sh)
A script to update all outdated pip packages.

    sudo pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo pip3 install -U

### Remove Empty Subdirectories
Recursively deletes all empty directories below current working directory.

    find . -type d -empty -delete

### Move from Subdirectories
Moves all files in subdirectories to current directory.

    find . -mindepth 2 -type f -print -exec mv {} . \;

***
