# snippets
Short bits of code that do simple tasks.

## Python 3

### Copy Files
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
A script to update all outdated pip packages.

    import pip
    from subprocess import call

    for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)

### Zip Files
Zips all files in `dir` into `out_file_name`.

    import shutil
    from os import makedirs

    def zip(out_file_name, dir):
        '''
        Creates a .zip file in the current directory containing all contents of dir, then clears dir.
        '''
        shutil.make_archive(str(out_file_name), 'zip', dir)
        shutil.rmtree(dir)
    makedirs(dir[:-1])


## Bash

### Update pip
A script to update all outdated pip packages.

***
